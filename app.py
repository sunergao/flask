from flask import Flask
from flask import escape,url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return '主页'

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