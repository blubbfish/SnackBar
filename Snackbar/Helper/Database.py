from csv import DictReader
from Snackbar import db, databaseName
from Snackbar.Models.Settings import Settings
from Snackbar.Models.User import User
from Snackbar.Models.Item import Item
from Snackbar.Models.Inpayment import Inpayment
from Snackbar.Models.Coffeeadmin import Coffeeadmin
from Snackbar.Models.History import History
from Snackbar.Helper.Appearance import button_background, button_font_color
from Snackbar.Helper.Billing import get_unpaid
from os import path
from shutil import move
from sqlalchemy.sql import func, and_, extract
from datetime import datetime


def set_default_settings():
  with open('defaultSettings.csv') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
      key = '{}'.format(row['key'])
      db_entry = db.session.query(Settings).filter_by(key=key).first()
      if db_entry is None:
        newsettingitem = Settings(key='{}'.format(row['key']), value='{}'.format(row['value']))
        db.session.add(newsettingitem)
  db.session.commit()


def build_sample_db():
  db.drop_all()
  db.create_all()
  with open('userList.csv') as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
      newuser = User(firstname='{}'.format(row['FirstName']), lastname='{}'.format(row['LastName']), imagename='{}'.format(row['ImageName']), email='{}'.format(row['email']))
      db.session.add(newuser)
      initial_balance = '{}'.format(row['InitialBalance'])
      # noinspection PyBroadException,PyPep8
      try:
        initial_balance_float = float(initial_balance)
        if initial_balance_float != 0:
          initial_payment = Inpayment(amount=initial_balance)
          initial_payment.user = newuser
          db.session.add(initial_payment)
      except:
        pass
  itemname = ['Coffee', 'Water', 'Snacks', 'Cola']
  price = [0.2, 0.55, 0.2, 0.4]
  for i in range(len(itemname)):
    newitem = Item(name='{}'.format(itemname[i]), price=float('{}'.format(price[i])))
    newitem.icon = "item" + str(i + 1) + ".svg"
    db.session.add(newitem)
  newadmin = Coffeeadmin(name='admin', password='admin')
  db.session.add(newadmin)
  db.session.commit()
  set_version_nr("0.8.0")
  return


def database_migrate_from_05_to_07():
  move(databaseName,"Snackbar/"+databaseName)
  db.engine.execute("ALTER TABLE `user` ADD `startmoney` FLOAT NOT NULL DEFAULT 0.0")
  db.engine.execute("CREATE TABLE `cashdesk` (`cashid` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `price` FLOAT NOT NULL DEFAULT 0.0, `date` DATETIME NOT NULL, `item` TEXT NOT NULL);")
  return database_migrate_from_07_to_08()


def database_migrate_from_07_to_080():
  set_version_nr("0.8.0")
  return


def database_exist_or_upgrade():
  if path.isfile(databaseName):
    return database_migrate_from_05_to_07()
  if path.isfile("Snackbar/"+databaseName) and get_version_nr() is None:
    return database_migrate_from_07_to_080()
  if get_version_nr() == "0.8.0":
    return
  return build_sample_db()


def get_version_nr():
  try:
    res = db.engine.execute("SELECT `versionnr` FROM `database`")
    for row in res:
      return row[0]
  except:
    return None


def set_version_nr(nr):
  if get_version_nr() is None:
    db.engine.execute("CREATE TABLE `database` (`versionnr` VARCHAR (20));")
  else:
    db.engine.execute("DELETE FROM `database`;");
    db.engine.execute("VACUUM;")
  db.engine.execute("INSERT INTO `database` (`versionnr`) VALUES ('"+nr+"')")


def settings_for(key):
  db_entry = db.session.query(Settings).filter_by(key=key).first()
  if db_entry is None:
    return ''
  else:
    return db_entry.value


def get_leader_data(userid, skip):
  leader_info = list()
  if not skip:
    all_items = Item.query.filter(Item.icon is not None, Item.icon != '', Item.icon != ' ')
    i = 0
    for aItem in all_items:
      leader_id = int(get_leader(aItem.itemid))
      if leader_id == userid:
        item_id = int(aItem.itemid)
        icon_file = str(aItem.icon)
        position = (-7 + (i * 34))
        leader_info.append({"item_id": item_id, "icon": icon_file, "position": position})
        i = i + 1
  return leader_info


def get_leader(itemid):
  tmp_query = db.session.query(User.userid, func.count(History.price))
  tmp_query = tmp_query.outerjoin(History, and_(User.userid == History.userid, History.itemid == itemid, extract('month', History.date) == datetime.now().month, extract('year', History.date) == datetime.now().year))
  tmp_query = tmp_query.group_by(User.userid)
  tmp_query = tmp_query.order_by(func.count(History.price).desc()).first()
  if tmp_query[1] != 0:
    return tmp_query[0]
  else:
    return -1


def get_users_with_leaders(with_leader):
  initusers = list()
  all_items = Item.query.filter(Item.icon is not None, Item.icon != '', Item.icon != ' ')
  all_items_id = [int(instance.itemid) for instance in all_items]
  if len(all_items_id) > 0:
    itemid = all_items_id[0]
  else:
    itemid = ''
  for instance in User.query.filter(User.hidden.is_(False)):
    initusers.append({'firstName': u'{}'.format(instance.firstName), 'lastName': u'{}'.format(instance.lastName), 'imageName': '{}'.format(instance.imageName), 'id': '{}'.format(instance.userid), 'bgcolor': '{}'.format(button_background(instance.firstName + ' ' + instance.lastName)), 'fontcolor': '{}'.format(button_font_color(instance.firstName + ' ' + instance.lastName)), 'coffeeMonth': get_unpaid(instance.userid, itemid), 'leader': get_leader_data(instance.userid, not with_leader), 'email': '{}'.format(instance.email)})
  return initusers