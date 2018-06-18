# class User(object):
#     def __init__(self, _id, username, password):
#         self.id = _id
#         self.username = username
#         self.password = password
#

from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import Resource

class User(Resource):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @jwt_required()
    def get(self): # view all users
        user = current_identity
        # then implement admin auth method
        # ...
