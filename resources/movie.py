from flask import Response, request
from database.models import Movie
from flask_restful import Resource


class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {'id': str(id)}, 200


class MovieApi(Resource):
    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)

    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return 'OK', 200

    def delete(self, id):
        Movie.objects.get(id=id).delete()
        return 'OK', 200
