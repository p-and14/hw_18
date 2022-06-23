import sqlalchemy.orm.exc
from flask import request
from flask_restx import Namespace, Resource

from dao.model.movie import MovieSchema
from container import movie_service

movie_ns = Namespace("movies")
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        did = request.args.get("director_id")
        gid = request.args.get("genre_id")
        year = request.args.get("year")

        if did:
            movies = movie_service.get_by_filter(did=did)
        elif gid:
            movies = movie_service.get_by_filter(gid=gid)
        elif year:
            movies = movie_service.get_by_filter(year=year)
        else:
            movies = movie_service.get_all()

        if not movies:
            return "Фильмы не найдены", 404

        result = movies_schema.dump(movies)

        return result, 200

    def post(self):
        try:
            req_json = request.json
            movie_service.create(req_json)
        except TypeError:
            return "Переданы неправильные ключи"

        return "Фильм добавлен", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)

        if not movie:
            return f"Фильм с ID: {mid} не найден", 404

        result = movie_schema.dump(movie)

        return result, 200

    def put(self, mid: int):
        req_json = request.json
        req_json["id"] = mid
        try:
            movie_service.update(req_json)
        except AttributeError:
            return f"Фильм с ID: {mid} не найден"

        return "", 204

    def delete(self, mid: int):
        try:
            movie_service.delete(mid)
        except sqlalchemy.orm.exc.UnmappedInstanceError:
            return f"Фильм с ID: {mid} не найден"

        return "", 204
