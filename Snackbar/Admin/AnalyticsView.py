from flask_admin import BaseView, expose
from Snackbar.Models import User

class AnalyticsView(BaseView):
  @expose('/')
  def index(self):
    initusers = list()
    for instance in User.query.filter(User.hidden.is_(False)):
        initusers.append({'name': u'{} {}'.format(instance.firstName, instance.lastName),'userid': '{}'.format(instance.userid),'bill': rest_bill(instance.userid)})
    users = sorted(initusers, key=lambda k: k['name'])
    return self.render('admin/test.html', users=users)

  @expose('/reminder/')
  def reminder(self):
    for aUser in User.query.filter(User.hidden.is_(False)):
      send_reminder(aUser)
    return redirect(url_for('admin.index'))

  @expose('/export/')
  def export(self):
    filename = 'CoffeeBill_{}_{}.xls'.format(datetime.now().date().isoformat(),datetime.now().time().strftime('%H-%M-%S'))
    fullpath = os.path.join(current_app.root_path, app.config['STATIC_FOLDER'])
    make_xls_bill(filename, fullpath)
    return send_from_directory(directory=fullpath, filename=filename, as_attachment=True)

  def is_accessible(self):
    return loginflask.current_user.is_authenticated
