from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db
from controllers.tarefa_controller import TarefaController
from routes.tarefas_routes import tarefas_bp

def criar_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    app.register_blueprint(tarefas_bp)
    
    return app

if __name__ == '__main__':
    app = criar_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
