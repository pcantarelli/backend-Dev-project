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

    # if session["email"]:
    #    user_found = mongo.db.users.find_one({"email": session["email"]})
    #    username = user_found[username]
    #    flash("Hey {}, welcome back!".format(user_found[username]))
    #    return redirect(url_for("programs_list", username=session["user"]))

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
        if user_found:
            # Check password hashed
            if check_password_hash(user_found["password"], request.form.get("password")):
                print("username found" + user_found["username"])
                session["user"] = user_found["username"]
                print(session["user"])
                flash("Hey {}, welcome back!".format(user_found["username"].capitalize()))
                return redirect(url_for("programs_list", username=session["user"]))
            else:
                # Password incorrect
                error_login = "Username and/or Password incorrect!"
                return render_template("index.html", error_login=error_login)

        else:
            # If username don't exists
            error_login = "Username and/or Password incorrect!"
            return render_template("index.html", error_login=error_login)
    else:
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


# TEST
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


# @app.route("/program")
# def program(program_id):
#     return render_template("program.html")

# FIX
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

# # FIX
# @app.route("/add_program")
# def add_program():
#     return render_template("add_program.html")

# # FIX
# @app.route("/delete_program")
# def delete_program():
#     return render_template("programs_list.html")


# @app.route("/edit_program")
# def edit_program():
#     # render list o program names to edit
#     return render_template("edit_program.html")


@app.route("/add_exercise", methods=["GET", "POST"])
def add_exercise():
    return render_template("add_exercise.html")

# # FIX
# @app.route("/delete_exercise")
# def delete_exercise():
#     return render_template("edit_program.html")

# # FIX
# @app.route("/edit_exercise", methods=["GET", "POST"])
# def edit_exercise():
#     return render_template("edit_exercise.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")


@app.route("/logout")
def logout():
    flash("Logged out successfully!")
    session.pop("user")
    return redirect(url_for("index"))

# FIX
@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)

