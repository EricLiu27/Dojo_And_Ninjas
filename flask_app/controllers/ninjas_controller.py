from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja


@app.route('/ninjas')
def new_ninja():
    all_dojos = Dojo.get_all()
    return render_template('ninjas_new.html', all_dojos = all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect (f'/dojos/{request.form["dojo_id"]}')