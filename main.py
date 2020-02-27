from flask import Flask, jsonify
from database.db import initialize_db
from database.models import User, Movie

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/flask',
    'port': 17017,
    'connect': False
}

initialize_db(app)


@app.route('/')
def index():
    User(name='maicon D', email='mdfilipiaki@gmail1.com', password='12312312').save()
    return 'ok'


@app.route('/list')
def list():
    users = User.objects()
    return jsonify({
        'users': users
    })


@app.route('/get')
def get():
    users = User.objects(name__contains='maicon D')
    return jsonify({
        'users': users
    })


@app.route('/delete/<id>')
def delete(id):
    try:
        user = User.objects.get(id=id)
    except Exception:
        return jsonify({
            'error': 'User nao encontrado'
        })
    user.delete()
    return 'ok'


@app.route('/create/movie')
def create():
    user = User.objects.get(id='5e57df750cf1623eebaacd0c')
    movie = Movie(name='007', user=user)
    movie.save()
    return jsonify({
        'movie': movie
    })


@app.route('/movie/get')
def getMovie():
    movie = Movie.objects.get(id='5e57ed12d3aedbb6c59e4aa0')
    return jsonify({
        'movie': {
            'name': movie.name,
            'user': movie.user
        }
    })
