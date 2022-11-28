# Classe que faz a conexão com o banco de dados através do Pymongo
from pymongo import MongoClient


class Db:

    def __init__(self):
        self.client = None
        self.URI = None

    # Função de conexão com o banco de dados
    def conn_db(self):

        self.URI = "mongodb://localhost:27017"

        self.client = MongoClient(self.URI)

        if self.client:
            pass
        else:
            self.client.close()

        return self.client

    # Função de criar o usuário (documento) no banco de dados. E caso a coleção (Portfolio) não exista, irá criar a coleção!
    def create_collection(self, firstname, lastname, email, user, password):

        db = self.conn_db(self)['Portfolio']

        insert_collection = db.users.insert_many(
            [
                {
                    #Valores passados pelo campo de input do pysimplegui
                    'first_name': firstname,
                    'last_name': lastname,
                    'email': email,
                    'user': user,
                    'password': password
                 }
            ]
        )

        return insert_collection

    # Função que verifica se o login e senha passados tem registro no banco de dados!
    def login_verify(self, user, password):

        db = self.conn_db(self)['Portfolio']

        collection = db['users']

        cursor = collection.count_documents({'user': user, 'password': password})

        return cursor

