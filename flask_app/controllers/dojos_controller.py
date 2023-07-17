from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route("/")
@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=all_dojos)


@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    Dojo.create(request.form)
    return redirect('/dojos')

@app.route("/dojos/<int:id>")
def view_one_dojo(id):
    data = {
        'id':id
    }
    one_dojo = Dojo.get_one(data)
    return render_template("dojo_one.html", one_dojo = one_dojo)