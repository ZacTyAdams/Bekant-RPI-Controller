# flask api for desk control and monitoring

import json
from turtle import up
from urllib import response
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import sys

app = Flask(__name__)

api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):
  
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
  
        return jsonify({'message': 'hello world'})
  
    # Corresponds to POST request
    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'data': data})
  
  
# another resource to calculate the square of a number
class Square(Resource):
  
    def get(self, num):
  
        return jsonify({'square': num**2})

class Desk(Resource):
    
    def get(self):
        print(request)
        if sys.platform != 'linux':
            response = jsonify({'height':'MacOS: 50'})
            response.status_code = 200
            return response
        else:
            response = jsonify({'height': 'Linux: 50'})
            response.status_code = 200
            return response
    
    def post(self):
        data = request.get_json()
        print(data['function'])
        if sys.platform != 'linux':
            resp = jsonify({'message': str('MacOS: desk going ' + data['function'])})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message': str('Linux: desk going ' + data['function'])})
            resp.status_code = 201
            return resp

        # print("received post request")
        # print(request)
        # print(request.get_data())
        # return 201
        
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Desk, '/desk')
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True, host='0.0.0.0', port='5001')