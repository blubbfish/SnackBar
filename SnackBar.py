# coding: utf-8

from Snackbar import app
from Snackbar.Helper.Autoreminder import setup_schedule, stop_schedule
from Snackbar.Helper.Database import database_exist, set_default_settings, build_sample_db
from Snackbar.Adminpannel import setup_admin
from Snackbar.Frontpage import setup_frontpage
from optparse import OptionParser
from werkzeug.wsgi import DispatcherMiddleware


def simple(env, resp):
  resp(b'200 OK', [(b'Content-Type', b'text/plain')])
  return [b'You have to call the url_prefix']


def load_options(default_host="0.0.0.0", default_port="8000", url_prefix=""):
  """
  Parses command-line flags to configure the app.
  """
  parser = OptionParser()
  parser.add_option("-H", "--host", help="Hostname of the Flask app [default %s]" % default_host, default=default_host)
  parser.add_option("-P", "--port", help="Port for the Flask app [default %s]" % default_port, default=default_port)
  parser.add_option("-U", "--url_prefix", help="Url Prefix for the Flask app [default %s]" % url_prefix, default=url_prefix)
  parser.add_option("-d", "--debug", action="store_true", dest="debug")
  parser.add_option("-p", "--profile", action="store_true", dest="profile")
  options, _ = parser.parse_args()
  return options


def flaskrun(app, options=None):
  """
  Takes a flask.Flask instance and runs it.
  """
  if not options.debug:
    options.debug = False
  if options.profile:
    from werkzeug.contrib.profiler import ProfilerMiddleware
    app.config['PROFILE'] = True
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
    options.debug = True
  app.wsgi_app = DispatcherMiddleware(simple, {options.url_prefix: app.wsgi_app})
  app.config["APPLICATION_ROOT"] = options.url_prefix
  app.run(debug=options.debug, host=options.host, port=int(options.port))


if __name__ == "__main__":
  setup_schedule()
  if database_exist() is False:
    build_sample_db()
  set_default_settings()
  setup_admin(app)
  setup_frontpage()

  # app.run()
  # app.run(host='0.0.0.0', port=5000, debug=False)
  flaskrun(app, options=load_options())
  stop_schedule()
