# coding: utf-8
# from Inpayment import Inpayment
##import math
##import os
##from datetime import datetime
##from hashlib import md5
##from math import sqrt

##import flask_login as loginflask
##import tablib
##from flask import Flask, redirect, url_for, render_template, request, send_from_directory, current_app, safe_join, flash, Response
##from flask_admin import Admin, expose, helpers, AdminIndexView, BaseView
##from flask_admin.base import MenuLink
##from flask_admin.contrib.sqla import ModelView
##from flask_admin.form.upload import FileUploadField
##from jinja2 import Markup

##from sqlalchemy import *
##from sqlalchemy.sql import func
# noinspection PyPackageRequirements
##from werkzeug.utils import secure_filename
# noinspection PyPackageRequirements
##from wtforms import form, fields, validators
##import requests
##from sendEmail import Bimail
# import code for encoding urls and generating md5 hashes
##import urllib, hashlib
##import optparse

##from Snackbar.Models import *
##from Snackbar.Admin import admin

##if not os.path.exists(app.config['IMAGE_FOLDER']):
##    os.makedirs(app.config['IMAGE_FOLDER'])


# Set up the command-line options





##@app.template_filter("itemstrikes")
##def itemstrikes(value):
##    counter = 0
##    tag_opened = False
##    out = ""
##    if value > 4:
##        out = "<s>"
##        tag_opened = True
##    for f in range(value):
##        counter += 1
##        if counter % 5 == 0:
##            out += "</s> "
##            if value - counter > 4:
##                out += "<s>"
##        else:
##            out += "|"
##    if tag_opened:
##        out += "</s>"
##    out += " (%d)" % value
##    return Markup(out)


### noinspection PyUnusedLocal
##class RegistrationForm(form.Form):
##    login = fields.StringField(validators=[validators.required()])
##    email = fields.StringField()
##    password = fields.PasswordField(validators=[validators.required()])

##    def validate_login(self, field):
##        if db.session.query(Coffeeadmin).filter_by(name=self.login.data).count() > 0:
##            raise validators.ValidationError('Duplicate username')








##def get_users():
##    get_users_with_leaders(false)


##def get_users_with_leaders(with_leader):
##    initusers = list()
##    all_items = Item.query.filter(Item.icon is not None, Item.icon != '', Item.icon != ' ')
##    all_items_id = [int(instance.itemid) for instance in all_items]
##    if len(all_items_id) > 0:
##        itemid = all_items_id[0]
##    else:
##        itemid = ''

##    for instance in User.query.filter(User.hidden.is_(False)):
##        initusers.append({'firstName': u'{}'.format(instance.firstName),
##                              'lastName': u'{}'.format(instance.lastName),
##                              'imageName': '{}'.format(instance.imageName),
##                              'id': '{}'.format(instance.userid),
##                              'bgcolor': '{}'.format(button_background(instance.firstName + ' ' + instance.lastName)),
##                              'fontcolor': '{}'.format(button_font_color(instance.firstName + ' ' + instance.lastName)),
##                              'coffeeMonth': get_unpaid(instance.userid, itemid),
##                              'leader': get_leader_data(instance.userid, not with_leader),
##                               'email': '{}'.format(instance.email),
##                              })
##    return initusers


##def get_leader_data(userid, skip):
##    leader_info = list()
##    if not skip:
##        all_items = Item.query.filter(Item.icon is not None, Item.icon != '', Item.icon != ' ')
##        i = 0
##        for aItem in all_items:
##            leader_id = int(get_leader(aItem.itemid))
##            if leader_id == userid:
##                item_id = int(aItem.itemid)
##                icon_file = str(aItem.icon)
##                position = (-7 + (i * 34))
##                leader_info.append({"item_id": item_id, "icon": icon_file, "position": position})
##                i = i + 1
##    return leader_info


##def get_leader(itemid):
##    tmp_query = db.session.query(User.userid, func.count(History.price))
##    tmp_query = tmp_query.outerjoin(History, and_(User.userid == History.userid, History.itemid == itemid,
##                                extract('month', History.date) == datetime.now().month,
##                                extract('year', History.date) == datetime.now().year))
##    tmp_query = tmp_query.group_by(User.userid)
##    tmp_query = tmp_query.order_by(func.count(History.price).desc()).first()

##    if tmp_query[1] != 0:
##        return tmp_query[0]
##    else:
##        return -1

