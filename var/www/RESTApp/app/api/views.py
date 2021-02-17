from flask import Flask
from flask_restful import  Api, Resource, reqparse

# new request parser object, automatically parse the request is being sent and make sure that it fits the
# kind of guidelines and has the correct information in it 
video_put_args = reqparse.RequestParser()

video_put_args.add_argument("name", type = str, help = "Name of the video", required = True)
video_put_args.add_argument("views", type = int, help = "Views of the video", required = True)
video_put_args.add_argument("likes", type = int, help = "Likes on the video", required = True)

videos = {}


# HelloWorld class is inherited from Resource
class Video(Resource):

    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id]

