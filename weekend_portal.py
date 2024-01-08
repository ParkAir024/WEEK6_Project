from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

users = {
    '1': {
        'username': 'goku',
        'email' : 'goku@capsule.com'
    },
    '2' : {
        'username' : 'tanjiroK',
        'email' : 'ktanjiro@corp.com'
    },
    '3' : {
        'username' : 'allmightjr',
        'email' : 'deku@ua.com'
    }
}

animes = {
    '1' : {
        'title' : 'My Hero Acadamia',
        'user_id' : '3'
    },
    '2' : {
        'title' : 'DragonBall Z',
        'user_id' : '1'
    },
    '3' : {
        'title' : 'Demon Slayer',
        'user_id' : '2'
    }
}

#user routes

@app.get('/user')
def user():
    return {'users': list(users.values())}, 200

@app.route('/user', methods=["POST"])
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return{'message': f'{json_body["username"]} created'}, 201

@app.put('/user')
def update_user():
    return

@app.delete('/user')
def delete_user():
    pass

#anime routes

@app.get('/anime')
def get_posts():
    return

@app.post('/anime')
def create_post():
    return

@app.put('/anime')
def update_post():
    return

@app.delete('/anime')
def delete_post():
    pass

