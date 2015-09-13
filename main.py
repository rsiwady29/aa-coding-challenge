from flask import Flask,request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def get(self):
        return {'test':'Hello World!'}
    def post(self):
        return eval(request.data)['secret']

api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(debug = True)
