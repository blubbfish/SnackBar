from Snackbar import app
from flask import render_template

class Analysispage():
  @app.route('/analysis')
  def analysis():
    from analysisUtils import main
    content, tags_hours_labels = main()
    return render_template('analysis.html', content=content, tagsHoursLabels=tags_hours_labels)

  @app.route('/analysis/slide')
  def analysis_slide():
      from analysisUtils import main
      content, tags_hours_labels = main()
      return render_template('analysisSlide.html', content=content, tagsHoursLabels=tags_hours_labels)
