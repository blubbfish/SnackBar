from Snackbar import db
from datetime import datetime


class Inpayment (db.Model):
  paymentid = db.Column(db.Integer, primary_key=True, autoincrement=True)
  userid = db.Column(db.Integer, db.ForeignKey('user.userid'))
  user = db.relationship('User', backref=db.backref('inpayment', lazy='dynamic'))
  amount = db.Column(db.Float)
  date = db.Column(db.DateTime)
  notes = db.Column(db.String(120))

  def __init__(self, user = None, amount = None, date = None, notes = None):
    self.userid = user
    self.amount = amount
    self.notes = notes
    if date is None:
      date = datetime.now()
    self.date = date

  def __repr__(self):
    return 'User {} paid {} on the {}'.format(self.userid, self.amount, self.date)
