"""Contains routes to various views of the application"""

from flask import Blueprint,render_template


routes=Blueprint("routes",__name__)


@routes.route("/")
def index():
    return render_template("index.html")


@routes.route("/map1")
def map1():
    
    return render_template("cHealthU.html")

@routes.route("/map2")
def map2():
    return render_template("fixedNet.html")

@routes.route("/map3")
def map3():
    return render_template("healthStaff.html")

@routes.route("/map4")
def map4():
    return render_template("netAcess.html")

@routes.route("/map5")
def map5():
    return render_template("netUsers.html")

@routes.route("/map6")
def map6():
    return render_template("operation.html")

@routes.route("/map7")
def map7():
    return render_template("placeOfBirth.html")