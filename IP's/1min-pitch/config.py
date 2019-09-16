import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://hapiness:  @localhost/seconds'
class ProdConfig(Config):
    pass

class DevConfig(COnfig):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
} 