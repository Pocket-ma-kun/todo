# coding: utf-8
from flask import Flask, render_template, request, redirect, url_for
import model

app = Flask(__name__)

#Land top page
@app.route("/")
def root():
    return render_template("login.html")

#Sign in button, save button
@app.route("/todo", methods = ["GET","POST"])
def todo():
    if request.method == "POST":
        print("start_name&pass")
        if(request.form["user_mail"],request.form["user_pass"]):
            print("start_if")
            user_mail = request.form["user_mail"]
            user_pass = request.form["user_pass"]
            print("user_mail = "+str(user_mail))
            print("user_pass = "+str(user_pass))
            print("end_if")

        elif(request.form["title"]):
            title = request.form["title"]
            print(title)

        """
        priority = request.form["priority"]
        deadline_date = request.form["deadline_date"]
        deadline_time = request.form["deadline_time"]
        time_req = request.form["time_req"]

        print(priority)
        print(deadline_date)
        print(deadline_time)
        print(time_req)
        print("end_entry")
        """
        print("end_name&pass")
        return render_template("todo.html")
    else:
        return redirect(url_for("login"))

#Sign out button
@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()
