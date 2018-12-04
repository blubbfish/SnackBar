from flask_admin.contrib.sqla import ModelView
import flask_login as loginflask

class MySettingsModelView(ModelView):
  can_create = False
  can_edit = False
  can_delete = False
  can_export = False
  column_editable_list = ['value']
  column_labels = dict(key='Name', value='Value')

  def is_accessible(self):
    return loginflask.current_user.is_authenticated
