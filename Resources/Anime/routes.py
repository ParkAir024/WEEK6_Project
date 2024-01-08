from flask import request
from uuid import uuid4

from app import app
from db import animes, users

# Anime routes

@app.route('/anime', methods=['GET'])
def get_animes():
    return {'animes': list(animes.values())}

@app.route('/anime/<anime_id>', methods=['GET'])
def get_anime(anime_id):
    try:
        anime = animes[anime_id]
        return {'anime': anime}, 200
    except KeyError:
        return {'message': "Invalid Anime ID"}, 400

@app.route('/anime', methods=['POST'])
def create_anime():
    post_data = request.get_json()
    user_id = post_data.get('user_id')

    if user_id in users:
        anime_id = str(uuid4())
        post_data['anime_id'] = anime_id
        animes[anime_id] = post_data
        return {'message': "Anime Added", 'anime_id': anime_id}, 201
    return {'message': "Invalid User"}, 404

@app.route('/anime/<anime_id>', methods=['PUT'])
def update_anime(anime_id):
    try:
        anime = animes[anime_id]
        post_data = request.get_json()

        if post_data.get('user_id') == anime.get('user_id'):
            anime['body'] = post_data.get('body')
            return {'message': 'Anime Updated'}, 200
        return {'message': "Unauthorized"}, 401
    except KeyError:
        return {'message': "Invalid Anime ID"}, 400

@app.route('/anime/<anime_id>', methods=['DELETE'])
def delete_anime(anime_id):
    try:
        del animes[anime_id]
        return {"message": "Anime Deleted"}, 204
    except KeyError:
        return {'message': "Invalid Anime ID"}, 400
