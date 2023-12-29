import os
import psycopg2
from flask import Flask, jsonify
from api import user_controller as u_controller
from repo import user_repo as u_repo
from service import user_service as u_service
from dotenv import load_dotenv  

def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL")) 

if __name__ == '__main__':
    load_dotenv()
    app = Flask(__name__)
    conn = get_connection()
    
    user_repo = u_repo.UserRepository(conn)
    user_service = u_service.UserService(user_repo)
    user_controller = u_controller.UserController(user_service)
    
    @app.route('/api/user/count', methods=['GET'])
    def api_user_count():
        user_count = user_controller.get_user_count()
        return jsonify({"user_count": user_count})

    @app.route('/api/user/names', methods=['GET'])
    def api_first_10_user_names():
        first_10_names = user_controller.get_first_10_user_names()
        return jsonify({"first_10_user_names": first_10_names})
    
    app.run(debug=True)