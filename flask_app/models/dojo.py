from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class Dojos:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def saveDojo(cls,data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW());'
        return connectToMySQL('dojosAndNinjas').query_db(query,data)

    @classmethod
    def getDojo(cls,data):
        query = 'SELECT name FROM dojos where id = %(id)s;'
        dojo = connectToMySQL('dojosAndNinjas').query_db(query,data)
        return dojo[0]

    @classmethod
    def allDojos(cls):
        query = 'SELECT * FROM dojos;'
        result = connectToMySQL('dojosAndNinjas').query_db(query)
        dojoList = []
        for dojo in result:
            dojoList.append(cls(dojo))
        return dojoList
