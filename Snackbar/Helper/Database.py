import csv
from Snackbar import db, databaseName
from Snackbar.Models import Settings, User, Item, Inpayment, Coffeeadmin
import os


def set_default_settings():
  with open('defaultSettings.csv') as csvfile:
    reader = csv.DictReader(csvfile)
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
    reader = csv.DictReader(csvfile)
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
  return


def database_exist():
  if not os.path.isfile("Snackbar/"+databaseName):
    return False
  return True