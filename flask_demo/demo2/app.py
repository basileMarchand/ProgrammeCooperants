from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Mines ParisTech"


@app.route("/wheel")
def wheel():
    return render_template("wheel.html")

@app.route("/shutdown")
def shutdown():
    raise RuntimeError


if __name__=="__main__":
    try:
        app.run(debug=False, port=3002)
    except RuntimeError:
        print("Server closed")


