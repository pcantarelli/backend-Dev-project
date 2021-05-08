import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from app_functions import list_info, get_groups_list
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Environment variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Route to the index page


@app.route("/")
def index():
    return render_template("index.html")


# Route to login
# On sucesss redirects to home page
# On failure redirects to index with error message
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if email exists in user db
        user_found = mongo.db.users.find_one(
            {"email": request.form.get("email")})
        if user_found:
            # Check password hashed
            if check_password_hash(
                    user_found["password"], request.form.get("password")):
                print("password matches")
                print("username found: " + user_found["username"])
                session["user"] = user_found["username"]
                print(session["user"])
                flash("Hey {}, welcome back!".format(
                    user_found["username"].capitalize()))
                return redirect(url_for("home", username=session["user"]))
            else:
                # Password incorrect
                print("password don't match")
                error_login = "Username and/or Password incorrect!"
                return render_template("index.html", error_login=error_login)
        else:
            # If username don't exists
            print("user not found")
            error_login = "Username and/or Password incorrect!"
            return render_template("index.html", error_login=error_login)
    else:
        print("Resquest POST false")
        flash("Login Error!")
        return render_template("index.html")


# Route to register user
# On sucesss redirects to home page
# On failure redirects to index with error message
@app.route("/register", methods=["GET", "POST"])
def register():
    print('register function initiate')
    if request.method == "POST":
        form_email = request.form.get("email")
        form_name = request.form.get("username")

        # Verify if email already exists
        email_found = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if email_found:
            error_register = "Email already used!"
            return render_template("index.html", error_register=error_register)

        # Verify if name already exists
        name_found = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if name_found:
            error_register = "User name already used!"
            return render_template("index.html", error_register=error_register)

        # Get register form data and add to DB
        register_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "dob": request.form.get("dob"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register_user)

        # Add user info into 'session' cookie and redirect to programs
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("home", username=session["user"]))
    else:
        flash("Registration Error!")
        return render_template("index.html")


# Route to Home page
# On failure redirects to index page
@app.route("/home")
def home():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if username:
        return render_template("home.html", username=username)

    return redirect(url_for("/"))


# Route to Program page
# On failure redirects to index page
@app.route("/programs_list/<username>", methods=["GET", "POST"])
def programs_list(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    exercises_list = list(mongo.db.exercises.find(
        {"created_by": session["user"]}))
    exercises_info = list_info(exercises_list)
    groups_list = get_groups_list(exercises_list)

    if username:
        # Render list of program cards
        return render_template(
                "programs_list.html",
                username=username,
                exercises_list=exercises_list,
                exercises_info=exercises_info,
                groups_list=groups_list)

    return redirect(url_for("/"))


# Route to Editor page
# On failure redirects to index page
@app.route("/edit_program")
def editor():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    exercises_list = list(mongo.db.exercises.find(
        {"created_by": session["user"]}))
    exercises_info = list_info(exercises_list)
    groups_list = get_groups_list(exercises_list)

    if username:
        # Render list of program cards
        return render_template(
            "edit_program.html",
            username=username,
            exercises_list=exercises_list,
            exercises_info=exercises_info,
            groups_list=groups_list)

    return redirect(url_for("/"))


# Route to Add Exercise page and add exercise to db
@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        exercise = {
            "group_name": request.form.get("group_name"),
            "exercise_name": request.form.get("exercise_name"),
            "weight": request.form.get("weight"),
            "reps": request.form.get("reps"),
            "series": request.form.get("series"),
            "time_interval": request.form.get("time_interval"),
            "created_by": username,
            "note": request.form.get("note")

        }
        mongo.db.exercises.insert_one(exercise)
        flash("Exercise Successfully Added")
        return redirect(url_for("editor"))

    return render_template("add_exercise.html", username=username)


# Route to Delete Exercise
@app.route("/delete_exercise/<exercise_id>", methods=["GET", "POST"])
def delete_exercise(exercise_id):
    mongo.db.exercises.remove({"_id": ObjectId(exercise_id)})
    flash("Exercise Deleted")
    return redirect(url_for("editor"))


# Route to Edit Exercise page and edit exercise on db
@app.route("/edit_exercise/<exercise_id>", methods=["GET", "POST"])
def edit_exercise(exercise_id):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        exercise_updated = {
            "group_name": request.form.get("group_name"),
            "exercise_name": request.form.get("exercise_name"),
            "weight": request.form.get("weight"),
            "reps": request.form.get("reps"),
            "series": request.form.get("series"),
            "time_interval": request.form.get("time_interval"),
            "created_by": username,
            "note": request.form.get("note")
        }
        mongo.db.exercises.update(
            {"_id": ObjectId(exercise_id)}, exercise_updated)
        flash("Exercise Updated")
        return redirect(url_for("editor"))

    exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    return render_template("edit_exercise.html", exercise=exercise)


# Route to logout
@app.route("/logout")
def logout():
    flash("Logged out successfully!")
    session.pop("user")
    return redirect(url_for("index"))

# Route to Profile page


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    user_data = mongo.db.users.find_one({"username": session["user"]})
    exercises_list = list(mongo.db.exercises.find(
        {"created_by": session["user"]}))
    exercises_info = list_info(exercises_list)

    return render_template(
        "profile.html",
        user=user_data,
        exercises_info=exercises_info)


# Route to Status page
@app.route("/status")
def status():
    user_list = list(mongo.db.users.find())
    exercises_list = list(mongo.db.exercises.find())
    exercises_total = len(exercises_list)
    groups_list = get_groups_list(exercises_list)
    user_total = len(user_list)

    return render_template(
        "status.html",
        user_total=user_total,
        exercises_total=exercises_total,
        groups_list=groups_list)


# Route to Search page and search query on DB
@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        exercises_list = list(mongo.db.exercises.find(
            {"$text": {"$search": query}}))
        groups_list = get_groups_list(exercises_list)

        if exercises_list:
            return render_template(
                "search.html",
                exercises_list=exercises_list,
                groups_list=groups_list,
                query=query)
        else:
            return render_template("search.html", no_results=True, query=query)

    return render_template("search.html")


# Route to copy an exercise from Search page
@app.route("/copy_exercise/<exercise_id>", methods=["GET", "POST"])
def copy_exercise(exercise_id):
    exercise_found = mongo.db.exercises.find_one(
        {"_id": ObjectId(exercise_id)})
    username = session["user"]
    exercise_found["created_by"] = username
    exercise_found.pop('_id', None)
    mongo.db.exercises.insert_one(exercise_found)

    flash("Exercise Copied Successfully")
    return redirect(url_for("programs_list", username=username))


# Error Handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def page_forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(410)
def page_gone(e):
    return render_template('410.html'), 410


@app.errorhandler(500)
def page_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
