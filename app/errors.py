from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title = 'Page Not Found')

@app.errorhandler(500)
def internal_error(error):
    db.session.roll_back()
    return render_template('500.html', title = 'Internal Error')