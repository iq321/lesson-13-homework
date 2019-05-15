import pickle
import json
from flask import Flask, request, Response


app = Flask(__name__)


def get_all_users():
    print(request.args)
    pickle_in = open('data.pickle', 'rb')
    data_new = pickle.load(pickle_in)
    js = json.dumps(data_new)
    pickle_in.close()
    return Response(js, status=200, mimetype='application/json')


def create_user():
    try:
        data = json.loads(request.data)
    except Exception as e:
        print(e)
        return
    
    if 'name' not in data or 'age' not in data:
        return Response('{"status": "error", "error": "Bad request"}',
                        status=400,
                        mimetype='application/json')
    pickle_in = open('data.pickle', 'rb')
    data_new = pickle.load(pickle_in)
    data_new['name'] = data['name']
    data_new['age'] = data['age']
    pickle_out = open("data.pickle","wb")
    pickle.dump(data_new, pickle_out)
    pickle_in.close()
    return Response('{"status": "ok"}',
                    status=200,
                    mimetype='application/json')

def update_user():
    data = request.data
    if 'name' not in data or 'age' not in data:
        return Response('{"status": "error", "error": "Bad request"}',
                      status=400,
                      mimetype='application/json')
   
    pickle_in = open('data.pickle', 'rb')
        data_new = pickle.load(pickle_in)
    [{'id': 1, 'name': '123'}, {'id': 1, 'name': '321'}]
    for user in data_new:
        if user['id'] == data['id']:
          user['name'] = data['name']
          user['...'] = data['...']
      
    js = json.dumps(data_new)
    pickle_in.close()
    return Response('{"status": "ok"}',
                    status=200,
                    mimetype='application/json')
    
def delete_user():
    data = request.data
    if 'id' not in data:
        return Response('{"status": "error", "error": "not id found"}',
                        status=400,
                        mimetype='application/json')
    
    data = pickle.load(pickle_in)  
    pickle_in.close()
    del data['id']
    pickle_out = open("data.pickle","wb")
    pickle.dump(data, pickle_out)
    pickle_in.close()
    return Response('{"status": "ok"}',
                    status=200,
                    mimetype='application/json')
    
@app.route('/users/', methods=['GET', 'POST', 'PATCH', 'DELETE'])
@app.route('/users/<id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])    
def users(*args, **kwargs):
    
    if request.method == 'GET':

        return get_all_users()

    elif request.method == 'POST':

        return create_user()

    elif request.method == 'PATCH':

        return update_user()

    elif request.method == 'DELETE':

        return delete_user()

    else:

        pass


if __name__ == '__main__':
    app.run(port=8080)

