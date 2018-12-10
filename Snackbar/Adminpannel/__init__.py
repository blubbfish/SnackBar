from flask_admin import Admin
from SnackBar import db
import flask_login as loginflask

from Snackbar.Adminpannel.MyAdminIndexView import MyAdminIndexView
from Snackbar.Adminpannel.AnalyticsView import AnalyticsView
from Snackbar.Adminpannel.MyPaymentModelView import MyPaymentModelView
from Snackbar.Models.Inpayment import Inpayment
from Snackbar.Adminpannel.MyUserModelView import MyUserModelView
from Snackbar.Models.User import User
from Snackbar.Adminpannel.MyItemModelView import MyItemModelView
from Snackbar.Models.Item import Item
from Snackbar.Adminpannel.MyHistoryModelView import MyHistoryModelView
from Snackbar.Models.History import History
from Snackbar.Adminpannel.MyCashdeskModelView import MyCashdeskModelView
from Snackbar.Models.Cashdesk import Cashdesk
from Snackbar.Adminpannel.MyAdminModelView import MyAdminModelView
from Snackbar.Models.Coffeeadmin import Coffeeadmin
from Snackbar.Adminpannel.MySettingsModelView import MySettingsModelView
from Snackbar.Models.Settings import Settings
from Snackbar.Adminpannel.SnackBarIndexView import SnackBarIndexView

def setup_admin(app):
  init_login(app)
  admin = Admin(app, name='SnackBar Admin Page', index_view=MyAdminIndexView(), base_template='my_master.html')
  admin.add_view(AnalyticsView(name='Bill', endpoint='bill'))
  admin.add_view(MyPaymentModelView(Inpayment, db.session, 'Inpayment'))
  admin.add_view(MyUserModelView(User, db.session, 'User'))
  admin.add_view(MyItemModelView(Item, db.session, 'Items'))
  admin.add_view(MyHistoryModelView(History, db.session, 'History'))
  admin.add_view(MyCashdeskModelView(Cashdesk, db.session, 'Cash Desk'))
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