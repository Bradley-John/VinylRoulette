from flask import Blueprint, jsonify

from .discogs_client import get_random_album

api = Blueprint("api", __name__)


@api.route("/spin", methods=["GET"])
def spin():
    genre = "Rock"
    # request.args.get('genre')
    album = get_random_album(genre=genre)  # record
    return jsonify(album)
