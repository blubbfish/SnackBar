from Snackbar import app
from Snackbar.Helper.Database import get_users_with_leaders
from Snackbar.Helper.Appearance import monster_image, image_from_folder
from flask import render_template, request, redirect, url_for

current_sorting = ""

class Titlepage():
  @app.route('/')
  def initial():
    global current_sorting
    initusers = get_users_with_leaders(True)
    if current_sorting == "az":
      users = sorted(initusers, key=lambda k: k['firstName'])
    elif current_sorting == "za":
      users = sorted(initusers, key=lambda k: k['firstName'])
      users.reverse()
    elif current_sorting == "coffee19":
      users = sorted(initusers, key=lambda k: k['coffeeMonth'])
    elif current_sorting == "coffee91":
      users = sorted(initusers, key=lambda k: k['coffeeMonth'])
      users.reverse()
    else:
      current_sorting = "az"
      users = sorted(initusers, key=lambda k: k['firstName'])
    return render_template('index.html', users=users, current_sorting=current_sorting)

  @app.route('/sort/<sorting>')
  def sort(sorting):
    global current_sorting
    current_sorting = sorting
    return redirect(url_for('initial'))

  @app.route('/icon/')
  def default_icon():
    return get_icon(None)

  @app.route('/icon/<icon>')
  def get_icon(icon):
      return image_from_folder(icon, app.config['ICON_FOLDER'], "static/unknown_icon.svg")

  @app.route('/image/')
  def default_image():
    userID = request.args.get('userID')
    return monster_image(None, userID)

  @app.route('/image/<filename>')
  def image(filename):
    userID = request.args.get('userID')
    return monster_image(filename, userID)
