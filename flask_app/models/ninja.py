from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models.dojo import Dojos

class Ninjas:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def addPage(cls, data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s) ;'
        return connectToMySQL('dojosAndNinjas').query_db(query,data)

    @classmethod
    def showNinjasInDojo(cls,data):
        query = 'SELECT first_name, last_name, age, dojo_id from ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojo_id = %(id)s'
        return connectToMySQL('dojosAndNinjas').query_db(query,data)