##def get_rank(userid, itemid):
##    tmp_query = db.session.query(User.userid, func.count(History.price)). \
##        outerjoin(History, and_(User.userid == History.userid, History.itemid == itemid,
##                                extract('month', History.date) == datetime.now().month,
##                                extract('year', History.date) == datetime.now().year)). \
##        group_by(User.userid). \
##        order_by(func.count(History.price).desc()).all()

##    user_id = [x[0] for x in tmp_query]
##    item_sum = [x[1] for x in tmp_query]

##    idx = user_id.index(userid)
##    rank = idx + 1

##    if rank == len(user_id):
##        upperbound = item_sum[idx - 1] - item_sum[idx] + 1
##        lowerbound = None

##    elif rank == 1:
##        upperbound = None
##        lowerbound = item_sum[idx] - item_sum[idx + 1] + 1

##    else:
##        upperbound = item_sum[idx - 1] - item_sum[idx] + 1
##        lowerbound = item_sum[idx] - item_sum[idx + 1] + 1

##    return {'rank': rank,
##            'upperbound': upperbound,
##            'lowerbound': lowerbound}





##def get_total(userid, itemid):
##    n_unpaid = db.session.query(History). \
##        filter(History.userid == userid). \
##        filter(History.itemid == itemid).count()

##    if n_unpaid is None:
##        n_unpaid = 0

##    return n_unpaid











##def button_background(user):
##    """
##        returns the background color based on the username md5
##    """
##    hash_string = md5(user.encode('utf-8')).hexdigest()
##    hash_values = (hash_string[:8], hash_string[8:16], hash_string[16:24])
##    background = tuple(int(value, 16) % 256 for value in hash_values)
##    return '#%02x%02x%02x' % background


##def button_font_color(user):
##    """
##        returns black or white according to the brightness
##    """
##    r_coef = 0.241
##    g_coef = 0.691
##    b_coef = 0.068
##    hash_string = md5(user.encode('utf-8')).hexdigest()
##    hash_values = (hash_string[:8], hash_string[8:16], hash_string[16:24])
##    bg = tuple(int(value, 16) % 256 for value in hash_values)
##    b = sqrt(r_coef * bg[0] ** 2 + g_coef * bg[1] ** 2 + b_coef * bg[2] ** 2)
##    if b > 130:
##        return '#%02x%02x%02x' % (0, 0, 0)
##    else:
##        return '#%02x%02x%02x' % (255, 255, 255)














##init_login()


##current_sorting = ""


##@app.route('/')
##def initial():
##    global current_sorting
##    initusers = get_users_with_leaders(True)

##    if current_sorting == "az":
##        users = sorted(initusers, key=lambda k: k['firstName'])
##    elif current_sorting == "za":
##        users = sorted(initusers, key=lambda k: k['firstName'])
##        users.reverse()
##    elif current_sorting == "coffee19":
##        users = sorted(initusers, key=lambda k: k['coffeeMonth'])
##    elif current_sorting == "coffee91":
##        users = sorted(initusers, key=lambda k: k['coffeeMonth'])
##        users.reverse()
##    else:
##        current_sorting = "az"
##        users = sorted(initusers, key=lambda k: k['firstName'])

##    return render_template('index.html', users=users, current_sorting=current_sorting)


##@app.route('/sort/<sorting>')
##def sort(sorting):
##    global current_sorting
##    current_sorting = sorting
##    return redirect(url_for('initial'))


##@app.route('/adduser', methods=('GET', 'POST'))
##def adduser():
##    if request.method == 'POST':
##        first_name_error = False
##        first_name = ''
##        if request.form['firstname'] is None or request.form['firstname'] == '':
##            first_name_error = true
##        else:
##            first_name = request.form['firstname']

##        last_name_error = False
##        last_name = ''
##        if request.form['lastname'] is None or request.form['lastname'] == '':
##            last_name_error = true
##        else:
##            last_name = request.form['lastname']

##        from email.utils import parseaddr
##        email_error = False
##        email = ''
##        if request.form['email'] is None or request.form['email'] == '':
##            email_error = true
##        else:
##            email = parseaddr(request.form['email'])[1]
##            if email == '':
##                email_error = true

##        if not first_name_error and not last_name_error and not email_error:
##            with app.app_context():
##                filename = ''
##                if 'image' in request.files:
##                    file = request.files['image']
##                    if file.filename != '' and allowed_file(file.filename):
##                        filename = secure_filename(file.filename)
##                        full_path = os.path.join(app.config['IMAGE_FOLDER'], filename)
##                        file.save(full_path)

##                new_user = User(firstname=first_name, lastname=last_name, email=email, imagename=filename)

##                db.session.add(new_user)
##                db.session.commit()
##                send_email_new_user(new_user)

