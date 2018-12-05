from Snackbar.Helper.Database import getcurrbill, get_payment
from Snackbar.Models.Item import Item
from Snackbar.Models.User import User
from Snackbar.Models.History import History
from tablib import Dataset
from Snackbar import db
from os import path
from datetime import datetime
from sqlalchemy import extract


def rest_bill(userid):
  curr_bill = getcurrbill(userid)
  total_payment = get_payment(userid)
  rest_amount = -curr_bill + total_payment
  return rest_amount


def get_unpaid(userid, itemid):
  n_unpaid = db.session.query(History).filter(History.userid == userid).filter(History.itemid == itemid).filter(extract('month', History.date) == datetime.now().month).filter(extract('year', History.date) == datetime.now().year).count()
  if n_unpaid is None:
    n_unpaid = 0
  return n_unpaid


def make_xls_bill(filename, fullpath):
  header = list()
  header.append('name')
  for entry in Item.query:
    header.append('{}'.format(entry.name))
  header.append('bill')
  excel_data = Dataset()
  excel_data.headers = header
  for instance in User.query.filter(User.hidden.is_(False)):
    firstline = list()
    firstline.append(u'{} {}'.format(instance.firstName, instance.lastName))
    for record in Item.query:
      firstline.append('{}'.format(get_unpaid(instance.userid, record.itemid)))
    firstline.append('{0:.2f}'.format(rest_bill(instance.userid)))
    excel_data.append(firstline)
  with open(path.join(fullpath, filename), 'wb') as f:
    f.write(excel_data.xls)
  return