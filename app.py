from flask import Flask
from flask import escape,url_for,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)

@app.route('/home/<name>')
def user_page(name):
    return 'user name:%s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='sunergao'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num=2))
    return 'test_page'

name = 'sunergao'
movies = [
    {'title':'大话西游','year':'1999'},
    {'title':'肖申克的救赎','year':'1999'},
    {'title':'动物也疯狂','year':'1999'},
    {'title':'楚门的世界','year':'1999'},
]