from flask_admin import AdminIndexView, helpers, expose
import flask_login as loginflask
from LoginForm import LoginForm
from flask import redirect

class MyAdminIndexView(AdminIndexView):
  @expose('/')
  def index(self):
    if not loginflask.current_user.is_authenticated:
      return redirect(url_for('.login_view'))
    return super(MyAdminIndexView, self).index()

  @expose('/login/', methods=('GET', 'POST'))
  def login_view(self):
    login_form = LoginForm(request.form)
    if helpers.validate_form_on_submit(login_form):
      user = login_form.get_user()
      loginflask.login_user(user)
    if loginflask.current_user.is_authenticated:
      return redirect(url_for('.index'))
    self._template_args['form'] = login_form
    return super(MyAdminIndexView, self).index()

  @expose('/logout/')
  def logout_view(self):
    loginflask.logout_user()
    return redirect(url_for('.index'))