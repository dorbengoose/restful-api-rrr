# agregar la habilidad de llamar los usuarios y passwords de la base de datos creadas en security.py


# import salite3
import sqlite3
from flask_restful import Resource, reqparse
from db import db

# en lugar de tener diccionarios, crearemos un objeto de usuarios

# esta clase es similar a la creacion de un diccionario, pero en lugar de ser un rango de datos en json , sera un objeto en python(funcion)

#_____________________________________________________________________
# Este modulo constitye por si solo un API
class UserModel(db.Model):
    #donde seran accesibles las tablas
    __tablename__='users' #indicar a Alchemy propiedades de la tabla y que valores contendra
    id=db.Column(db.Integer, primary_key=True)  # PRimary Key tambien indica que es unica
    username=db.Column(db.String(80))
    password=db.Column(db.String(80))

    def __init__(self, username, password):             # se borro temporalmente _id
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self) # si se quiere borrar en lugar de anadir, delete
        db.session.commit()

    # buscamos el username de la base de datos para compararlo asi cmo tambien self para llamar cualquier metodo dentro de la funcion
    @classmethod
    def find_by_username(cls, username):

        return cls.query.filter_by(username=username).first() # SELECT * FROM users

        # ________________________________________________
        # Se comentan los paramentros de sqlite3
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # # llamamos linea por linea para buscar el username hasta que haga match, en dado caso
        # query = "SELECT * FROM users WHERE username=?"
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None
        # connection.close()
        # return user
        # asignamos el parametro que encuentre dentro del query con (username,) en forma de tupla
        # seleccionar con fetchone el primer resultado dentro de la lista que encuentre el cursor
          # cuando encuentre al elegido
            # aqui creamos el objeto usuario con los datos que nos arroja ressultado.
        # notar que no se esta invocando la propiedad self, pero en lugar se esta llamando la Clase User()

    @classmethod
    def find_by_id(cls, _id):

        return cls.query.filter_by(id=_id).first()
        # lleva el _id porque es el argumento del metodo que viene de self.id=_id

    #_____________________________________________________________
    # SE REEMPLAZA EL CODIGO DE sqlite
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
    #     # llamamos linea por linea para buscar el username hasta que haga match, en dado caso
    #     query = "SELECT * FROM users WHERE id=?"
    #     # asignamos el parametro que encuentre dentro del query con (username,) en forma de tupla
    #     result = cursor.execute(query, (_id,))
    #     # seleccionar con fetchone el primer resultado dentro de la lista que encuentre el cursor
    #     row = result.fetchone()
    #     if row:  # cuando encuentre al elegido
    #         # aqui creamos el objeto usuario con los datos que nos arroja ressultado.
    #         user = cls(*row)
    #     else:
    #         user = None
    #     connection.close()
    #     return user

##########################################################################
# Necesitamos crear una nueva clase que no depende de la clase User, sino para registro

# mientras no cambiemos el API no debemos preocuparnos por los cambios afuera