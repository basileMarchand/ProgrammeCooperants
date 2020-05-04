from flask import Flask, render_template
from flask import request 


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Mines ParisTech"


@app.route("/wheel")
def wheel():
    name = request.args.get("name")
    return render_template("wheel.html", name= name)

@app.route("/forloop")
def forloop():
    size = request.args.get("size")
    if size is None:
        size = 10
    else:
        size = int(size)

    return render_template("forloop.html", size=size )


@app.route("/shutdown")
def shutdown():
    raise RuntimeError


if __name__=="__main__":
    try:
        app.run(debug=False, port=3002)
    except RuntimeError:
        print("Server closed")


