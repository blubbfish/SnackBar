from Snackbar import db

class Settings(db.Model):
  settingsid = db.Column(db.Integer, primary_key=True, autoincrement=True)
  key = db.Column(db.String(80), unique=True)
  value = db.Column(db.String(600))

  def __init__(self, key='', value=''):
    if not key:
      key = ''
    if not value:
      value = ''
    self.key = key
    self.value = value

  def __repr__(self):
    return self.key