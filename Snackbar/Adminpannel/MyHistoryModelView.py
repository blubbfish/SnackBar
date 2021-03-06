# coding=utf-8

from flask_admin.contrib.sqla import ModelView
import flask_login as loginflask
from datetime import datetime


class MyHistoryModelView(ModelView):
  can_create = True
  can_export = True
  can_delete = True
  can_edit = True
  export_types = ['csv']
  column_descriptions = dict()
  column_labels = dict(user='Name')
  column_default_sort = ('date', True)
  column_filters = ('user', 'item', 'date')
  form_args = dict(date=dict(default=datetime.now()), price=dict(default=0))

  # noinspection PyMethodMayBeStatic,PyUnusedLocal
  def date_format(self, context, model, name):
    field = getattr(model, name)
    if field is not None:
      return field.strftime('%Y-%m-%d %H:%M')
    else:
      return ""

  column_formatters = dict(date=date_format, price=lambda view, context, model, name: u'{0:.2f} €'.format(model.price))

  def is_accessible(self):
    return loginflask.current_user.is_authenticated
