from flask import Flask, Response, request, render_template 
import json

app = Flask(__name__)

@app.route('/')
def blog_root():
    return render_template('index.html')

@app.route('/hello')
def hello():
    resp = Response("Hello world", status=200, mimetype='text/plain')
    return resp

@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
    return "Nothing"

@app.route('/message', methods = ['POST'])
def api_message():
    print(request.headers['Content-Type'])
    if request.headers['Content-Type'] == 'text/plain':
        return f'Text plain message: {request.data}'
    elif request.headers['Content-Type'] == 'application/json':
        return f'JSON message: {json.dumps(request.json)}'
    else:
        return '415 Unsupported Media Type ;_'

@app.route('/blog/articles')
def blog_articles():
    return render_template(f'blog.html')

@app.route('/blog/articles/<article_id>')
def blog_articles_num(article_id):
    return render_template(f'article{article_id}.html')

if __name__ == '__main':
    app.run()
