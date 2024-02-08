from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import AnimeModel
from schemas import PostSchema, PostSchemaNested

from . import bp
# post routes

@bp.route('/<post_id>')
class Post(MethodView):

  @bp.response(200, PostSchemaNested)
  def get(self, post_id):
    post = AnimeModel.query.get(post_id)
    if post:
      return post 
    abort(400, message='Invalid Post')

  @jwt_required
  @bp.arguments(PostSchema)
  def put(self, post_data, post_id):
    post = AnimeModel.query.get(post_id)
    if post and post.user_id == get_jwt_identity():
      post.title = post_data['title']
      post.plot = post_data['plot']
      post.genre = post_data.get('genre')
      post.rating = post_data.get('rating')
      post.commit()   
      return {'message': 'List updated'}, 201
    return {'message': "Invalid Post Id"}, 400
    
  @jwt_required()
  def delete(self, post_id):
    post = AnimeModel.query.get(post_id)
    if post and post.user_id == get_jwt_identity():
      post.delete()
      return {"message": "Post Deleted"}, 202
    return {'message':"Invalid Post or User"}, 400

@bp.route('/')
class PostList(MethodView):

  @bp.response(200, PostSchemaNested(many = True))
  def get(self):
    return AnimeModel.query.all()
  
  @jwt_required()
  @bp.arguments(PostSchema)
  def post(self, post_data):
    try:
      post = AnimeModel()
      post.user_id = get_jwt_identity() 
      post.title = post_data['title']
      post.plot = post_data['plot']
      post.genre = post_data['genre']
      post.rating = post_data['rating']
      post.commit()
      return { 'message': "Post Created" }, 201
    except:
      return { 'message': "Invalid User"}, 401