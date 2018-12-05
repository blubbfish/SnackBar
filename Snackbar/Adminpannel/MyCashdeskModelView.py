from flask_admin.contrib.sqla import ModelView
import flask_login as loginflask
from datetime import datetime

class MyCashdeskModelView(ModelView):
  can_create = True
  can_export = True
  can_delete = True
  can_edit = True
  export_types = ['csv']
  column_descriptions = dict()
  column_default_sort = ('date', True)
  column_filters = ('item', 'date')
  form_args = dict(date=dict(default=datetime.now()), price=dict(default=0))

  def date_format(self, context, model, name):
    field = getattr(model, name)
    if field is not None:
      return field.strftime('%Y-%m-%d %H:%M')
    else:
      return ""

  column_formatters = dict(date=date_format)

  def is_accessible(self):
    return loginflask.current_user.is_authenticated