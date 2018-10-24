import sys
import gzip
#si pasan menos o mas de 2 argumentos, correccion de errores
if (len(sys.argv)>2 or len(sys.argv)<2):
	print ('Numero de argumentos invalidos')
else:
	#inicializamos la variable adn para ir introduciendo datos en ella
	contador_proteinas = 0
	array = {}
	linea_prueba=""
	linea_nombre=""
	contador = 1
	fileadn = open(sys.argv[1])
	for linea  in  fileadn:
		#print (linea[0:2])
		if (('OX') == (linea[0:2])):
			linea_prueba = linea.split('   ')
			linea_prueba=linea_prueba[1].split('=')
			linea_prueba=linea_prueba[1].replace(".", "").replace("\n", "").replace(";","")
			if linea_nombre in array:
				print array[linea_nombre]
				array[linea_nombre][1]+=1
			else:
				array[linea_nombre]=[linea_prueba,contador]
			print(contador,linea_prueba)
		if (('OS') == (linea[0:2])):
			linea_nombre = linea.split('   ')[1].replace(".", "").replace("\n", "")
	print(array)
