from flask import Flask, render_template
from flask_restful import Api

FlaskAppInstance = Flask(__name__)

from app.api.views import Video

apiInstance= Api(FlaskAppInstance)
apiInstance.add_resource(Video, '/video/<int:video_id>')