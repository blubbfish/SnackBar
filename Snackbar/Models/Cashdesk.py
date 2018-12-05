from Snackbar import db
from datetime import datetime

class Cashdesk(db.Model):
  cashid = db.Column(db.Integer, primary_key=True, autoincrement=True)
  price = db.Column(db.Float)
  date = db.Column(db.DateTime)
  item = db.Column(db.String(120))

  def __init__(self, item=None, price=0, date=None):
    self.item = item
    self.price = price
    if date is None:
      date = datetime.now()
    self.date = date

  def __repr__(self):
    return 'Cashdesk item {} for {} on {}'.format(self.item, self.price, self.date)