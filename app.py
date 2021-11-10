from flask import Flask,request
from getdata import test

app = Flask(__name__)

@app.route("/uhhhh",methods=["POST"])
def hello_world():
    return "test"

@app.route("/",methods=["POST"])
def tet():
    content = request.json
    test()
    return content