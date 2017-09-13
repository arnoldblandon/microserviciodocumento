README
- Este README explica el funcionamiento de este microservicio.
----------------------------------------------------------------------------------------------------------------------------------

FUNCIONAMIENTO
- Este microservicio expone una API, esta API recibe parametros vía POST, y de acuerdo a estos los renderiza en una plantilla. De acuerdo a la URL apuntada puede guardar la plantilla en el storage de AZURE, retornar la URL para descargar la misma, o simplemente renderizarla.
----------------------------------------------------------------------------------------------------------------------------------
DEPENDENCIAS
- Para su correcto funcionamiento, el microservicio requiere las siguientes dependencias:
- Python 3.5.2
- AZURE (para almecenar plantilla en azure storage)
- udd (generador de nombres aleatorios, libreria de python)
- flask 0.12.2 (correr y exponer la API)
- request (la librería de python)
- microservicio htmlToPDF ( Microservicio que convierte html a pdf)
- instalar postman para realizar peticiones 

----------------------------------------------------------------------------------------------------------------------------------
ENTORNO VIRTUAL

Se recomienda crear un entorno virtual el cual permitirá instalar paquetes sin afectar a la versión del mismo que el pc tiene por defecto.

ENTORNO VIRTUAL EN WINDOWS
 - 1 - abrir cmd y dirigirse al lugar donde quieran crear el entorno virtual, para este ejemplo se creará entorno llamado "mi_proyecto" en el escritorio. Pasos.. EJECUTAR COMANDOS
- 1.1 -> cd Desktop
- 1.2 -> mkdir mi_proyecto
- 1.3 -> cd mi_proyecto
- 1.4 -> virtualenv .
- ya tendrá el entorno virtual instalado, para acivarlo ejecute.
- 1.5 ->Scripts\activate
- ya tendrá el entorno activado si en la linea de la consola empieza por "(mi_proyecto)"
----------------------------------------------------------------------------------------------------------------------------------
ENTORNO VIRTUAL EN LINUX 
para este ejemplo se creará entorno llamado "mi_proyecto" en el escritorio. Pasos.. EJECUTAR COMANDOS

- 1  abrir terminal y ejecutar  sudo apt-get install python3-pip 
- 1.2 luego sudo pip3 install virtualenv
- 1.3 cd Escritorio
- 1.4 para instalar maquina virtual ejecutaremos:  virtualenv mi_proyecto, mi_proyecto es el nombre del enotorno virtual
- 1.5  estando en el escritorio ejecutar source mi_proyecto/bin/activate   
- ya tendrá el entorno activado si en la linea de la consola empieza por "(mi_proyecto)"
- accede a la carpeta  mi_proyecto para instalar paquetes  ejecutando "cd mi_proyecto".

----------------------------------------------------------------------------------------------------------------------------------
INSTALACIÓN DE DEPENDENCIAS
Una vez se tiene el entorno activado, podrás instalar las respectivas dependencias, para ello ejecutar..

- pip install python==3.5.2
- pip install mongoengine
- pip install azure
- pip install flask==0.12.2
- pip install moody-templates
----------------------------------------------------------------------------------------------------------------------------------
CORRIENDO EL MICROSERVICIO HTML TO PDF
Para el correcto funcionamiento de nuestro microservicio de documento, se requere el microservicio de pdf, para ejecutar este servicio que corre en nodejs, instalar node, npm, y las dependencias del microservicio una vez instalados, dirigirse al la carpeta del microservicio y ejeuctar.
- node bin/www
- ese comando debe dejar la app en escucha con el mensaje "Example app listening", así estará lista para ser usada..

----------------------------------------------------------------------------------------------------------------------------------
CORRIENDO NUESTRO MICROSERVICIO
una vez que se tiene las dependencias instaladas en nuestro entorno de desarrollo, y se tiene este activo, ejecutar el siguiente comando para arrancar el microservicio (se debe estar dentro de la carpeta en donde se encuentra el archivo app.py).
- python app.py
debería estar viendo en la última linea, este mensaje
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 a esa URL se le harán las peticiones..
 
 ----------------------------------------------------------------------------------------------------------------------------------
- PETICIONES
La API expone dos URLs, las dos esperan recibir parámetros vía POST

- /ver_contrato
- /aprobar_contrato

URLs
- http://127.0.0.1:5000/ver_contrato
- http://127.0.0.1:5000/aprobar_contrato


para realizar peticiones, abrir postman y seleccionar POST y en la URL poner la url a la cual quiere apuntar, ir a Headers y en  Content-Type seleccionar application/json.

- ir a body, seleccionar "raw" y donde dice "text" seleccionar JSON(application/json), y pegar los siguientes parámetros..

{ 
        "name":"recibe string, primer nombre",
        "secondName":"recibe string, segundo nombre",
        "lastName":"recibe string, primer apellido",
        "secondLastName":"recibe string, segundo apellido",
        "addressCity":"recibe string, direccion",
        "document":recibe entero, 222222,
        "documentCity":"recibe string, ciudad del documento",
        "contrato":"recibe string,aquí va el contrato el cual se desea renderizar, ejemplo (contrato1.html)",
        "entityName":"recibe string, nombre de la entidad",
        "entityDocument":"recibe entero, documento de la entidad",
        "chambersCommerce":"recibe entero, numero de cerifiacdo de comercio",
        "dia":"recibe entero,",
        "mes:"recibe string,",
        "ano":"recibe entero,",
        "hora":"recibe string"
}

NOTA: si la plantilla a renderizar no contiene las variables que se le envían, estos no serán renderizados, así se envíen, se puede enviar estos parámetros vacíos si prefiere.
 ----------------------------------------------------------------------------------------------------------------------------------
- EJEMPLO DE PTECIÓN A POST http://127.0.0.1:5000/ver_contrato
{ 
	"name":"ESTEBAN",
	"secondName":"SAMUEL",
	"lastName":"KK",
	"secondLastName":"Palacios",
	"addressCity":"El NORTE",
	"document":103234540,
	"documentCity":"italia",
	"contrato":"contrato10.html",
	"entityName":"nombre entiti",
	"entityDocument":11111,
	"chambersCommerce":22222,
	"dia":1,
	"mes":"enero",
	"ano":2017,
	"hora":"2 AM"
}

-PETICIONES A http://127.0.0.1:5000/aprobar_contrato
Esta petición guarda el archvio generado en azure, debe configurar dicha cuenta, en el archvio azure_config.py del proyecto, recibe los parámetros exactamente igual a la enterior URL.

 ----------------------------------------------------------------------------------------------------------------------------------
- NOTA
En Windows se presentarán muchos inconvenientes a la hora de guardar archivos(permisos), u otros como 
"UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 35697: character maps to <undefined>"
se recomienda usar linux, para este ejemplo se usó (Ubuntu 16.4)




 

