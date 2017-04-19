from flask import Flask, abort, request
import json

from users_commands import get_all_users, add_user, remove_user, user_data, recently_logged, user_commands

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/users',methods=['POST'])
def create_user():
  content = request.get_json(silent=True)
  username = content['username']
  password = content['password']
  if not username or not password:
    return "empty username or password", 400
  if username in get_all_users():
    return "user already exist", 400
  if add_user(username,password):
    return "user created", 201
  else:
    return "error while creating user", 400

@app.route(api_url+'/users',methods=['GET'])
def read_user():
  list = {}
  list["users"] = get_all_users()
  return json.dumps(list), 200

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  return "not found", 404

@app.route(api_url+'/users',methods=['DELETE'])
def delete_user():
  error = False
  for username in get_all_users():
    if not remove_user(username):
        error = True

  if error:
    return 'some users were not deleted', 400
  else:
    return 'all users were deleted', 200

@app.route(api_url+'/users/<string:username>',methods=['GET'])
def read_one_user(username):
  if user_data(username) == False:
    return 'the user does not exist', 400
  else:
    linea=user_data(username)
    
    return json.dumps(linea), 200
 
@app.route(api_url+'/users/<string:username>', methods =['POST'])
def post_user():
 return "not found",404

@app.route(api_url+'/users/<string:username>', methods =['PUT'])
def put_user():
 return "not found",404


@app.route(api_url+'/users/<string:username>',methods=['DELETE'])
def delete_username(username):
 if user_data(username)== False:
  return 'the user does not exist',400
 else:
  remove_user(username);
  return 'the user was deleted',200



@app.route(api_url+'/users/recently_logged', methods =['GET'])
def read_user_filter():
 list = {}
 list =recently_logged()
 list.remove("Nombre")

 if list:
  return json.dumps (list),200 
 else:
  return 'no recently logged users',400 
 
@app.route(api_url+'/users/recently_logged', methods =['POST'])
def post_recently():
 return "not found",404

@app.route(api_url+'/users/recently_logged', methods =['PUT'])
def put_recently():
 return "not found",404

@app.route(api_url+'/users/recently_logged', methods =['DELETE'])
def delete_recently():
 return "not found",404

@app.route(api_url+'/users/<string:username>/commands', methods =['GET'])
def get_commands(username):


 if user_data(username)== False:
  return 'the user does not exist',400
 else:
  list = {}
  list =user_commands(username);
  return json.dumps (list),200 
 
@app.route(api_url+'/users/<string:username>/commands', methods =['POST'])
def post_commands():
 return "not found",404

@app.route(api_url+'/users/<string:username>/commands', methods =['PUT'])
def put_commands():
 return "not found",404

@app.route(api_url+'/users/<string:username>/commands', methods =['DELETE'])
def delete_commands():
 return "not found",404



if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080,debug='True')
