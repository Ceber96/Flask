from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    #加载配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

