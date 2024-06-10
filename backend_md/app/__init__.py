from flask import Flask, jsonify
from app.extensions import db, cors
#from app.config import Config
from app.routes.users_routes import user_bp
import os

def create_app():
    app = Flask(__name__)
    #app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db.init_app(app)
    cors.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(user_bp, url_prefix='/api/flask')

    # test route
    @app.route('/', methods=["GET"])
    def test():
        return jsonify({'message': 'The server is Running'})

    return app