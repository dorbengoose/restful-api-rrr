# agregar la habilidad de llamar los usuarios y passwords de la base de datos creadas en security.py


# import salite3
import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

# en lugar de tener diccionarios, crearemos un objeto de usuarios

# # esta clase es similar a la creacion de un diccionario, pero en lugar de ser un rango de datos en json , sera un objeto en python(funcion)
# class User:
#     def __init__(self, _id, username, password):
#         self.id = _id
#         self.username = username
#         self.password = password

#     # buscamos el username de la base de datos para compararlo asi cmo tambien self para llamar cualquier metodo dentro de la funcion
#     @classmethod
#     def find_by_username(cls, username):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()
#         # llamamos linea por linea para buscar el username hasta que haga match, en dado caso
#         query = "SELECT * FROM users WHERE username=?"
#         result = cursor.execute(query, (username,))
#         row = result.fetchone()
#         if row:
#             user = cls(*row)
#         else:
#             user = None
#         connection.close()
#         return user
#         # asignamos el parametro que encuentre dentro del query con (username,) en forma de tupla
#         # seleccionar con fetchone el primer resultado dentro de la lista que encuentre el cursor
#           # cuando encuentre al elegido
#             # aqui creamos el objeto usuario con los datos que nos arroja ressultado.
#         # notar que no se esta invocando la propiedad self, pero en lugar se esta llamando la Clase User()

#     @classmethod
#     def find_by_id(cls, _id):
#         connection = sqlite3.connect('data.db')
#         cursor = connection.cursor()
#         # llamamos linea por linea para buscar el username hasta que haga match, en dado caso
#         query = "SELECT * FROM users WHERE id=?"
#         # asignamos el parametro que encuentre dentro del query con (username,) en forma de tupla
#         result = cursor.execute(query, (_id,))
#         # seleccionar con fetchone el primer resultado dentro de la lista que encuentre el cursor
#         row = result.fetchone()
#         if row:  # cuando encuentre al elegido
#             # aqui creamos el objeto usuario con los datos que nos arroja ressultado.
#             user = cls(*row)
#         else:
#             user = None
#         connection.close()
#         return user

##########################################################################
# Necesitamos crear una nueva clase que no depende de la clase User, sino para registro


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    # El Parser hace una inspeccion Parse dentro del JSON de la solicitud y enviarlo a la solicitud en data

    # crear un endpoint Flask
    # crear el metodo post

    def post(self):
        # aplicar el reqpaser para aplicar username y password
        data = UserRegister.parser.parse_args()
        # lo primero que tiene que hacer es conectar a la base

        if UserModel.find_by_username(data['username']):
            return {"Message":"User already exists"},400

        user=UserModel(**data) #unpack y pasar todo lo d data sin considerar _id cada de una las keys pasa los valores, por el parser user name y password
        user.save_to_db() #recapitular simplificar la linea 
        
        return{"message": "User created succesfully"}, 201
        # ______________________________________ SQLITE reemplazado
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO users VALUES(NULL,?,?)"
        # cursor.execute(query, (data['username'], data['password']))
        # connection.commit()
        # connection.close()

        


# Se verifica usuarios repetidos con el comando if 