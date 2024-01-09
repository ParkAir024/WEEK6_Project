from flask import request
from uuid import uuid4
from flask.views import MethodView

from schemas import PostSchema
from db import animes, users
from . import bp

# Anime routes

@bp.route('/<anime_id>')
class Post(MethodView):

  @bp.response(200, PostSchema)
  def get(self, anime_id):
    try:
      return animes[anime_id]
    except KeyError:
      return {'message': "Invalid Post"}, 400

  @bp.arguments(PostSchema)
  def put(self, anime_data ,anime_id):
    try:
      post = posts[post_id]
      if anime_data['user_id'] == anime['user_id']:
        anime['body'] = anime_data['body']
        return { 'message': 'Post Updated' }, 202
      return {'message': "Unauthorized"}, 401
    except:
      return {'message': "Invalid Post Id"}, 400

  def delete(self, anime_id):
    try:
      del animes[anime_id]
      return {"message": "Post Deleted"}, 202
    except:
      return {'message':"Invalid Post"}, 400

@bp.route('/')
class PostList(MethodView):

  @bp.response(200, PostSchema(many = True))
  def get(self):
    return  list(animes.values())
  
  @bp.arguments(PostSchema)
  def post(self, post_data):
    user_id = anime_data['user_id']
    if user_id in users:
      animes[uuid4()] = anime_data
      return { 'message': "Post Created" }, 201
    return { 'message': "Invalid User"}, 401
