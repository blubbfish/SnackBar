from flask_admin import Admin
from SnackBar import db
from Snackbar.Models import *
import flask_login as loginflask

from MyAdminIndexView import MyAdminIndexView
from AnalyticsView import AnalyticsView
from MyPaymentModelView import MyPaymentModelView
from MyUserModelView import MyUserModelView
from MyItemModelView import MyItemModelView
from MyHistoryModelView import MyHistoryModelView
from MyAdminModelView import MyAdminModelView
from MySettingsModelView import MySettingsModelView
from SnackBarIndexView import SnackBarIndexView

def setup_admin(app):
  init_login(app)
  admin = Admin(app, name='SnackBar Admin Page', index_view=MyAdminIndexView(), base_template='my_master.html')
  admin.add_view(AnalyticsView(name='Bill', endpoint='bill'))
  admin.add_view(MyPaymentModelView(Inpayment, db.session, 'Inpayment'))
  admin.add_view(MyUserModelView(User, db.session, 'User'))
  admin.add_view(MyItemModelView(Item, db.session, 'Items'))
  admin.add_view(MyHistoryModelView(History, db.session, 'History'))
  admin.add_view(MyAdminModelView(Coffeeadmin, db.session, 'Admins'))
  admin.add_view(MySettingsModelView(Settings, db.session, 'Settings'))
  admin.add_view(SnackBarIndexView(name='Back to Snack Bar', endpoint='back'))


def init_login(app):
  login_manager = loginflask.LoginManager()
  login_manager.init_app(app)

  # Create User loader function
  @login_manager.user_loader
  def load_user(user_id):
    return db.session.query(Coffeeadmin).get(user_id)