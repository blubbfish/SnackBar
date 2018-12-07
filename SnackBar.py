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

# Set up the command-line options


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


##def allowed_file(filename):
##    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
##    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


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


from Snackbar import app
from Snackbar.Helper import setup_schedule, database_exist, set_default_settings, build_sample_db, stop_schedule
from Snackbar.Adminpannel import setup_admin
from Snackbar.Frontpage import setup_frontpage
from flaskrun import flaskrun, load_options

options = load_options()

if __name__ == "__main__":
  setup_schedule()
  if database_exist() is False:
    build_sample_db()
  set_default_settings()
  setup_admin(app)
  setup_frontpage()

  # app.run()
  # app.run(host='0.0.0.0', port=5000, debug=False)
  flaskrun(app, options=options)
  stop_schedule()
