import schedule
import threading
from Reminder import send_reminder_to_all
import time


running = True


def setup_schedule():
  schedule.every().monday.at("10:30").do(send_reminder_to_all)
  schedule_thread = threading.Thread(target=run_schedule).start()


def stop_schedule():
  global running
  running = False


def run_schedule():
  global running
  while running is True:
    schedule.run_pending()
    time.sleep(1)