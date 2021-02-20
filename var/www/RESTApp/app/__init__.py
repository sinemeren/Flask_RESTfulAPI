from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

FlaskAppInstance = Flask(__name__)

# database
FlaskAppInstance.config.from_pyfile('config/development.cfg')
db = SQLAlchemy(FlaskAppInstance)
db.create_all()

#from app.api.views import Video

apiInstance= Api(FlaskAppInstance)

