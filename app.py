import os
import click
from flask import Flask
from flask import escape,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path,'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)    #后写

@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)

@app.route('/home/<name>')
def user_page(name):
    return 'user name:%s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('index'))
    print(url_for('user_page',name='sunergao'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'test_page'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# name = 'sunergao'
# movies = [
#     {'title':'大话西游','year':'1999'},
#     {'title':'肖申克的救赎','year':'1999'},
#     {'title':'动物也疯狂','year':'1999'},
#     {'title':'楚门的世界','year':'1999'},
# ]

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)

@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop.')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
def forge():
    db.create_all()

    name = 'sunergao'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title = m['title'],year = m['year'])
        db.session.add(movie)
    
    db.session.commit()
    click.echo('Done.')