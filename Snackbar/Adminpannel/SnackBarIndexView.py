from flask_admin import expose, BaseView
from flask import redirect, url_for

class SnackBarIndexView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('initial'))
