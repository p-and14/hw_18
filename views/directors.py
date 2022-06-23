from flask_restx import Namespace, Resource

from dao.model.director import DirectorSchema
from container import director_service

director_ns = Namespace("directors")
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        result = directors_schema.dump(directors)

        return result, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = director_service.get_one(did)

        if not director:
            return f"Режиссёр с ID: {did} не найден"
        result = director_schema.dump(director)

        return result, 200
