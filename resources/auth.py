from flask import request, Response
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist

from database.models import User
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError

import datetime


class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return {'id': str(id)}, 201
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class LoginApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError

            expires_at = datetime.timedelta(days=7)
            access_token = create_access_token(
                identity=str(user.id), expires_delta=expires_at)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
