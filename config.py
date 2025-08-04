import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql+psycopg2://greenchain_admin:MTvRpQRtD2c5yIpQplT9dDDgXRC6BhYm@dpg-d285uac9c44c73a3sa70-a.frankfurt-postgres.render.com/greenchain_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')