##                return redirect(url_for('initial'))
##        else:
##            return render_template('adduser.html', firstNameError=first_name_error, firstName=first_name,
##                                   lastNameError=last_name_error, lastName=last_name,
##                                   emailError=email_error, email=email)
##    else:
##        return render_template('adduser.html', firstNameError=False, firstName='', lastNameError=False, lastName='',
##                               emailError=False, email='')


##def allowed_file(filename):
##    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
##    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


##@app.route('/image/')
##def default_image():
##    userID = request.args.get('userID')
##    return monster_image(None, userID)


##@app.route('/image/<filename>')
##def image(filename):
##    userID = request.args.get('userID')
##    return monster_image(filename, userID)


##@app.route('/icon/')
##def default_icon():
##    return get_icon(None)


##@app.route('/icon/<icon>')
##def get_icon(icon):
##    return image_from_folder(icon, app.config['ICON_FOLDER'], "static/unknown_icon.svg")


##def monster_image(filename, userID):
##    if filename is None:
##        return monster_image_for_id(userID)

##    fullpath = os.path.join(current_app.root_path, app.config['IMAGE_FOLDER'])

##    full_file_path = safe_join(fullpath, filename)
##    if not os.path.isabs(full_file_path):
##        full_file_path = os.path.join(current_app.root_path, full_file_path)
##    try:
##        if not os.path.isfile(full_file_path):
##            return  monster_image_for_id(userID)
##    except (TypeError, ValueError):
##        pass

##    return send_from_directory(directory=fullpath, filename=filename, as_attachment=False)



##def monster_image_for_id(userID):
##    if userID is None:
##        userID = "example@example.org"

##    use_gravatar = True
##    returnValue = send_from_directory(directory=current_app.root_path, filename="static/unknown_image.png",
##                                      as_attachment=False)

##    # mail_parts = userID.split("@")
##    # if len(mail_parts) == 2:
##    #     prefix = mail_parts[0]
##    #     domain = mail_parts[1]
##    #     if domain == "fit.fraunhofer.de":
##    #         use_gravatar = False
##    #         requestURL = "https://chat.fit.fraunhofer.de/avatar/" + prefix
##    #         try:
##    #             proxyResponse = requests.get(requestURL, timeout=5)
##    #
##    #             returnValue = Response(proxyResponse)
##    #         except:
##    #             pass

##    if use_gravatar:
##        userHash = hashlib.md5(str(userID).encode('utf-8').lower()).hexdigest()
##        requestURL = "https://www.gravatar.com/avatar/" + userHash + "?s=100" + "&d=monsterid"
##        try:
##            proxyResponse = requests.get(requestURL, timeout=5)
##            returnValue = Response(proxyResponse)
##        except:
##            pass
##    return returnValue


##def image_from_folder(filename, image_folder, the_default_image):
##    if filename is None:
##        return send_from_directory(directory=current_app.root_path, filename=the_default_image, as_attachment=False)

##    fullpath = os.path.join(current_app.root_path, image_folder)

##    full_file_path = safe_join(fullpath, filename)
##    if not os.path.isabs(full_file_path):
##        full_file_path = os.path.join(current_app.root_path, full_file_path)
##    try:
##        if not os.path.isfile(full_file_path):
##            return send_from_directory(directory=current_app.root_path, filename=the_default_image, as_attachment=False)
##    except (TypeError, ValueError):
##        pass

##    return send_from_directory(directory=fullpath, filename=filename, as_attachment=False)
##    # return redirect(url)


### from https://gist.github.com/deontologician/3503910
##def reltime(date, compare_to=None, at='@'):
##    """Takes a datetime and returns a relative representation of the
##    time.
##    :param date: The date to render relatively
##    :param compare_to: what to compare the date to. Defaults to datetime.now()
##    :param at: date/time separator. defaults to "@". "at" is also reasonable.
##    """

##    def ordinal(n):
##        r"""Returns a string ordinal representation of a number
##        Taken from: http://stackoverflow.com/a/739301/180718
##        """
##        if 10 <= n % 100 < 20:
##            return str(n) + 'th'
##        else:
##            return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, "th")

##    compare_to = compare_to or datetime.now()
##    if date > compare_to:
##        return NotImplementedError('reltime only handles dates in the past')
##    # get timediff values
##    diff = compare_to - date
##    if diff.seconds < 60 * 60 * 8:  # less than a business day?
##        days_ago = diff.days
##    else:
##        days_ago = diff.days + 1
##    months_ago = compare_to.month - date.month
##    years_ago = compare_to.year - date.year
##    weeks_ago = int(math.ceil(days_ago / 7.0))
##    # get a non-zero padded 24-hour hour
##    hr = date.strftime('%H')
##    if hr.startswith('0'):
##        hr = hr[1:]
##    wd = compare_to.weekday()
##    # calculate the time string
##    _time = '{0}:{1}'.format(hr, date.strftime('%M').lower())

