from .movie import MovieApi, MoviesApi
from .auth import SignupApi, LoginApi
from .reset_password import ForgotPassword, ResetPassword

api_v1 = '/api/v1'


def initialize_routes(api):
    api.add_resource(MoviesApi, f'{api_v1}/movies')
    api.add_resource(MovieApi, f'{api_v1}/movies/<id>')

    api.add_resource(SignupApi, f'{api_v1}/auth/signup')
    api.add_resource(LoginApi, f'{api_v1}/auth/login')

    api.add_resource(ForgotPassword, f'{api_v1}/auth/forgot')
    api.add_resource(ResetPassword, f'{api_v1}/auth/reset')
