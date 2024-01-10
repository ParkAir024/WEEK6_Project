from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from marshmallow import post_dump

from models import AnimeModel
from schemas import PostSchema, PostSchemaNested
from . import bp

# Anime routes

@bp.route('/<anime_id>')
class Post(MethodView):

  @bp.response(200, PostSchemaNested)
  def get(self, anime_id):
    post = AnimeModel.query.get(anime_id)
    if post:
      print(post.author)
      return post 
    abort(400, message='Invalid POst')

  @bp.arguments(PostSchema)
  def put(self, anime_data ,anime_id):
    post = AnimeModel.query.get(anime_id)
    if post:
      post.body = anime_data['body']
      post.commit()
      return {'message': 'anime updated'}, 201
    return {'message': "Invalid Post Id"}, 400

  def delete(self, anime_id):
    post = AnimeModel.query.get(anime_id)
    if post:
      post.delete()
      return {"message": "Post Deleted"}, 202
    return {'message':"Invalid Post"}, 400

@bp.route('/')
class PostList(MethodView):

  @bp.response(200, PostSchema(many = True))
  def get(self):
    return AnimeModel.query.all()
  
  @bp.arguments(PostSchema)
  def post(self, anime_data):
    try:
      post = AnimeModel()
      post.user_id = anime_data['user_id']
      post.body = anime_data['body']
      post.commit()
      return { 'message': "Post Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401
