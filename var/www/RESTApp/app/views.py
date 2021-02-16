from flask import Flask
from flask_restful import  Api, Resource

FlaskAppInstance = Flask(__name__)
apiInstance= Api(FlaskAppInstance)

# HelloWorld class is inherited from Resource
class HelloWorld(Resource):
    def get(self):
        return {"name": "Hello World"}


apiInstance.add_resource(HelloWorld, "/helloworld")    

if __name__ == '__main__':
    FlaskAppInstance.run(debug=True, host='0.0.0.0')