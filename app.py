from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

"""docstring"""
@app.route('/')
def index():
    response = requests.get("https://pcs-node.azurewebsites.net/users")
    print(response.text)
    return render_template("index.html", title=response.text)

@app.route('/login', methods=['POST'])
def login():
    name = request.form["name"]
    pwd = request.form["password"]
    return render_template("login.html", name=name, password=pwd)

if __name__ == '__main__':
    app.run(debug=True)