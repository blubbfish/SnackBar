from flask_admin import expose, BaseView

class SnackBarIndexView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('initial'))