##    # calculate the date string
##    if days_ago == 0:
##        datestr = 'today {at} {time}'
##    elif days_ago == 1:
##        datestr = 'yesterday {at} {time}'
##    elif (wd in (5, 6) and days_ago in (wd + 1, wd + 2)) or \
##            wd + 3 <= days_ago <= wd + 8:
##        # this was determined by making a table of wd versus days_ago and
##        # divining a relationship based on everyday speech. This is somewhat
##        # subjective I guess!
##        datestr = 'last {weekday} {at} {time} ({days_ago} days ago)'
##    elif days_ago <= wd + 2:
##        datestr = '{weekday} {at} {time} ({days_ago} days ago)'
##    elif years_ago == 1:
##        datestr = '{month} {day}, {year} {at} {time} (last year)'
##    elif years_ago > 1:
##        datestr = '{month} {day}, {year} {at} {time} ({years_ago} years ago)'
##    elif months_ago == 1:
##        datestr = '{month} {day} {at} {time} (last month)'
##    elif months_ago > 1:
##        datestr = '{month} {day} {at} {time} ({months_ago} months ago)'
##    else:
##        # not last week, but not last month either
##        datestr = '{month} {day} {at} {time} ({days_ago} days ago)'
##    return datestr.format(time=_time,
##                          weekday=date.strftime('%A'),
##                          day=ordinal(date.day),
##                          days=diff.days,
##                          days_ago=days_ago,
##                          month=date.strftime('%B'),
##                          years_ago=years_ago,
##                          months_ago=months_ago,
##                          weeks_ago=weeks_ago,
##                          year=date.year,
##                          at=at)


##@app.route('/user/<int:userid>', methods=['GET'])
##def user_page(userid):
##    user_name = u'{} {}'.format(User.query.get(userid).firstName, User.query.get(userid).lastName)
##    items = list()

##    for instance in Item.query:
##        rank_info = get_rank(userid, instance.itemid)
##        items.append({'name': u'{}'.format(instance.name),
##                      'price': instance.price,
##                      'itemid': '{}'.format(instance.itemid),
##                      'icon': '{}'.format(instance.icon),
##                      'count': get_unpaid(userid, instance.itemid),
##                      'total': get_total(userid, instance.itemid),
##                      'rank': rank_info['rank'],
##                      'ub': rank_info['upperbound'],
##                      'lb': rank_info['lowerbound']})

##    no_users = User.query.filter(User.hidden.is_(False)).count()
##    currbill = rest_bill(userid)
##    can_change_image = settings_for('usersCanChangeImage')

##    last_purchase = "-"
##    last_purchase_item = History.query.filter(History.userid == userid).order_by(History.date.desc()).first()
##    if last_purchase_item is not None:
##        # last_purchase = last_purchase_item.date.strftime('%Y-%m-%d %H:%M')
##        last_purchase = reltime(last_purchase_item.date)

##    return render_template('choices.html',
##                           currbill=currbill,
##                           chosenuser=user_name,
##                           userid=userid,
##                           items=items,
##                           noOfUsers=no_users,
##                           canChangeImage=can_change_image,
##                           last_purchase=last_purchase
##                           )


##def send_email_new_user(curuser):
##    if curuser.email:
##        mymail = Bimail('SnackBar User Created', ['{}'.format(curuser.email)])
##        mymail.sendername = settings_for('mailSender')
##        mymail.sender = settings_for('mailSender')
##        mymail.servername = settings_for('mailServer')
##        # start html body. Here we add a greeting.
##        mymail.htmladd(
##            'Hallo {} {},<br><br>ein neuer Benutzer wurde mit dieser E-Mail Adresse erstellt. Solltest du diesen '
##            'Acocunt nicht erstellt habe, melde dich bitte bei {}.<br><br>Ciao,<br>SnackBar Team [{}]'
##            '<br><br><br><br>---------<br><br><br><br>'
##            'Hello {} {},<br><br>a new User has been created with this mail address. If you have not created this '
##            'Acocunt, please contact {}.<br><br>Ciao,<br>SnackBar Team [{}]'.format(
##                curuser.firstName, curuser.lastName, settings_for('snackAdmin'), settings_for('snackAdmin'),
##                curuser.firstName,
##                curuser.lastName, settings_for('snackAdmin'), settings_for('snackAdmin')))
##        # Further things added to body are separated by a paragraph, so you do not need to worry about
##        # newlines for new sentences here we add a line of text and an html table previously stored
##        # in the variable
##        # add image chart title
##        # attach another file
##        # mymail.htmladd('Ciao,<br>SnackBar Team [Clemens Putschli (C5-315)]')
##        # mymail.addattach([os.path.join(fullpath, filename)])
##        # send!
##        # print(mymail.htmlbody)
##        mymail.send()





