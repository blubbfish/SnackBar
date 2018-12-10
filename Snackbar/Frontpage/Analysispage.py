from Snackbar import app
from flask import render_template
from Snackbar.Helper.Analysis import create_analysis

class Analysispage():
  @app.route('/analysis')
  def analysis():
    content, tags_hours_labels = create_analysis()
    return render_template('analysis.html', content=content, tagsHoursLabels=tags_hours_labels)

  @app.route('/analysis/slide')
  def analysis_slide():
      content, tags_hours_labels = create_analysis()
      return render_template('analysisSlide.html', content=content, tagsHoursLabels=tags_hours_labels)
