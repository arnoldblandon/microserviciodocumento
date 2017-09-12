# -*- coding: utf-8 -*-
from flask import Flask, request
from utils import *

app = Flask(__name__, static_url_path='/static')

# Recibe parametros vía POST y lo renderiza en html
@app.route('/ver_contrato',methods=['POST'])
def ver_contrato():
	if request.method == 'POST':
		json_dict = request.get_json()
		# Datos de usuario
		name = json_dict['name']
		secondName = json_dict["secondName"]
		lastName = json_dict["lastName"]
		secondLastName = json_dict["secondLastName"]
		addressCity = json_dict["addressCity"]
		document = json_dict["document"]
		documentCity = json_dict["documentCity"]
		# en esta variable se carga el contrato a renderizar
		contrato = json_dict["contrato"]
		# Datos de la entidad, si no aplica para el contrato, los datos no serán tomados para renderizar.
		entityName = json_dict["entityName"]
		entityDocument = json_dict["entityDocument"]
		chambersCommerce = json_dict["chambersCommerce"]

		dia = json_dict["dia"]
		mes = json_dict["mes"]
		ano = json_dict["ano"]
		hora = json_dict["hora"]
		# este parametro le indicará a load_html si solo renderiza los datos o guarda el documento
		requerimiento =1
		# Variable para mostrar solo si se aprueba  el contrato
		visibility = False
		# llama a load_data,el cual recibe los parámetros y los renderiza en el html cargado en la variable "contrato"
		data = load_html(name, secondName, lastName, secondLastName, addressCity, document, documentCity, dia, mes, ano, hora, requerimiento,visibility, contrato,entityName,entityDocument,chambersCommerce)
		return data

	else:
		return ("Error..")

# Recibe parametros vía POST, renderiza los datos  en html para guardarlos en azure.
@app.route('/aprobar_contrato', methods=["POST"])
def aprobar_contrato():
	if request.method=='POST':
		json_dict = request.get_json()
		# Datos de usuario
		name = json_dict['name']
		secondName = json_dict["secondName"]
		lastName = json_dict["lastName"]
		secondLastName = json_dict["secondLastName"]
		addressCity = json_dict["addressCity"]
		document = json_dict["document"]
		documentCity = json_dict["documentCity"]
		# en esta variable se carga el contrato a renderizar
		contrato = json_dict["contrato"]
		# Datos de la entidad, si no aplica para el contrato, los datos no serán tomados para renderizar.
		entityName = json_dict["entityName"]
		entityDocument = json_dict["entityDocument"]
		chambersCommerce = json_dict["chambersCommerce"]

		dia = json_dict["dia"]
		mes = json_dict["mes"]
		ano = json_dict["ano"]
		hora = json_dict["hora"]
        # este parametro le indicará a load_html si solo renderiza los datos o guarda el documento
		requerimiento = 2
		# Variable para mostrar solo si se aprueba  el contrato
		visibility =True
		# llama a load_data,el cual recibe los parámetros y los renderiza en el html cargado en la variable "contrato"
		data = load_html(name, secondName, lastName, secondLastName, addressCity, document, documentCity, dia, mes, ano,
						 hora, requerimiento, visibility, contrato, entityName, entityDocument, chambersCommerce)
		return data

if __name__ =='__main__':
	app.run(debug = True)




