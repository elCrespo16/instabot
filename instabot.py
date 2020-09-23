from time import sleep
from selenium import webdriver
import random
from typing import Optional, List
import json


class User:
    def __init__(self, username: str, password: str, nombre: str):
        self.username = username
        self.password = password
        self.nombre = nombre
    def get_data(self):
        return {"user_type":None,"username":self.username,"password":self.password,"nombre":self.nombre}

class InstagramUser(User):
    def __init__(self, username: str, password: str, nombre: str, tags: Optional[List[str]]=None, comments: Optional[List[str]]=None):
        super(InstagramUser, self).__init__(username,password,nombre)
        self.tags = tags or []
        self.comments = comments or []
    def add_comment(self, comment: str):
        self.comments.append(comment)
    def add_comments(self, comments: Optional[List[str]]=None):
        if comments:
            self.comments.append(comments)
    def get_random_comment(self):
        return self.comments[random.randint(0,len(self.comments))]
    def get_data(self):
        return {"username":self.username,"password":self.password,"user_type":"Instagram","tags":self.tags,"comments":self.comments,"nombre":self.nombre}

class SetOfUsers:
    def __init__(self, users: Optional[dict]=None):
        self.users = {}
        if users:
            for user in users:
                if user["user_type"] == "Instagram":
                    self.users[user["nombre"]] = InstagramUser(user["username"],user["password"],user["nombre"],user["tags"],user["comments"])
                else:
                    self.users[user["nombre"]] = User(user["username"],user["password"],user["nombre"])
    def get_data(self):
        result = {}
        for key,value in self.users.items():
            result[key] = value.get_data()
        return result
    def add_instagram_user(self, username: str, password: str, nombre: str, tags: Optional[List[str]]=None, comments: Optional[List[str]]=None):
        if(not self.search_user(username)):
            new_instgram_user = InstagramUser(username,password,nombre,tags,comments)
            self.users[new_instgram_user["nombre"]] = new_instgram_user
            return self.users[new_instgram_user["nombre"]]
        else: return None
    def search_user(self, username:str):
        if not username in self.users: return None
        return self.users.get(username)

class FileParser:
    def parse_file(self, file_name: str):
        with open(file_name) as file:
            try:
                data_dict =  json.load(file)
                return SetOfUsers(data_dict)
            except:
                print("ERROR: No se pudo leer el fichero")
                return None
    def save_data(self, file_name: str, users: SetOfUsers):
        with open(file_name,"w") as file:
            try:
                json.dump(users.get_data(), file)
            except:
                print("ERROR:No se ha podido guardar los datos")
                return None



def main():
    command = input("Hola, Bienvenido a Instabot v0.1 ¿Que quieres hacer?\n")
    file = FileParser()
    users = SetOfUsers()
    user = None
    while command:
        if(command == "help" or command == "ayuda"):
            print("Comandos:\n-buscar usuario o find: introduce el username\n-cargar fichero o load: introduce el nombre del fichero\n-exit:cierra el programa\n")
        if(command == "buscar usuario" or command == "find"):
            username = input("Introduce el username\n")
            user = users.search_user(username)
            print(user.get_data())
        if(command == "cargar fichero" or command == "load"):
            file_name = input("Introduce el nombre del fichero\n")
            users = file.parse_file(file_name)
        if(command == "")
        if(command == "exit"):
            exit()
        else:
            print("Comando erroneom, introduce otro\n")
        command = input("¿Qué quieres hacer ahora?")

# file_name = "cuentas.txt"
#
# browser = webdriver.Firefox()
#
# browser.get('https://www.instagram.com/')
#
# sleep(5)
#
# browser.close()

if __name__ == '__main__':
    main()
