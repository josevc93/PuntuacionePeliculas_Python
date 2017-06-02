import zmq
import time
import sys
import os

ctx = zmq.Context()
sock = ctx.socket(zmq.PULL)

sock2 = ctx.socket(zmq.PUSH)
sock2.connect("tcp://localhost:6977")

arg = sys.argv[1]
sock.bind("tcp://*:490%s" %arg)
print("Abriendo Worker")

while True:
	data = sock.recv_string()
	time.sleep(1)
	print("Leído el dato '%s'" %data)
	#Busca la película en Filmaffinity y imdb

	for j in [0, 1]:
		origen = open('/home/jose/Escritorio/practicaSD/scrap' + str(j) + '.py','r')
		destino = open('/home/jose/Escritorio/practicaSD/scrapJ' + str(j) + '_'+ str(arg) + '.py','w')
		i = 0

		for line in origen:
			if i != 11:     
				destino.write(line)
			else:
				destino.write("\tpeliculaName = '" + data + "'\n")
			i = i + 1

		origen.close()
		destino.close()		

	for j in [0, 1]:
		os.system('scrapy runspider scrapJ' + str(j) + '_' + str(arg) + '.py -o ' + data + '.json')

	#elimina ficheros
	for j in [0,1]:
		os.remove('/home/jose/Escritorio/practicaSD/scrapJ' + str(j) + '_' + str(arg) + '.py')

	sock2.send_string(data)