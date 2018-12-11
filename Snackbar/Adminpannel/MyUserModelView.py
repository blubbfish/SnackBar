# coding=utf-8

from flask_admin.contrib.sqla import ModelView
import flask_login as loginflask
from Snackbar import app
from flask_admin.form.upload import FileUploadField

class MyUserModelView(ModelView):
  can_export = True
  export_types = ['csv']
  column_exclude_list = ['history', 'inpayment',]
  form_excluded_columns = ['history', 'inpayment']
  column_descriptions = dict(
    firstName='Name of the corresponding person'
  )

  base_path = app.config['IMAGE_FOLDER']
  form_overrides = dict(imageName=FileUploadField)
  form_args = {
    'imageName': {
      'base_path': base_path
    }
  }
  column_labels = dict(firstName='First Name',lastName='Last Name',imageName='User Image')
  
  column_default_sort = 'firstName'
  column_formatters = dict(startmoney=lambda view, context, model, name: u'{0:.2f} €'.format(model.startmoney))

  def is_accessible(self):
    return loginflask.current_user.is_authenticated
