from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Regestering the auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/')
