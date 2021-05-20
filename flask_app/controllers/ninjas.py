from flask_app.models.ninja import Ninjas
from flask import render_template, redirect, request, session
from flask_app import app


from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojos


@app.route('/newNinja')
def createPage():

    return render_template('NewNinja.html', allDojos = Dojos.allDojos())

@app.route('/addNinja', methods = ['POST'])
def add():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    Ninjas.addPage(data)
    return redirect(f'/showNinjas/{request.form["dojo_id"]}')

@app.route('/showNinjas/<int:id>')
def showPage(id):
    data = {
        'id': id

    }
    return render_template('showNinjas.html', thisDojo = Ninjas.showNinjasInDojo(data), oneDojo = Dojos.getDojo(data))
