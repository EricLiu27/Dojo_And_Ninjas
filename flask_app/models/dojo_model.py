from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

from flask_app.models import ninja_model

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

    @classmethod
    def create(cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def get_all (cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row_from_db in results:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos

    @classmethod
    def get_one (cls,data):
        query = """
            SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id 
            WHERE dojos.id = %(id)s;
        
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results: 
            dojo_instance = cls(results[0])
            ninjas_list = []
            for row in results:
                ninja_data = {
                    'id': row['ninjas.id'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': row['age'],
                    'created_at': row['ninjas.created_at'],
                    'updated_at': row['ninjas.updated_at'],
                    'dojo_id': row['dojo_id']
                }
                ninja_instance = ninja_model.Ninja(ninja_data)
                ninjas_list.append(ninja_instance)

            dojo_instance.all_ninjas = ninjas_list
            return dojo_instance
        return results