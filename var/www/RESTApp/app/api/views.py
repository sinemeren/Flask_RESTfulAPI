from flask import Flask
from flask_restful import  Api, Resource



names = {"tim": {"age": 19, "gender": "male"},
         "bill": {"age": 70, "gender": "male"}}

# HelloWorld class is inherited from Resource
class HelloWorld(Resource):

    def get(self, name):
        return names [name]

