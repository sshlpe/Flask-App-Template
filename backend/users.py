from flask import Flask, request, jsonify, make_response

class AdminsRoute:
    def __init__(self, app, db, table):
        self.app = app
        self.db = db
        self.table = table

    # get all admnins
    @self.app.route('/api/flask/users', methods=['GET'])
    def get_users(self):
        try:
            users = self.table.query.all()
            data = [user.json() for user in users]
            return jsonify(data), 200
        except Exception as e:
            data = {'message': 'error creating user', 'error': str(e)}
            return make_response(jsonify(data), 500)
