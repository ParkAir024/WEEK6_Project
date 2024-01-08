from flask import request
from uuid import uuid4


from app import app
from db import animes, users

#anime routes

@app.get('/anime')
def get_posts():
    return { 'animes': list(animes.values()) }

@app.get('/anime/<post_id>')
def get_post(post_id):
  try:
    return {'post': animes[post_id]}, 200
  except KeyError:
    return {'message': "Invalid Post"}, 400

@app.post('/anime')
def create_post():
    post_data = request.get_json()
    user_id = post_data['user_id']
    if user_id in users:
        animes[uuid4()] = post_data
        return {'message': "Anime Added"}, 201
    return { 'message': "Invalid User"}, 404


@app.put('/anime/<post_id>')
def update_post(post_id):
  try:
    post = animes[post_id]
    post_data = request.get_json()
    if post_data['user_id'] == post['user_id']:
      post['body'] = post_data['body']
      return { 'message': 'Post Updated' }, 202
    return {'message': "Unauthorized"}, 401
  except:
    return {'message': "Invalid Post Id"}, 400

@app.delete('/anime/<post_id>')
def delete_post(post_id):
  try:
    del animes[post_id]
    return {"message": "Post Deleted"}, 202
  except:
    return {'message':"Invalid Post"}, 400
