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
        
        if user_found:
            # Check password hashed
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["email"] = request.form.get("email")
                        flash("Hey {}, welcome back!".format(user_found[username]))
                        return redirect(url_for(
                            "programs_list", username=session["user"]))
            else:
                # Password incorrect
                error_message = "Username and/or Password incorrect!"
                return render_template("index.html", error_message=error_message)

        else:
            # If username don't exists
            error_message = "Username and/or Password incorrect!"
            return render_template("index.html", error_message=error_message)
    else:
        flash("Login Error!")
        return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Verify if email already exists
        user_found = mongo.db.users.find_one(
            {"email": request.form.get("email")})

        if user_found:
            error_message = "Username already used!"
            return render_template("index.html", error_message=error_message)

        register_user = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "dob": request.form.get("dob"),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register_user)

        # Add user info into 'session' cookie and redirect to programs
        session["user"] = request.form.get("email")
        flash("Registration Successful!")
        return redirect(url_for("programs_list", username=session["user"]))

    else:
        flash("Registration Error!")
        return render_template("index.html")


# # TEST
# @app.route("/programs_list")
# def programs_list(username):
#     username = mongo.db.users.find_one(
#         {"username": session["user"]})["username"]
#     # render list of program cards
#     return render_template("programs_list.html", username=username)


# @app.route("/program")
# def program(program_id):
#     return render_template("program.html")

# # FIX
# @app.route("/edit_list")
# def edit_list():
#     # render list o program names to edit
#     return render_template("edit_list.html")

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


# @app.route("/add_exercise", methods=["GET", "POST"])
# def add_exercise():
#     return render_template("add_exercise.html")

# # FIX
# @app.route("/delete_exercise")
# def delete_exercise():
#     return render_template("edit_program.html")

# # FIX
# @app.route("/edit_exercise", methods=["GET", "POST"])
# def edit_exercise():
#     return render_template("edit_exercise.html")


# @app.route("/search", methods=["GET", "POST"])
# def search():
#     return render_template("search.html")


# @app.route("/logout")
# def logout():
#     flash("Logged out successfully!")
#     session.pop("user")
#     return redirect(url_for("login"))

# # FIX
# @app.route("/profile")
# def profile():
#     return render_template("profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)

