from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Mines ParisTech"


@app.route("/shutdown")
def shutdown():
    raise RuntimeError


if __name__=="__main__":
    try:
        app.run(debug=False, port=3001)
    except RuntimeError:
        print("Server closed")


