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

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# FIX
@app.route("/")
def index():
    return render_template("index.html")

# TEST
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if email exists in user db
        user_found = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        print("user_found:")
        print(user_found)
        print("password:")
        print(request.form.get("password"))
        print("password match?")
        print(check_password_hash(user_found["password"], request.form.get("password")))
        if user_found:
            # Check password hashed
            if check_password_hash(user_found["password"], request.form.get("password")):
                print("password matches")
                print("username found: " + user_found["username"])
                session["user"] = user_found["username"]
                print(session["user"])
                flash("Hey {}, welcome back!".format(user_found["username"].capitalize()))
                return redirect(url_for("programs_list", username=session["user"]))
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


@app.route("/register", methods=["GET", "POST"])
def register():
    print('register function initiate')
    if request.method == "POST":
        print('request POST')

        form_email = request.form.get("email")
        print('form_email: ' + form_email)
        form_name = request.form.get("username")
        print('form_name: ' + form_name)

        # Verify if email already exists
        email_found = mongo.db.users.find_one({"email": request.form.get("email").lower()})

           
        if email_found:
            print(email_found)
            error_register = "Email already used!"
            return render_template("index.html", error_register=error_register)
        
        name_found = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if name_found:
            print(name_found)
            error_register = "User name already used!"
            return render_template("index.html", error_register=error_register)

        print("user not found")

        register_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "dob": request.form.get("dob"),
            "password": generate_password_hash(request.form.get("password"))
        }

        print("register user:")

        print(register_user)

        mongo.db.users.insert_one(register_user)

        print('user registred')

        # Add user info into 'session' cookie and redirect to programs
        session["user"] = request.form.get("username").lower()
        print(session["user"])
        flash("Registration Successful!")
        return redirect(url_for("programs_list", username=session["user"]))

    else:
        flash("Registration Error!")
        return render_template("index.html")


@app.route("/home")
def home():
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    if username:
        return render_template("home.html", username=username )

    return redirect(url_for("/"))

@app.route("/programs_list/<username>", methods=["GET", "POST"])
def programs_list(username):
    print('username: ' + username)
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    print('username: ' + username)
    exercises_list = list(mongo.db.exercises.find({"created_by": session["user"]}))
    print("exercises_list below")
    print(exercises_list)

    exercises_info = list_info(exercises_list)
    print("exercises_info below")
    print(exercises_info)

    groups_list = get_groups_list(exercises_list)
    print("groups_list below")
    print(groups_list)
    
    if username:
        # render list of program cards
        return render_template("programs_list.html", username=username, exercises_list=exercises_list, exercises_info=exercises_info, groups_list=groups_list )

    return redirect(url_for("/"))

@app.route("/edit_program")
def editor():
    print('session: ' + session["user"])
    username = mongo.db.users.find_one({"username": session["user"]})["username"]
    print('username: ' + username)
    exercises_list = list(mongo.db.exercises.find({"created_by": session["user"]}))
    print("exercises_list below")
    print(exercises_list)

    exercises_info = list_info(exercises_list)
    print("exercises_info below")
    print(exercises_info)

    groups_list = get_groups_list(exercises_list)
    print("groups_list below")
    print(groups_list)
    
    if username:
        # render list of program cards
        return render_template("edit_program.html", username=username, exercises_list=exercises_list, exercises_info=exercises_info, groups_list=groups_list )

    return redirect(url_for("/"))

@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

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

@app.route("/delete_exercise/<exercise_id>", methods=["GET", "POST"])
def delete_exercise(exercise_id):
    print('exercise id')
    print(exercise_id)
    mongo.db.exercises.remove({"_id": ObjectId(exercise_id)})
    flash("Exercise Deleted")
    return redirect(url_for("editor"))


@app.route("/edit_exercise/<exercise_id>", methods=["GET", "POST"])
def edit_exercise(exercise_id):
    username = mongo.db.users.find_one({"username": session["user"]})["username"]

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
        mongo.db.exercises.update({"_id": ObjectId(exercise_id)}, exercise_updated)
        flash("Exercise Updated")
        return redirect(url_for("editor"))

    exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    print('exercise found')
    print(exercise)
    return render_template("edit_exercise.html", exercise=exercise)

@app.route("/logout")
def logout():
    flash("Logged out successfully!")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    print("username:")
    print(username)

    user_data = mongo.db.users.find_one({"username": session["user"]})
    print(" ")
    print("user_data:")
    print(user_data)

    exercises_list = list(mongo.db.exercises.find({"created_by": session["user"]}))
    exercises_info = list_info(exercises_list)
    
    return render_template("profile.html", user=user_data, exercises_info=exercises_info)


@app.route("/status")
def status():

    user_list = list(mongo.db.users.find())
    exercises_list = list(mongo.db.exercises.find())
    exercises_total = len(exercises_list)
    groups_list = get_groups_list(exercises_list)
    user_total = len(user_list)

    return render_template("status.html", user_total=user_total, exercises_total=exercises_total, groups_list=groups_list)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        print("query:")
        print(query)
        print(" ")

        exercises_list = list(mongo.db.exercises.find({"$text": {"$search": query}}))
        print("exercises_list:")
        print(exercises_list)
        groups_list = get_groups_list(exercises_list)

        if exercises_list:
            return render_template("search.html", exercises_list=exercises_list, groups_list=groups_list, query=query)
        else:
            return render_template("search.html", no_results=True, query=query)
    
    return render_template("search.html")


#Haddling errors
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
    debug=True) # trocar para False

