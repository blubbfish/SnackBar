from Snackbar import db

class Coffeeadmin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False, default='')
  password = db.Column(db.String(64))
  
  @staticmethod
  def is_authenticated():
    return True

  @staticmethod
  def is_active():
    return True

  @staticmethod
  def is_anonymous():
    return False

  def get_id(self):
    return self.id
