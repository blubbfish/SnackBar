from flask_admin import Admin
from SnackBar import app, db
from Snackbar.Models import *

from MyAdminIndexView import MyAdminIndexView
from AnalyticsView import AnalyticsView
from MyPaymentModelView import MyPaymentModelView
from MyUserModelView import MyUserModelView
from MyItemModelView import MyItemModelView
from MyHistoryModelView import MyHistoryModelView
from MyAdminModelView import MyAdminModelView
from MySettingsModelView import MySettingsModelView
from SnackBarIndexView import SnackBarIndexView

admin = Admin(app, name='SnackBar Admin Page', index_view=MyAdminIndexView(), base_template='my_master.html')
admin.add_view(AnalyticsView(name='Bill', endpoint='bill'))
admin.add_view(MyPaymentModelView(Inpayment, db.session, 'Inpayment'))
admin.add_view(MyUserModelView(User, db.session, 'User'))
admin.add_view(MyItemModelView(Item, db.session, 'Items'))
admin.add_view(MyHistoryModelView(History, db.session, 'History'))
admin.add_view(MyAdminModelView(Coffeeadmin, db.session, 'Admins'))
admin.add_view(MySettingsModelView(Settings, db.session, 'Settings'))
admin.add_view(SnackBarIndexView(name='Back to Snack Bar', endpoint='back'))