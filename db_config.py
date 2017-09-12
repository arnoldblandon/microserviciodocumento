from mongoengine import *  # Base de datos
#nombre de la base de datos
connect('users_links', host="localhost",port=27017)

class Link(Document):
    link = StringField(required=True, max_length=200)

# añadir link a base de datos
def guardar_link(url):
    nuevo_link = Link (
        link = url )
    nuevo_link.save()
    print(" url guardaba en base de datos")
