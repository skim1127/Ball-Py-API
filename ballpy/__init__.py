# Config
from flask import Flask
from flask_migrate import Migrate

# Factory
def create_app():
    app = Flask(__name__)

    # Database Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return "This is the Homepage."

    # Register reptile blueprint
    from . import reptile
    app.register_blueprint(reptile.bp)

    return app