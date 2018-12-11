# coding=utf-8

from flask_admin.contrib.sqla import ModelView
from Snackbar import app
import flask_login as loginflask
from flask_admin.form.upload import FileUploadField

class MyItemModelView(ModelView):
  can_export = True
  export_types = ['csv']
  form_excluded_columns = 'items'

  base_path = app.config['ICON_FOLDER']
  form_overrides = dict(icon=FileUploadField)
  form_args = {
    'icon': {
      'base_path': base_path
    }
  }

  column_default_sort = 'name'
  column_formatters = dict(price=lambda view, context, model, name: u'{0:.2f} €'.format(model.price))

  def is_accessible(self):
    return loginflask.current_user.is_authenticated