from flask_restful import Resource, reqparse
from globals import importResource
from repository.employee import EmployeeRepository
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt, create_access_token
from config.blacklist import BLACKLIST

conn = importResource('conn', 'config.database_instance')

class UserRegister(Resource):
    def __init__(self):
        super().__init__()
        self.arguments = reqparse.RequestParser()
        self.arguments.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank.")
        self.arguments.add_argument('user', type=str, required=True, help="The field 'user' cannot be left blank.")
        self.arguments.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank.")
        self.repo = EmployeeRepository(conn)

    @jwt_required()
    def post(self):
        data = self.arguments.parse_args()
        user_found = self.repo.find_by_login(data.get('user'))
        password = data.get('password')
        data.update({'password': generate_password_hash(password, method='sha256')})
        
        if user_found:
            return {'message': "User '{}' already exists, please use another.".format(data.get('user'))}

        result = self.repo.register_user(**data)
        return {'message': 'User created successfully!'}, 201

class UserLogin(Resource):
    def __init__(self):
        super().__init__()
        self.arguments = reqparse.RequestParser()
        self.arguments.add_argument('user', type=str, required=True, help="The field 'user' cannot be left blank.")
        self.arguments.add_argument('password', type=str, required=True, help="The field 'password' cannot be left blank.")
        self.repo = EmployeeRepository(conn)

    def post(self):
        data = self.arguments.parse_args()
        user_found = self.repo.find_by_login(data.get('user'))
        password_found = self.repo.find_password(data.get('user'))
        
        if user_found and password_found:
            pwd_hash = password_found.password
            password_checked = check_password_hash(pwd_hash, data.get('password'))

            if password_checked:
                token = create_access_token(identity=user_found.user)
                return {'access_token': token}, 200

            return {'message': 'User or Password is incorrect'}, 404
        return {'message': 'User is incorrect'}, 404

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti']
        BLACKLIST.add(jwt_id)
        return {'message': 'Logged out successfully!'}, 200
