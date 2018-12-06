from flask_admin.contrib.sqla import ModelView
import flask_login as loginflask
from datetime import datetime
from Snackbar.Models.Cashdesk import Cashdesk
from sqlalchemy import func


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
  list_template = 'admin/custom_list.html'

  def is_accessible(self):
    return loginflask.current_user.is_authenticated

  def date_format(self, context, model, name):
    field = getattr(model, name)
    if field is not None:
      return field.strftime('%Y-%m-%d %H:%M')
    else:
      return ""

  column_formatters = dict(date=date_format)

  def page_sum(self, current_page):
    # this should take into account any filters/search inplace
    _query = self.session.query(Cashdesk).limit(self.page_size).offset(current_page * self.page_size)
    page_sum = sum([payment.price for payment in _query])
    if page_sum is None:
      page_sum = 0
    return '{0:.2f}'.format(page_sum)

  def total_sum(self):
    # this should take into account any filters/search inplace
    total_sum = self.session.query(func.sum(Cashdesk.price)).scalar()
    if total_sum is None:
      total_sum = 0
    return '{0:.2f}'.format(total_sum)

  def render(self, template, **kwargs):
    # we are only interested in the list page
    if template == 'admin/custom_list.html':
      # append a summary_data dictionary into kwargs
      _current_page = kwargs['page']
      kwargs['summary_data'] = [
        {'title': 'Page Total', 'price': self.page_sum(_current_page)},
        {'title': 'Grand Total', 'price': self.total_sum()},
        #{'title': 'Money in cash point', 'amount': self.cash_sum()},
      ]
      kwargs['summary_title'] = [{'title': ''}, {'title': 'Amount'}, ]
    return super(MyCashdeskModelView, self).render(template, **kwargs)