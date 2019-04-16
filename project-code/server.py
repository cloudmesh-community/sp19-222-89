import os
import connexion
from flask import Flask, render_template, request

print(os.getcwd())
app = connexion.App(__name__, specification_dir="./")

app.add_api("master.yaml")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=4555, debug=False)

