from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse

# from flask_jwt import JWT #, jwt_required, current_identity
# from security import authenticate, identity


app = Flask(__name__)
# app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
# app.secret_key = 'lynne'
# app.config['JWT_AUTH_URL_RULE'] = '/login'
# app.config['JWT_AUTH_USERNAME_KEY'] = 'username'
api = Api(app)

# jwt = JWT(app, authenticate, identity)
# jwt = JWT(app, authenticate, identity)  # /auth
# @jwt.auth_response_handler
# def customized_error_handler(error):
#     return jsonify({'message': error.description,'code': error.status_code}), error.status_code

items = []


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, name):
        item = next(filter(lambda x:x['name'] == name, items), None)
        return {'item':item}, 200 if item else 404
        # return {'item':next(filter(lambda x:x['name'] == name, items), None)}

    def post(self, name):
        if next(filter(lambda x:x['name'] == name, items), None) is not None:
            return {'message':"An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = {'name':name, 'price':data['price']}
        # item = {'name':name, 'price':12}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x:x['name'] != name, items))
        return {'message':'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        # data = request.get_json()
        # Once again, print something not in the args to verify everything works
        item = next(filter(lambda x:x['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items':items}


#
#
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# if __name__ == '__main__':
#     app.run(debug=True)  # important to mention debug=True


app.run(port=5000, debug=True)  # important to mention debug=True
