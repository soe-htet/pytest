from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.user import UserRegister
from security import authenticate,identity
from resources.store import StoreList,Store

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "soe"
api = Api(app)
jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister,'/register')
api.add_resource(ItemList,'/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList,'/stores')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5001)

