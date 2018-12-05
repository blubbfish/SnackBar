# coding=utf-8

from Snackbar.Helper.Billing import rest_bill
from Snackbar.Helper.Database import settings_for
from Snackbar.Helper.Bimail import Bimail

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
            mymail.htmladd('Hallo {} {},<br>'
              '<br>'
              'du hast nur noch wenig Geld auf deinem SnackBar Konto ({} €). Zahle bitte ein bisschen Geld ein, damit wir wieder neue Snacks kaufen können!<br>'
              '<br>'
              'Ciao,<br>'
              'SnackBar Team [{}]<br>'
              '<br>'
              '<br>'
              '<br>'
              '---------<br>'
              '<br>'
              '<br>'
              '<br>'
              'Hello {} {},<br>'
              '<br>'
              'your SnackBar balance is very low ({} €). Please top it up with some money!<br>'
              '<br>'
              'Ciao,<br>'
              'SnackBar Team [{}]'.format(curuser.firstName, curuser.lastName, currbill, settings_for('snackAdmin'), curuser.firstName, curuser.lastName, currbill, settings_for('snackAdmin')))
            mymail.send()
