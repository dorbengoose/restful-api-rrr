# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',  # en este punto podemos agregar un monton de informacion
                        type=float,  # este parser completo tambien srive para formas en HTML por lo que se recomienda ampliamente
                        required=True,
                        help="This field cant be blank_anything!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs to have an store_id"
                        )

    @jwt_required()
    def get(self, name):
        # la funcion lambda filta la funcion mediante el iterador x, que asocia el nombre del iterador con el del articulo, toma la lista items
        # item = next(filter(lambda x: x['name'] == name, items), None)
        # Regresa un objeto filtro, no una lista ni un solo elemento, aplicar metodos para mostrar resultados
        # Se aplica next, para darnos el primer elemento al asociar la funcion por filtro, el resultado
        # return {"item": item}, 200 if item else 404

        # se borraron los metodos de Get a traves de listas y se ingresara metodo por base de datos

        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()

        # query="SELECT * FROM items WHERE name=?"
        # result=cursor.execute(query,(name,)) #asi va la instruccion porque es una tupla de un solo valor
        # row=result.fetchone()
        # connection.close()

        # if row:
        #     return {"item":{"name": row[0], "price": row[1]}}
        item = ItemModel.find_by_name(name)
        if item:
            # se inserta como objeto porque ya no es un diccionario, sino un objeto por eso se agrega .json()
            return item.json()
        return{"message": "Item does not exist"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"mesage": "Item already exists '{}' duplicated".format(name)}, 400
        # if next(filter(lambda x: x['name'] == name, items), None):

            # aqui agregamos el parser poqeu primerro filtramos el nombre si ya esta en la database no se hace nada, error approach
            # paramos y break, ya que los errrores se han limpiado empieza con el ciclo
            # de esa froma podemos evitar los errores que se generen y arranca limpio, para si el nombre esta en la base de datos, aborta
            # evita duplicados y para
        data = Item.parser.parse_args()
        # {'name': name, 'price': data['price']}
        item = ItemModel(name,**data) 
        try:  # ItemModel.insert(item)
            item.save_to_db()

        except:
            # internal server error
            return {"message", "An error occurred"}, 500

        return item.json(), 201
        # items.append(item)

    def delete(self, name):
        # problema que se presenta seguido en python
        # Como en todas las funciones o bien metodos de una clase, items de aqui solo es una variable local de DELETE
        # se llama por esta ocasion la GLOBAL ITEMS porque es la que queremos aplicar
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))
        # se va a sobreescribir la lista de items, EXCEPTO con el item que se va a quitar

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'The item has been deleted'}

        # SE ELIIMINA EL CODIGO DE SQLITE
        # ---------------------------------------------------------------------------
        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()

        # query="DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))

        # connection.commit()
        # connection.close()
        # return {'message': "The item: '{}' has been deleted".format(name)}
        # ---------------------------------------------------------------------------

    def put(self, name):
        # agregamos aqui a continuacion los elementos para el nuevo objeto parser por precio, price
        data = Item.parser.parse_args()
        # data = request.get_json() #quitamos request json payload por data parser
        item = ItemModel.find_by_name(name)

        # updated_item = ItemModel(name, data['price'])   # {'name': name, 'price': data['price']}

        # item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:  # mirar aqui una vez la actualizacio ha sido ejecutada en models/item.py
            item = ItemModel(name, **data) #data['price'], data['store_id']

            # try:
            #     updated_item.insert()           #guarda el dato en la base de datos,  ItemModel.insert(updated_item)
            # except:
            #     return {"message":"An error occurred inserting the item"},500
        else:
            item.price = data['price']
            
        #     try:
        #         updated_item.update()  #ItemModel.update(updated_item)
        #     except:
        #         return {"message":"An error occurred updating the item"},500

        item.save_to_db()

        return item.json()  # updatee in SQLITE


class ItemList(Resource):
    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}

 # utilizando lambdas
        # seplica toda la funcion lambda a cada elemento del query, lista funciones a elementos

        # solo utiliza map cuando trabajes con otros desarrolladores o bien otros lenguajes
        # return {'items': [x.json() for x in ItemModel.query.all()]}

        # return {'items':[item.json() for item in ItemModel.query.all()]}
        # items regresa una lista de items en json, como se obtienen?
        # se utiliza un query de SQLAlchemy, all todos los objetos de la base de datos

        # return{'items': items}
        # _____________________________SQLITE3
        # connection=sqlite3.connect('data.db')
        # cursor=connection.cursor()

        # query="SELECT * FROM items"
        # result=cursor.execute(query)
        # items=[]
        # for row in result:
        #     items.append({'id':row[0],'name':row[1],'price':row[2]})
        # connection.close()
        # _____ return {'items':items}
