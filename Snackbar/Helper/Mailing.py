# coding=utf-8

from Snackbar.Helper.Billing import rest_bill
from Snackbar.Helper.Database import settings_for
from Snackbar.Helper.Bimail import Bimail
from datetime import datetime


def send_reminder(curuser):
  if curuser.email:
    curn_bill_float = rest_bill(curuser.userid)
    minimum_balance = float(settings_for('minimumBalance'))
    if curn_bill_float <= minimum_balance:
      currbill = '{0:.2f}'.format(rest_bill(curuser.userid))
      mymail = Bimail('SnackBar Reminder', ['{}'.format(curuser.email)])
      mymail.sendername = settings_for('mailSender')
      mymail.sender = settings_for('mailSender')
      mymail.servername = settings_for('mailServer')
      mymail.htmladd(u'Hallo {} {},<br>du hast nur noch wenig Geld auf deinem SnackBar Konto ({} €). Zahle bitte ein bisschen Geld ein, damit wir wieder neue Snacks kaufen können!'.format(curuser.firstName, curuser.lastName, currbill))
      mymail.htmladd(u'Ciao,<br>SnackBar Team [{}]'.format(settings_for('snackAdmin')))
      mymail.htmladd('---------')
      mymail.htmladd(u'Hello {} {},<br>your SnackBar balance is very low ({} €). Please top it up with some money!'.format(curuser.firstName, curuser.lastName, currbill))
      mymail.htmladd(u'Ciao,<br>SnackBar Team [{}]'.format(settings_for('snackAdmin')))
      mymail.send()


def send_email_new_user(curuser):
  if curuser.email:
    mymail = Bimail('SnackBar User Created', ['{}'.format(curuser.email)])
    mymail.sendername = settings_for('mailSender')
    mymail.sender = settings_for('mailSender')
    mymail.servername = settings_for('mailServer')
    mymail.htmladd(u'Hallo {} {},<br>ein neuer Benutzer wurde mit dieser E-Mail Adresse erstellt. Solltest du diesen Acocunt nicht erstellt habe, melde dich bitte bei {}.'.format(curuser.firstName, curuser.lastName, settings_for('snackAdmin')))
    mymail.htmladd(u'Ciao,<br>SnackBar Team [{}]'.format(settings_for('snackAdmin')))
    mymail.htmladd('---------')
    mymail.htmladd(u'Hello {} {},<br>a new User has been created with this mail address. If you have not created this Acocunt, please contact {}.'.format(curuser.firstName, curuser.lastName, settings_for('snackAdmin')))
    mymail.htmladd(u'Ciao,<br>SnackBar Team [{}]'.format(settings_for('snackAdmin')))
    mymail.send()


def send_email(curuser, curitem):
  if curuser.email:
    if settings_for('instantMail') == 'true':
      currbill = '{0:.2f}'.format(rest_bill(curuser.userid))
      mymail = Bimail(u'SnackBar++ ({} {})'.format(curuser.firstName, curuser.lastName), ['{}'.format(curuser.email)])
      mymail.sendername = settings_for('mailSender')
      mymail.sender = settings_for('mailSender')
      mymail.servername = settings_for('mailServer')
      today = datetime.now().strftime('%Y-%m-%d %H:%M')
      mymail.htmladd(u'Hallo {} {}, <br>SnackBar hat gerade "{}" ({0:.2f} €) für dich GEBUCHT!<br>Dein Guthaben beträgt jetzt {} €'.format(curuser.firstName, curuser.lastName, curitem.name, curitem.price, currbill))
      mymail.htmladd(u'Ciao,<br>SnackBar Team [{}]'.format(settings_for('snackAdmin')))
      mymail.htmladd('---------')
      mymail.htmladd(u'Hello {} {}, <br>SnackBar has just ORDERED {} ({0:.2f} €) for you!<br>Your balance is now {} €'.format(curuser.firstName, curuser.lastName, curitem.name, curitem.price, currbill))
      mymail.htmladd(u'Ciao,<br>SnackBar Team [{}]'.format(settings_for('snackAdmin')))
      mymail.htmladd('---------<br>Registered at: {}'.format(today))
      mymail.send()
    else:
      send_reminder(curuser)