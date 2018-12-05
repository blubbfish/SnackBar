from Snackbar import db
from datetime import datetime

class History(db.Model):
  historyid = db.Column(db.Integer, primary_key=True, autoincrement=True)
  userid = db.Column(db.Integer, db.ForeignKey('user.userid'))
  user = db.relationship('User', backref=db.backref('history', lazy='dynamic'))
  itemid = db.Column(db.Integer, db.ForeignKey('item.itemid'))
  item = db.relationship('Item', backref=db.backref('items', lazy='dynamic'))
  price = db.Column(db.Float)
  date = db.Column(db.DateTime)

  def __init__(self, user=None, item=None, price=0, date=None):
    self.user = user
    self.item = item
    self.price = price
    if date is None:
      date = datetime.now()
    self.date = date

  def __repr__(self):
    return 'User {} bought {} for {} on the {}'.format(self.user, self.item, self.price, self.date)
