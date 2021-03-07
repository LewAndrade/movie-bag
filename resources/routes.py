from .movie import MovieApi, MoviesApi

api_v1 = '/api/v1'


def initialize_routes(api):
    api.add_resource(MoviesApi, api_v1 + '/movies')
    api.add_resource(MovieApi, api_v1 + '/movies/<id>')
