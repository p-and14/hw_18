from flask_restx import Namespace, Resource

from dao.model.genre import GenreSchema
from container import genre_service

genre_ns = Namespace("genres")
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        result = genres_schema.dump(genres)

        return result, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        genre = genre_service.get_one(gid)

        if not genre:
            return f"Жанр с ID: {gid} не найден"

        result = genre_schema.dump(genre)

        return result, 200
