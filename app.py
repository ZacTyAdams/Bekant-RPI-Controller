# flask api for desk control and monitoring

from flask import Flask, request, jsonify
from flask_restful import Resource, Api

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
        return jsonify({'data': data}), 201
  
  
# another resource to calculate the square of a number
class Square(Resource):
  
    def get(self, num):
  
        return jsonify({'square': num**2})

class Desk(Resource):
    
    def get(self):
        return jsonify({'message': 'This is the current desk height'})
    
    def post(self):
        print("received post request")
        print(request)
        print(request.get_data())
        return 201
        
# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Desk, '/desk')
  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)