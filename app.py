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
    

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=80)

