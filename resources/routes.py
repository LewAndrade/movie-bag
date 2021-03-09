from .movie import MovieApi, MoviesApi
from .auth import SignupApi, LoginApi

api_v1 = '/api/v1'


def initialize_routes(api):
    api.add_resource(MoviesApi,  f'{api_v1}/movies')
    api.add_resource(MovieApi, f'{api_v1}/movies/<id>')

    api.add_resource(SignupApi, f'{api_v1}/auth/signup')
    api.add_resource(LoginApi, f'{api_v1}/auth/login')
