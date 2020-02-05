
# este es una copia del ejercicio 01, pero con mejoras conforme a la leccion en turno
# # pip install Flask-JWT  JSON WEB TOKEN , encoding data
import os

from flask import Flask       #quitamos request
from flask_restful import Api  #quitamos Resource y reqparse

# reqparse actualiza no necesariamente todos los campos, seleccina por data parsing inspecciona
from flask_jwt import JWT      # Quitamos jwt_required

# se requiere llamar flask-JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
# Hay que especificarle a SQL ALCHEMY donde encontrar la base de datos
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL','sqlite:///data.db') #Al final de esta ruta es donde se especifica el tipo de Base : SQL, Postgre o bien sqlite3
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  # de forma que un objeto cambie, pero no se guarde, la extension no la tome a modificacion
# insertar una llave
app.secret_key = 'ricardo'
api = Api(app)

# la insutrccion anade una tabla por medio de SQL sin embargo, no se encarga de llenarla
# Hacer un flask decorator



jwt = JWT(app, authenticate, identity)
# JWT crea un nuevo endpoint con la ruta /auth
# luego jwt hace la autenticacion con username y password
# cuando encuentra el correcto objeto usario , compara el password correspondiente
##items = [] ELIMINAMOS LA LISTA EN VACIO PORQUE YA NO SE ALMACENARAN TEMPORALMENTE EN UNA LISTA, SINO EN UNA BASE DE DATOS LOS ARTICULOS


# se van a aplicar funciones filtro a continuacion





#aqui se agregan los endpoints para cada metodo de Flask
#se agrega el metodo o funcion y la ruta final o endpoint 
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

#cuando se llama cualquier end point, va y ejecuta lo especificado en cada metodo
# por ejemplo cuando se accesa a /register, python va y ejecuta lo especificado en UserRegister
if __name__ == "__main__":
    app.run(debug=True)
