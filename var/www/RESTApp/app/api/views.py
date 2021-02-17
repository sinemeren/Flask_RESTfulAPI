from flask import Flask
from flask_restful import  Api, Resource, reqparse, abort

# new request parser object, automatically parse the request is being sent and make sure that it fits the
# kind of guidelines and has the correct information in it 
video_put_args = reqparse.RequestParser()

video_put_args.add_argument("name", type = str, help = "Name of the video", required = True)
video_put_args.add_argument("views", type = int, help = "Views of the video", required = True)
video_put_args.add_argument("likes", type = int, help = "Likes on the video", required = True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message = "Could not find video...")

def abort_if_video_id_exists(video_id):
    if video_id in videos:
        abort(404, message = "video already exist with that id...")

# HelloWorld class is inherited from Resource
class Video(Resource):

    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_id_exists(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return ' ', 204



