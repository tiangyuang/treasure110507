from flask import Flask, request
from getdata import getData

app = Flask(__name__)

# @app.route("/uhhhh",methods=["POST"])
# def hello_world():
#     return "test"

@app.route("/")
def index():
    photo = request.args.get('photo')
    getData(photo)

    return photo
@app.route("/test")
def test():
    return "yusiang is good and smart"
