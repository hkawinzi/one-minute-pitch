from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
#initializing flask extension
    bootstrap.init_app(app)
    db.init_app
