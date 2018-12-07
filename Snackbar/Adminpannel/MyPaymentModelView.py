from flask_admin.contrib.sqla import ModelView
from sqlalchemy import func
from datetime import datetime
import flask_login as loginflask
from Snackbar.Models.Inpayment import Inpayment
from Snackbar.Models.Cashdesk import Cashdesk
from Snackbar.Models.User import User
from Snackbar.Helper.Database import settings_for
from Snackbar.Helper.Billing import rest_bill


class MyPaymentModelView(ModelView):
  can_create = True
  can_delete = True
  can_edit = True
  can_export = True
  export_types = ['csv']
  column_default_sort = ('date', True)
  column_filters = ('user', 'amount', 'date')
  form_args = dict(date=dict(default=datetime.now()), amount=dict(default=0))
  list_template = 'admin/custom_list.html'
  
  def date_format(self, context, model, name):
    field = getattr(model, name)
    return field.strftime('%Y-%m-%d %H:%M')

  column_formatters = dict(date=date_format)

  def is_accessible(self):
    return loginflask.current_user.is_authenticated

  def page_sum(self, current_page):
    # this should take into account any filters/search inplace
    _query = self.session.query(Inpayment).limit(self.page_size).offset(current_page * self.page_size)
    page_sum = sum([payment.amount for payment in _query])
    if page_sum is None:
      page_sum = 0
    return page_sum

  def total_sum(self):
    # this should take into account any filters/search inplace
    total_sum = self.session.query(func.sum(Inpayment.amount)).scalar()
    if total_sum is None:
      total_sum = 0
    return total_sum

  def total_sum_cashdesk(self):
    # this should take into account any filters/search inplace
    total_sum = self.session.query(func.sum(Cashdesk.price)).scalar()
    if total_sum is None:
      total_sum = 0
    return total_sum

  def cash_sum(self):
    money_start = settings_for('startmoney')
    if money_start is '':
      money_start = 0
    if money_start is not 0:
      money_start = float(money_start)
    money_start = money_start + self.total_sum()
    money_start = money_start + self.total_sum_cashdesk()
    return money_start

  def total_list(self):
    sum = 0
    for instance in User.query.filter(User.hidden.is_(False)):
      sum = sum + rest_bill(instance.userid)
    return sum

  def render(self, template, **kwargs):
    # we are only interested in the list page
    if template == 'admin/custom_list.html':
      # append a summary_data dictionary into kwargs
      _current_page = kwargs['page']
      kwargs['summary_data'] = [
        {'title': 'Page Total', 'amount': '{0:.2f}'.format(self.page_sum(_current_page))},
        {'title': 'Grand Total', 'amount': '{0:.2f}'.format(self.total_sum())},
        {'title': 'Money in cash point', 'amount': '{0:.2f}'.format(self.cash_sum())},
        {'title': 'Money on List', 'amount': '{0:.2f}'.format(self.total_list())}
      ]
      kwargs['summary_title'] = [{'title': ''}, {'title': 'Amount'}, ]
    return super(MyPaymentModelView, self).render(template, **kwargs)
