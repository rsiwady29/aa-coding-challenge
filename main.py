from flask import Flask,request
from flask_restful import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def get(self):
        return {'test':'Hello World!'}
    def post(self):
        secret = eval(request.data)['secret']
        print secret
        return secret

api.add_resource(Main, '/')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
