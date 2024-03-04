import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'  #figure out using bash file to hide sensitive information.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'   #os.environ.get('SECRET_KEY') /('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'yeyulchoi@gmail.com'  # os.environ.get('EMAIL_USER')
    MAIL_PASSWORD= 'ucta njcl aupg itqa'  # os.environ.get('EMAIL_PASS')