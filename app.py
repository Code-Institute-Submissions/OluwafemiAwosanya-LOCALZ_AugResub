import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_ads")
def get_ads():
    ads = list(mongo.db.business.find())
    return render_template("business.html", ads=ads)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/place_ad", methods=["GET", "POST"])
def place_ad():
    if request.method == "POST":
        ad = {
            "category_name": request.form.get("category_name"),
            "ad_name": request.form.get("ad_name"),
            "ad_description": request.form.get("ad_description"),
            "ad_address": request.form.get("ad_address"),
            "ad_telephone": request.form.get("ad_telephone"),
            "created_by": session["user"]
        }
        mongo.db.business.insert_one(ad)
        flash("Ad Successfully Added")
        return redirect(url_for("get_ads"))
        
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("place_ad.html", categories=categories)


@app.route("/edit_ad/<ad_id>", methods=["GET", "POST"])
def edit_ad(ad_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "ad_name": request.form.get("ad_name"),
            "ad_description": request.form.get("ad_description"),
            "ad_address": request.form.get("ad_address"),
            "ad_telephone": request.form.get("ad_telephone"),
            "created_by": session["user"]
        }
        mongo.db.business.update({"_id": ObjectId(ad_id)}, submit)
        flash("Ad Successfully Updated")

    ad = mongo.db.business.find_one({"_id": ObjectId(ad_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_ad.html", ad=ad, categories=categories)


@app.route("/delete_ad/<ad_id>")
def delete_ad(ad_id):
    mongo.db.business.remove({"_id": ObjectId(ad_id)})
    flash("Ad Successfully Deleted")
    return redirect(url_for("get_ads"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)