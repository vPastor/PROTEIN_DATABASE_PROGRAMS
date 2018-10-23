import sys
import gzip
#si pasan menos o mas de 2 argumentos, corrección de errores
if (len(sys.argv)>2 or len(sys.argv)<2):
	print ('Numero de argumentos invalidos')
else:
	#inicializamos la variable adn para ir introduciendo datos en ella
	contador_proteinas = 0
	array = {}
	fileadn = open(sys.argv[1])
	for linea  in  fileadn:
		#si al principio de la linea encuentra el signo >, es que es una cabecera, por lo tanto, imprimir la cabecera
		#print (linea[0:2])
		if (('OX') == (linea[0:2])):
			print("\n\n")
			print (linea)
			linea_prueba = linea.split('   ')
			linea_prueba=linea_prueba[1].split('=');
			print (linea_prueba[1])
		if (('OS') == (linea[0:2])):
			print("\n\n")
			print (linea)
			linea_prueba = linea.split('   ')
			print (linea_prueba[1])
