from flask import Flask
from flask_restful import  Api, Resource


# HelloWorld class is inherited from Resource
class HelloWorld(Resource):
    def get(self):
        return {"name": "Hello World"}


