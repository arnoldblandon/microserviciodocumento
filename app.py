# -*- coding: utf-8 -*-
from flask import Flask, request
from utils import *

app = Flask(__name__, static_url_path='/static')

# Recibe parametros vía POST y lo renderiza en html
@app.route('/ver_factura',methods=['POST'])
def ver_factura():
	if request.method == 'POST':
		json_dict = request.get_json()
		id_factura = json_dict['id_factura']
		user       = json_dict["user"]
		description=json_dict["description"]
		signup     =json_dict["signup"]
		verify     =json_dict["verify"]
		tipe       =json_dict["type"]
		requerimiento =1
		data = load_html(id_factura,user,description,signup,verify,tipe,requerimiento)
		return data

	else:
		return ("Error..")

# Recibe parametros vía POST, renderiza los datos  en html para guardarlos en azure.
@app.route('/aprobar_factura', methods=["POST"])
def aprobar_factura():
	if request.method=='POST':
		json_dict = request.get_json()
		id_factura = json_dict['id_factura']
		user       = json_dict["user"]
		description=json_dict["description"]
		signup     =json_dict["signup"]
		verify     =json_dict["verify"]
		tipe       =json_dict["type"]
        # este parametro le indicará a load_html si solo renderiza los datos o realiza otra acción
		requerimiento = 2
		data = load_html(id_factura, user, description, signup, verify, tipe, requerimiento)
		return data


if __name__ =='__main__':
	app.run(debug = True)




