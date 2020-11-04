import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=1
    MAIL_USERNAME='norulesanymore@gmail.com'
    MAIL_PASSWORD='n$P@-a!eP=2gB&T+'
    ADMINS=['tastebolder@gmail.com']
    
    START_NGROK=os.environ.get('START_NGROK') is not None and os.environ.get('WERKZEUG_RUN_MAIN') is not 'true'

    # reCAPTCHA configuration
    RECAPTCHA_PUBLIC_KEY='6LfyL9oZAAAAAB3EFZQYBx3ivtgu00zQmOEqH4OQ'
    RECAPTCHA_PRIVATE_KEY='6LfyL9oZAAAAAOfYBlOGCDt-MLYIvLBcFehW12d_'

    # Heroku logs
    LOG_TO_STDOUT=os.environ.get('LOG_TO_STDOUT')