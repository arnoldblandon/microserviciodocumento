README
- Este README explica el funcionamiento de este microservicio.
----------------------------------------------------------------------------------------------------------------------------------

FUNCIONAMIENTO
- Este microservicio expone una API, esta API recibe parametros vía POST, y de acuerdo a estos, renderiza plantillas html, de acuerdo a la URL en ejecución puede guardar la plantilla en el storage de AZURE, retornar la URL para descargar dicha plantilla, o simplemente renderizrla.
----------------------------------------------------------------------------------------------------------------------------------
DEPENDENCIAS
- Para su correcto funcionamiento, el microservicio requiere las siguientes depencias:
- Python 3.5.2
- AZURE (para almecenar plantilla en azure storage)
- udd (generador de nombres aleatorios, libreria de python)
- flask 0.12.2 (correr y exponer la API)
- request (la librería de python)
- microservicio htmlToPDF ( Microservicio que convierte html a pdf)

----------------------------------------------------------------------------------------------------------------------------------
ENTORNO VIRTUAL|

Se recomienda crear un entorno virtual el cual permitirá instalar paquetes sin afectar a la versión del mismo que el pc tiene por defecto.

ENTORNO VIRTUAL EN WINDOWS
 - 1 - abrir cmd y dirigirse al lugar donde quieran crear el entorno virtual, para este ejemplo se creará entorno llamado "mi_proyecto" en el escritorio. Pasos.. EJECUTAR COMANDOS
- 1.1 -> cd Desktop
- 1.2 -> mkdir mi_proyecto
1.3 -> cd mi_proyecto
1.4 -> virtualenv .
ya tendrá el entorno virtual instalado, para acivarlo ejecute.
1.5 ->Scripts\activate
ya tendrá el entorno activado si en la linea de la consola empieza por "(mi_proyecto)"

ENTORNO VIRTUAL EN LINUX 
1 - abrir terminal y dirigirse al lugar donde quieran crear el entorno virtual, para este ejemplo se creará entorno llamado "mi_proyecto" en  el escritorio. Pasos.. EJECUTAR COMANDOS

1.1 --> cd Escritorio (puede ser Desktop)
1.2 -> mkdir mi_proyecto


----------------------------------------------------------------------------------------------------------------------------------
INSTALACIÓN DE DEPENDENCIAS|
Para instalar cada dependencia ejecute
pip

----------------------------------------------------------------------------------------------------------------------------------




