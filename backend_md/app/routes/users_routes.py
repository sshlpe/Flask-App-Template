from flask import Blueprint, request, jsonify, make_response
from app.models import User
from app.extensions import db

user_bp = Blueprint('user_bp', __name__)

# create user
@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.json()), 201
    except Exception as e:
        data = {'message': 'error creating user', 'error': str(e)}
        return make_response(jsonify(data), 500)

# get all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        data = [user.json() for user in users]
        return jsonify(data), 200
    except Exception as e:
        data = {'message': 'error creating user', 'error': str(e)}
        return make_response(jsonify(data), 500)

#get user by id
@user_bp.route('/users/<id>', methods=['GET'])
def get_user(id):
    try: 
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting user', 'error': str(e)}), 500)
    
#update user by id
@user_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    try: 
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name = data['name']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'user updates'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error updating user', 'error': str(e)}), 500) 

#delete user by id
@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'user deleted'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
         return make_response(jsonify({'message': 'error deleting user', 'error': str(e)}), 500)