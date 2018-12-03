
# noinspection PyBroadException,PyPep8
def send_reminder_to_all():
  try:
    for aUser in User.query.filter(User.hidden.is_(False)):
      send_reminder(aUser)
  except:
    pass
