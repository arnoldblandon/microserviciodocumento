import uuid # Para retonar números aletorios
import moody # renderizar vista con datos
import requests as rs
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
    endpoint = endpoints['topdf']
    url = "%s:%d%s" % (
    endpoint['host'],
    endpoint['port'],
    endpoint['urlToPDF'] )
    print (url)
    # ATENCIÓN: se le envía al micriservicio el path donde se guardará el archivo generado (correr microservicio "htmltoPdf")
    headers = {'Content-Type': "text/html",
               "path":"/home/arnold/Escritorio/microservicio/final.pdf", }
    # Toma el html y convierte los caracteres
    htmlFinal =html.encode('utf-8').decode('utf-8').encode('ascii', 'xmlcharrefreplace')
    # Arma la url
    res = rs.post(url, data=htmlFinal, headers= headers)
    # Llama upload_to_azure, pero antes llama a create_name para asigarle un nombre al archivo
    return  upload_to_azure(nameBlob=str(create_name()))


# Asigna URL para descargar archivo
def url_dowload(nameblob):
    # La url para del c
    url = 'https://pruebamesfix.blob.core.windows.net/mycontainer/'
    archivo = nameblob
    url_final = url + archivo
    print("Archivo guardado, lo puedes descargar con la siguiente URL: " + url_final)
    # guarda url en la base de datosl guardar_link está en db_config.py
    guardar_link(url_final)


# Subir archizo a azure
def upload_to_azure(nameBlob):
	block_blob_service.create_blob_from_path(
		'mycontainer',
        nameBlob,
        # ATENCIÓN: final.pdf es el nombre asignado en la send_file, si es modificado cargará a azure un archivo erroneo, tener cuidado.
		'final.pdf',
		content_settings=ContentSettings(content_type='application/pdf') )
	return url_dowload(nameBlob)

# recibe las variables y las pinta en html
def load_html(name, secondName, lastName, secondLastName, addressCity, document, documentCity, dia, mes, ano,hora, requerimiento, visibility, contrato,entityName,entityDocument,chambersCommerce):
    # Si el requerimiento es 1 sólo pinta los datos en html
	if requerimiento == 1:
		loader = moody.make_loader('static')
		html = loader.render(contrato, name=name, secondName=secondName, lastName=lastName, secondLastName=secondLastName,
                             addressCity=addressCity, document=document, documentCity=documentCity, dia=dia, mes=mes, ano=ano,hora=hora, visibility=visibility,
                             entityName=entityName, entityDocument=entityDocument, chambersCommerce=chambersCommerce )
		return  html

    # Si el requerimiento es 2  llama a send_file para convertir el html a pdf con los datos rendereizados
	elif requerimiento == 2:
		loader = moody.make_loader('static')
		html = loader.render(contrato, name=name, secondName=secondName, lastName=lastName, secondLastName=secondLastName,
                             addressCity=addressCity, document=document, documentCity=documentCity, dia=dia, mes=mes, ano=ano,hora=hora, visibility=visibility,
                             entityName=entityName, entityDocument=entityDocument, chambersCommerce=chambersCommerce)
		toPdf = send_file(html)
		return "Se envió html exitosamente..."
