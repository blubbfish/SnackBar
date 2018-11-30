from Snackbar import db

class User(db.Model):
  userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
  firstName = db.Column(db.String(80), nullable=False, default='')
  lastName = db.Column(db.String(80), nullable=False, default='')
  imageName = db.Column(db.String(240))
  email = db.Column(db.String(120), nullable=False, default='')
  hidden = db.Column(db.Boolean)
  startmoney = db.Column(db.Float, nullable=False, default=0.0)

  def __init__(self, firstname='', lastname='', email='', imagename='', startmoney=''):
    if not firstname:
      firstname = ''
    if not lastname:
      lastname = ''
    if not imagename:
      imagename = ''
    if not email:
      email = 'example@example.org'
    if not startmoney:
      startmoney = 0

    self.hidden = False
    self.firstName = firstname
    self.lastName = lastname
    self.imageName = imagename
    self.email = email
    self.startmoney = startmoney

  def __repr__(self):
    return u'{} {}'.format(self.firstName, self.lastName)