##def send_email(curuser, curitem):
##    if curuser.email:
##        if settings_for('instantMail') == 'true':
##            currbill = '{0:.2f}'.format(rest_bill(curuser.userid))
##            # print(instance.firstName)
##            # print(currbill)
##            mymail = Bimail(u'SnackBar++ ({} {})'.format(curuser.firstName, curuser.lastName), ['{}'.format(curuser.email)])
##            mymail.sendername = settings_for('mailSender')
##            mymail.sender = settings_for('mailSender')
##            mymail.servername = settings_for('mailServer')
##            # start html body. Here we add a greeting.

##            today = datetime.now().strftime('%Y-%m-%d %H:%M')
##            mymail.htmladd(
##                u'Hallo {} {}, <br>SnackBar hat gerade "{}" ({} €) für dich GEBUCHT! '
##				u'<br><br> Dein Guthaben beträgt jetzt {} € <br><br>'.format(
##                    curuser.firstName, curuser.lastName, curitem.name, curitem.price, currbill))
##            mymail.htmladd('Ciao,<br>SnackBar Team [{}]'.format(settings_for('snackAdmin')))
##            mymail.htmladd('<br><br>---------<br><br>')
##            mymail.htmladd(
##                u'Hello {} {}, <br>SnackBar has just ORDERED {} ({} €) for you! '
##                u'<br><br> Your balance is now {} € <br><br> '.format(
##                    curuser.firstName, curuser.lastName, curitem.name, curitem.price, currbill))
##            # Further things added to body are separated by a paragraph, so you do not need to worry
##            # about newlines for new sentences here we add a line of text and an html table previously
##            # stored in the variable
##            # add image chart title
##            # attach another file
##            mymail.htmladd('Ciao,<br>SnackBar Team [{}]'.format(settings_for('snackAdmin')))

##            mymail.htmladd('<br><br>---------<br>Registered at: {}'.format(today))

##            # mymail.addattach([os.path.join(fullpath, filename)])
##            # send!
##            # print(mymail.htmlbody)
##            mymail.send()


##@app.route('/change/<int:userid>')
##def change(userid):
##    itemid = request.args.get('itemid')
##    curuser = User.query.get(userid)
##    curitem = Item.query.get(itemid)
##    user_purchase = History(curuser, curitem, curitem.price)

##    db.session.add(user_purchase)
##    db.session.commit()

##    send_email(curuser, curitem)
##    return redirect(url_for('user_page', userid=userid))


##@app.route('/analysis')
##def analysis():
##    from analysisUtils import main
##    content, tags_hours_labels = main()
##    return render_template('analysis.html', content=content, tagsHoursLabels=tags_hours_labels)

##@app.route('/analysis/slide')
##def analysis_slide():
##    from analysisUtils import main
##    content, tags_hours_labels = main()
##    return render_template('analysisSlide.html', content=content, tagsHoursLabels=tags_hours_labels)


##@app.route('/change_image', methods=(['POST']))
##def change_image():
##    with app.app_context():
##        if 'image' in request.files:
##            file = request.files['image']
##            if file.filename != '' and allowed_file(file.filename):
##                filename = secure_filename(file.filename)
##                full_path = os.path.join(app.config['IMAGE_FOLDER'], filename)
##                file.save(full_path)

##                userid = request.form["userid"]
##                current_user = User.query.get(userid)
##                current_user.imageName = filename

##                db.session.commit()

##    return redirect(url_for('initial'))






from Snackbar import app
from Snackbar.Helper import setup_schedule, database_exist, set_default_settings, build_sample_db, stop_schedule
from Snackbar.Adminpannel import setup_admin
from flaskrun import flaskrun, load_options

options = load_options()

if __name__ == "__main__":
  setup_schedule()
  if database_exist() is False:
    build_sample_db()
  set_default_settings()
  setup_admin(app)

  # app.run()
  # app.run(host='0.0.0.0', port=5000, debug=False)
  flaskrun(app, options=options)
  stop_schedule()
