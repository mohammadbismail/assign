from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


# @app.route("/dojo")
# def hello_world():
#     return "Dojo!"


# @app.route("/<name>")
# def my_route(name):
#     return "Hi " + name + "!"


@app.route("/repeat/<int:id>/<name>")
def repeat(id, name):
    return name * id


@app.errorhandler(404)
def notValidRoute(e):
    return "Sorry, No response. Try again"


if __name__ == "__main__":
    app.run(debug=True)
