import os
import psycopg2
from flask import Flask, jsonify, request
from api import user_controller as u_controller
from repo import user_repo as u_repo
from service import user_service as u_service
from api import movie_controller as m_controller
from repo import movie_repo as m_repo
from service import movie_service as m_service
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
    
    movie_repo = m_repo.MovieRepository(conn)
    movie_service = m_service.MovieService(movie_repo)
    movie_controller = m_controller.MovieController(movie_service)
    
    @app.route('/api/users/count', methods=['GET'])
    def api_user_count():
        user_count = user_controller.get_user_count()
        return jsonify({"user_count": user_count})

    @app.route('/api/users/names', methods=['GET'])
    def api_first_10_user_names():
        first_10_names = user_controller.get_first_10_user_names()
        return jsonify({"first_10_user_names": first_10_names})
    
    @app.route('/api/movies', methods=['GET'])
    def api_movie_info():
        try:
            page_size = int(request.args.get('page_size', 10)) 
            page_number = int(request.args.get('page_number', 1)) 
            
            movie_info = movie_controller.get_movie_info(page_size, page_number)
            
            return jsonify(movie_info), 200
        except ValueError:
            return jsonify({"error": "page_size and page_number must be numbers"}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    app.run(debug=True)