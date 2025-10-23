from flask import Flask, request, url_for,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return f'메인 페이지:{url_for("index")}'

@app.route('/user/<username>')
def profile(username):
    return f'사용자: {username}, URL: {url_for("profile", username=username)}'

@app.route('/static-example')
def static_example():
    return f'정적 파일 URL: {url_for("static", filename="style.css")}'

@app.route('/absolute')
def absolute():
    return f'외부 절대url: {url_for("index", _external=True)}'

@app.route('/http')
def http():
    return f'외부 절대url(HTTP): {url_for("index", _external=True, _scheme="http")}'

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0',use_reloader=True)