from flask_app.models.dojo import Dojos
from flask import render_template, redirect, request, session
from flask_app import app


from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninjas
# from flask_app.models.dojo import 


@app.route("/")
def index():
    
    return render_template('Dojos.html', getDojo = Dojos.allDojos())


@app.route('/dojos', methods = ['post']) 
def homePage():
    Dojos.saveDojo(request.form)
    return redirect('/')




