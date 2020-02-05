# in memory table for registered users

# crear un json con id, username y password

#importar el archivo del archivo python user
from werkzeug.security import safe_str_cmp
from models.user import UserModel

# se elminan los jsons y se forman las listas porque es python puro
#users=[User(1,"dorbengoose","ricar481")]



# key, values
#username_mapping={u.username: u for u in users}
#userid_mapping={u.id: u for u in users}

# otra instanacia con el id como key
# valores como el body
# crecera conforme al tamanio de los usuarios
# SE utilizan los diccionarios para no tener que estar iterando cada vez que se haga una consulta, solo llamar conforme lo siguiente por
# username o por id el numero

##username_mapping['ricardo']
##username_mapping[1]

# userid_mapping={1:{
#      "id":1,
#     "username":"dorbengoose",
#     "password":"ricar481"

# }
# }

# se crearan dos funciones 
#la primera hara la autentificacion del usuario

def authenticate(username,password):
    user=UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id=payload['identity']
    return UserModel.find_by_id(user_id)      #userid_mapping.get(user_id,None)



