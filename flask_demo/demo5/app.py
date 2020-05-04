from flask import Flask, flash, redirect, render_template
from form import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

@app.route("/home")
def home():
    return "Hello Mines ParisTech"

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        """Log in requested for {form.username.data} with passord {form.password.data}"""
        ## Add function here to check password
        
        return redirect("/home")
    return render_template("login.html", form=form)

@app.route("/shutdown")
def shutdown():
    raise RuntimeError


if __name__=="__main__":
    try:
        app.run(debug=False, port=3001)
    except RuntimeError:
        print("Server closed")


