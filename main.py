from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    name = request.form["name"]
    pwd = request.form["password"]
    return render_template("login.html", name=name, password=pwd)

if __name__ == '__main__':
    app.run(debug=True)