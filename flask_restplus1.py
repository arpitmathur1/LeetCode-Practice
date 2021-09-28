from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}, 200, {'Etag': 'some-opaque-string', 'Age':0}

if __name__ == '__main__':
    app.run(debug=True)