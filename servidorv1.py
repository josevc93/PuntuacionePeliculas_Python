import zmq
import time
import dropbox
import tempfile
import os
import subprocess
import json
import sys

print("Iniciando servidor...")

ctx = zmq.Context()
sock = ctx.socket(zmq.PULL)
sock.bind("tcp://*:6977")
tituloFichero = sock.recv_string()

print("Descargando archivo " + tituloFichero + " de Dropbox...")

#Autenticación dropbox
token = ""
dbx = dropbox.Dropbox(token)

#Descarga archivo
try:
	ruta = "/home/jose/Escritorio/practicaSD/" + tituloFichero
	dbx.files_download_to_file(ruta, "/" + tituloFichero)
except:
	print("No se ha encontrado el archivo, o el token no es correcto.")
	sys.exit()

#Se lee el archivo descargado y se almacenan las peliculas en 'peliculas'
fich = open(ruta, "r")

peliculas = []
for line in fich:
	peliculas.append(line[:-1])

print(peliculas)

fich.close()
#Se elimina el archivo descargado
os.remove(ruta)

#Crear un worker por pelicula
workers = []
tcp = 4901
for p in peliculas:
	tcp = tcp + 1
	workers.append("tcp://localhost:"+str(tcp))
    
socks = []

for worker in workers:
	sock_send = ctx.socket(zmq.PUSH)
	sock_send.connect(worker)
	socks.append(sock_send)

last = 0

#Enviar a worker
for p in peliculas:
	socks[last].send_string(p)
	last = (last+1) % len(socks)
	print("Envio a socket %d" %last)

#Espero que terminen los workers
for p in peliculas:
	a = sock.recv_string()
	print(a + " ha terminado.")

print("Creando fichero...")
#Se crea un archivo procesando los datos de scraping
newFile = open("procesado" + tituloFichero, "w")
for p in peliculas:
	print("Añadiendo " + p + " procesado...")
	fichjson = open("/home/jose/Escritorio/practicaSD/" + p + ".json", "r")
	titulos = []
	puntuaciones = []
	paginas = []
	for line in fichjson:
		titlePos = line.find('title')
		puntPos = line.find('puntuacion')
		pagPos = line.find('pagina')
	
		if titlePos != -1:
			i = titlePos  + 9
			titleEnd = -1
			while titleEnd==-1:
				if(line[i] == '"'):
					titleEnd = i
				i = i + 1
			titulos.append(line[titlePos +  9:titleEnd])

		if puntPos != -1:
			i = puntPos  + 14
			puntEnd = -1
			while puntEnd==-1:
				if(line[i] == '"'):
					puntEnd = i
				i = i + 1
			puntR = line[puntPos +  14:puntEnd].replace(',','.')
			puntuaciones.append(puntR)

		if pagPos != -1:
			i = pagPos  + 10
			pagEnd = -1
			while pagEnd==-1:
				if(line[i] == '"'):
					pagEnd = i
				i = i + 1
			paginas.append(line[pagPos +  10:pagEnd])
	
	if len(titulos) > 0:
		suma = 0.0
		i = 0	
		newFile.write(titulos[0] + "\n")
		while (i<len(titulos)):		
			newFile.write("  " + paginas[i] + ":" + puntuaciones[i] + "\n")
			suma = suma + float(puntuaciones[i])
			i = i + 1
		newFile.write("  Media: " + str(suma/len(titulos)) + "\n\n")
	fichjson.close()
	os.remove("/home/jose/Escritorio/practicaSD/" + p + ".json")
		
newFile.close()
#Se sube el fichero a dropbox
with open("/home/jose/Escritorio/practicaSD/procesado" + tituloFichero, "rb") as f:
   	dbx.files_upload(f.read(), '/procesado' + tituloFichero, mute = True)	


os.remove("/home/jose/Escritorio/practicaSD/procesado" + tituloFichero)
