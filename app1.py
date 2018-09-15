# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/todo", methods = ["GET","POST"])
def todo():
    if request.method == "POST":
        return render_template("todo.html")

    else:
        return redirect(url_for("login"))
if __name__ == "__main__":
    app.run()
