# import sqlite3
from db import db #importar la base de datos creada en db con SQLAlchemy

# crear un nuevo ItemModel cambiando las propiedad de name y price y eso conlleva a la creacon de un objeto

class ItemModel(db.Model): #aplicar el objeto a ItemModel porque ahora trabajara con la base de datos db
    __tablename__='items'

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(precision=2))
    store_id=db.Column(db.Integer, db.ForeignKey('stores.id'))
    store=db.relationship('StoreModel')

    def __init__(self, name, price, store_id): #define the items by name and price with the init method
        self.name=name
        self.price=price
        self.store_id= store_id

    def json(self): #JSon representation of the module, a dictionario
        return{"name":self.name, "price":self.price, "store_id":self.store_id}
            #
            #el siguiente paso es mover todos los metodos que no dependen de un recurso resource y copiarlos abajo dentro de este modulo
    @classmethod    #DEBE PERMANECER COMO CLASE PORQUE REGRESA UN OBJETO
    def find_by_name(cls,name): 
        # a continuacion los nuevos queries con SQL ALCHEMY
        # Equivalente a decir SELECT * FROM items WHERE name=name en sql/sqlite3
        return cls.query.filter_by(name=name).first()    #El query viene de db.Model enviado por SQL Alchemy
        # como se utiliza la clase ItemModel que proporciona name y price, se 
        # reemplaza ItemModel por cls

        # metemos en comentarios cuando se hicieron los querys de sqlite3
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items WHERE name=?"
        # # asi va la instruccion porque es una tupla de un solo valor
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(*row) #row[0], row[1]

    #@classmethod No tiene sentido ser un metodo de una clase, cuando por si solo lo puede ejecutar, se quita cls , item y se pone self
    def save_to_db(self): #cls,item
       # Guarda el modelo a  la base de datos
       # insertando SQL Alchemy
       db.session.add(self)
       db.session.commit() #es una coleccion de objetos que se graban en la base de datos
       # Esta sesion llama de la base, donde una vez en Python se puede asimismo modificar y escribir
       # Por lo que se reemplaza el nombre por save_to_db, guarda y actualiza a la vez.

        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()
        # query="INSERT INTO items VALUES (?,?)"
        # cursor.execute(query, (self.name, self.price))
        # connection.commit()
        # connection.close()


    def delete_from_db(self): # se reemplaza el metodo update por delete from db
        db.session.delete(self)
        db.session.commit()

        # SE ELIIMINAN LOS COMADOS DE SQLITE
        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()

        # query="UPDATE items SET price=? WHERE name=?"
        # cursor.execute(query, (self.price, self.name))

        # connection.commit()
        # connection.close()