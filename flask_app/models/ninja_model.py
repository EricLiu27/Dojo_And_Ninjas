from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE



class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def create(cls,data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);'
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def get_all (cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for row_from_db in results:
            ninja_instance = cls(row_from_db)
            all_ninjas.append(ninja_instance)
        return all_ninjas