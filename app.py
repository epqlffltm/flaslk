from flask import Flask, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    user_url=url_for('user', username='john_doe')
    post_url=url_for('date', year=2023, month=3, day=15)
    return f"user_url: {user_url}, post_url: {post_url}"

@app.route('/user/<username>')
def user(username):
    return f'{username} 프로파일 {url_for("index")}'

@app.route('/date/<int:year>/<int:month>/<int:day>')
def date(year,month,day):
    return {"my_date": f"{year}-{month}-{day}"}

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return {"message": "Login successful!"}
    else:
        return {"message": "Login Form"}

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0',use_reloader=True)
