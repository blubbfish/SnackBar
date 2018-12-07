from Snackbar.Models.Item import Item
from Snackbar.Models.User import User
from Snackbar.Models.History import History
from Snackbar.Models.Inpayment import Inpayment
from tablib import Dataset
from Snackbar import db
from os import path
from datetime import datetime
from sqlalchemy import extract, func


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


def get_total(userid, itemid):
  n_unpaid = db.session.query(History).filter(History.userid == userid).filter(History.itemid == itemid).count()
  if n_unpaid is None:
    n_unpaid = 0
  return n_unpaid


def getcurrbill(userid):
  curr_bill_new = db.session.query(func.sum(History.price)).filter(History.userid == userid).scalar()
  if curr_bill_new is None:
    curr_bill_new = 0
  user_start = db.session.query(User.startmoney).filter(User.userid == userid).scalar()
  if user_start is None:
    user_start = 0
  curr_bill_new =  curr_bill_new + user_start
  return curr_bill_new


def get_payment(userid):
  total_payment_new = db.session.query(func.sum(Inpayment.amount)).filter(Inpayment.userid == userid).scalar()
  if total_payment_new is None:
    total_payment_new = 0
  return total_payment_new


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