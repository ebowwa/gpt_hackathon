from flask import Flask
app = Flask(__name__)

@app.route("/userinput", methods=["POST"]))
def user_input():
    return "<p>Hello, World!</p>" // userinput object -> Twelvelabs search

@app.route("/")