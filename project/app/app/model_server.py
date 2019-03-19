"""
Main module of the server file
"""

from flask import jsonify, request
import connexion
from run_model import run_model


# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("master.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)

@app.route("/runmodel", methods=['GET', 'POST'])
def do_this():
    if request.method == 'POST':
        return jsonify('post')
    if request.method == 'GET':
        return jsonify('get')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=False)
