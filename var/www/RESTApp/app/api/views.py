from flask import Flask
from flask_restful import  Api, Resource


# HelloWorld class is inherited from Resource
class HelloWorld(Resource):
    def get(self):
        return {"name": "Hello World"}




if __name__ == '__main__':
    FlaskAppInstance.run(debug=True, host='0.0.0.0')