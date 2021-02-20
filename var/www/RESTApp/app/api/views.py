from flask import Flask
from flask_restful import  Api, Resource, reqparse, abort, marshal_with, fields
from app import db, apiInstance, VideoModel

# new request parser object, automatically parse the request is being sent and make sure that it fits the
# kind of guidelines and has the correct information in it 
video_put_args = reqparse.RequestParser()

video_put_args.add_argument("name", type = str, help = "Name of the video", required = True)
video_put_args.add_argument("views", type = int, help = "Views of the video", required = True)
video_put_args.add_argument("likes", type = int, help = "Likes on the video", required = True)


# resource fields is a way how object should be serialised
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# HelloWorld class is inherited from Resource
class Video(Resource):

    # marshal_with: when we return, take this return value and serialise it using resource fields
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id = video_id).first()
        #if not result:
		#    abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id = video_id).first()
        if result:
            abort(409, message = "Video id taken...")

        video = VideoModel(id = video_id, name = args['name'], views = args['views'], likes = args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

  



apiInstance.add_resource(Video, '/video/<int:video_id>')
