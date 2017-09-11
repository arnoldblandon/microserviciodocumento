import uuid # Para retonar números aletorios
import moody # renderizar vista con datos
import requests as rs
from flask import request
from db_config import  guardar_link
from azure_config import *
from config.config import (
    running_mode,
    endpoints )

# crea números aleotrios
def create_name():
	return uuid.uuid4()

#Recibe archvio html, carga la configuración de los endpoints en donde se encuentran los datos de la url a la que se el enviará el html
def send_file(html):
    print(html)
    endpoint = endpoints['topdf']
    url = "%s:%d%s" % (
    endpoint['host'],
    endpoint['port'],
    endpoint['urlToPDF'] )
    print (url)
    headers = {'Content-Type': "text/html",
               "path":"/home/arnold/Escritorio/microservicio/final.pdf"
               }
    # Arma la url.
    res = rs.post(url, data=html, headers= headers)
    return  upload_to_azure(nameBlob=str(create_name()))


# Asigna URL para descargar archivo
def url_dowload(nameblob):
    url = 'https://pruebamesfix.blob.core.windows.net/mycontainer/'
    archivo = nameblob
    url_final = url + archivo
    print("Archivo guardado, lo puedes descargar con la siguiente URL: " + url_final)
    # guarda url en la base de datos
    guardar_link(url_final)


# Subir archizo a azure
def upload_to_azure(nameBlob):
	block_blob_service.create_blob_from_path(
		'mycontainer',
        nameBlob,
		'nuevo.pdf',
		content_settings=ContentSettings(content_type='application/pdf') )
	return url_dowload(nameBlob)

# recibe las variables y las pinta en html
def load_html(id_factura,user,description,signup,verify,tipe,requerimiento):

    # Si el requerimiento es 1 sólo pinta los datos en html
	if requerimiento == 1:
		loader = moody.make_loader('static')
		html = loader.render('ver_factura.html', id_factura=id_factura,user=user,description=description,signup=signup,verify=verify,tipe=tipe)
		return  html

    # Si el requerimiento es 2 sólo reenderiza  los datos en html y envía
	elif requerimiento == 2:
		loader = moody.make_loader('static')
		html = loader.render('ver_factura.html', id_factura=id_factura,user=user,description=description,signup=signup,verify=verify,tipe=tipe)
		toPdf = send_file(html)
		return "Enviado al html to Pdf (Cambiar este texto por 'html' si desea ver el html renderizado)"



