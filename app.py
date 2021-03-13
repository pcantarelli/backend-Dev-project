import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
def index():
    exercises = mongo.db.exercises.find()
    # check if logged
    # if not
        # return render_template("login.html")
    # if yes 
        # return render_template("programs.html", exercises=exercises )
    return render_template("base.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/programs_list")
def login():
    # render list of program cards
    return render_template("login.html")


@app.route("/program/<program_id>")
def program(program_id):
    return render_template("program.html")
    

@app.route("/edit_list")
def edit_list():
    # render list o program names to edit
    return render_template("edit_list.html")


@app.route("/add_program")
def add_program():
    return render_template("add_program.html") 


@app.route("/delete_program")
def delete_program():
    return render_template("edit_list.html") 


@app.route("/edit_program")
def edit_program():
    # render list o program names to edit
    return render_template("edit_program.html")


@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    return render_template("add_exercise.html") 


@app.route("/delete_exercise")
def delete_exercise():
    return render_template("edit_program.html") 
    

@app.route("/edit_exercise", methods=["GET", "POST"])
def login():
    return render_template("edit_exercise.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")


@app.route("/logout")
def logout():
    return render_template("login.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)

