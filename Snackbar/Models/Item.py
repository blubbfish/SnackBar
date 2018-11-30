from Snackbar import db

class Item(db.Model):
  itemid = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(80), unique=True, nullable=False, default='')
  price = db.Column(db.Float)
  icon = db.Column(db.String(300))

  def __init__(self, name='', price=0):
    self.name = name
    self.price = price

  def __repr__(self):
    return self.name