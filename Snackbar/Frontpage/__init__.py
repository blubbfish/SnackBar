from Snackbar.Frontpage.Titlepage import Titlepage
from Snackbar.Frontpage.Analysispage import Analysispage
from Snackbar.Frontpage.Userpage import Userpage
from Snackbar import app
from os import path, makedirs

def setup_frontpage():
  if not path.exists("Snackbar/"+app.config['IMAGE_FOLDER']):
    makedirs("Snackbar/"+app.config['IMAGE_FOLDER'])
  Titlepage()
  Userpage()
  Analysispage()