from Snackbar import app, db
from flask import render_template
from jinja2 import Markup
from Snackbar.Models.User import User
from Snackbar.Models.Item import Item
from Snackbar.Models.History import History
from Snackbar.Helper.Ranking import get_rank
from Snackbar.Helper.Billing import get_unpaid, get_total, rest_bill
from Snackbar.Helper.Database import settings_for
from Snackbar.Helper.Appearance import reltime


class Userpage():
  @app.route('/user/<int:userid>', methods=['GET'])
  def user_page(userid):
    user_name = u'{} {}'.format(User.query.get(userid).firstName, User.query.get(userid).lastName)
    items = list()
    for instance in Item.query:
        rank_info = get_rank(userid, instance.itemid)
        items.append({
          'name': u'{}'.format(instance.name), 
          'price': instance.price, 
          'itemid': '{}'.format(instance.itemid), 
          'icon': '{}'.format(instance.icon),
          'count': get_unpaid(userid, instance.itemid),
          'total': get_total(userid, instance.itemid),
          'rank': rank_info['rank'],
          'ub': rank_info['upperbound'],
          'lb': rank_info['lowerbound']
        })
    no_users = User.query.filter(User.hidden.is_(False)).count()
    currbill = rest_bill(userid)
    can_change_image = settings_for('usersCanChangeImage')
    last_purchase = "-"
    last_purchase_item = History.query.filter(History.userid == userid).order_by(History.date.desc()).first()
    if last_purchase_item is not None:
        last_purchase = reltime(last_purchase_item.date)
    return render_template('choices.html', currbill=currbill, chosenuser=user_name, userid=userid, items=items, noOfUsers=no_users, canChangeImage=can_change_image, last_purchase=last_purchase)

  @app.route('/adduser', methods=('GET', 'POST'))
  def adduser():
    if request.method == 'POST':
      first_name_error = False
      first_name = ''
      if request.form['firstname'] is None or request.form['firstname'] == '':
        first_name_error = true
      else:
        first_name = request.form['firstname']
      last_name_error = False
      last_name = ''
      if request.form['lastname'] is None or request.form['lastname'] == '':
        last_name_error = true
      else:
        last_name = request.form['lastname']
      from email.utils import parseaddr
      email_error = False
      email = ''
      if request.form['email'] is None or request.form['email'] == '':
        email_error = true
      else:
        email = parseaddr(request.form['email'])[1]
        if email == '':
          email_error = true
      if not first_name_error and not last_name_error and not email_error:
        with app.app_context():
          filename = ''
          if 'image' in request.files:
            file = request.files['image']
            if file.filename != '' and allowed_file(file.filename):
              filename = secure_filename(file.filename)
              full_path = os.path.join(app.config['IMAGE_FOLDER'], filename)
              file.save(full_path)
          new_user = User(firstname=first_name, lastname=last_name, email=email, imagename=filename)
          db.session.add(new_user)
          db.session.commit()
          send_email_new_user(new_user)
          return redirect(url_for('initial'))
      else:
        return render_template('adduser.html', firstNameError=first_name_error, firstName=first_name, lastNameError=last_name_error, lastName=last_name, emailError=email_error, email=email)
    else:
      return render_template('adduser.html', firstNameError=False, firstName='', lastNameError=False, lastName='', emailError=False, email='')

  @app.template_filter("itemstrikes")
  def itemstrikes(value):
    counter = 0
    tag_opened = False
    out = ""
    if value > 4:
      out = "<s>"
      tag_opened = True
    for f in range(value):
      counter += 1
      if counter % 5 == 0:
        out += "</s> "
        if value - counter > 4:
          out += "<s>"
      else:
        out += "|"
    if tag_opened:
      out += "</s>"
    out += " (%d)" % value
    return Markup(out)

  @app.route('/change/<int:userid>')
  def change(userid):
    itemid = request.args.get('itemid')
    curuser = User.query.get(userid)
    curitem = Item.query.get(itemid)
    user_purchase = History(curuser, curitem, curitem.price)
    db.session.add(user_purchase)
    db.session.commit()
    send_email(curuser, curitem)
    return redirect(url_for('user_page', userid=userid))

  @app.route('/change_image', methods=(['POST']))
  def change_image():
    with app.app_context():
      if 'image' in request.files:
        file = request.files['image']
        if file.filename != '' and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          full_path = os.path.join(app.config['IMAGE_FOLDER'], filename)
          file.save(full_path)
          userid = request.form["userid"]
          current_user = User.query.get(userid)
          current_user.imageName = filename
          db.session.commit()
    return redirect(url_for('initial'))