import sys
import gzip
from tabulate import tabulate
#si pasan menos o mas de 3 argumentos, correccion de errores
if (len(sys.argv)>3 or len(sys.argv)<3):
	print ('Numero de argumentos invalidos')
else:
	#inicializamos la variable adn para ir introduciendo datos en ella
	contador_proteinas = 0
	array = {}
	linea_prueba=""
	linea_nombre=""
	contador = 1
	repite = 0
	fileadn = gzip.open(sys.argv[1],"r")
	filetoprint = open(sys.argv[2],"w")
	array[0]=["TaxID","Scientific Name(Common Name)","Number of proteins"]
	for linea  in  fileadn:
		linea = linea.decode()  # pasamos de line typo bit a tipo string
		#print (linea[0:2])
		if (('OX') == (linea[0:2])):
			repite = 0
			linea_prueba = linea.split('   ')
			linea_prueba=linea_prueba[1].split('=')
			linea_prueba=linea_prueba[1].replace(".", "").strip().replace(";","")
			if linea_nombre in array:
				#print array[linea_nombre]
				array[linea_nombre][2]+=1
			else:
				array[linea_nombre]=[linea_nombre,linea_prueba,contador]
			#print(contador,linea_prueba)
		elif (('OS') == (linea[0:2])):
			linea_nombre_prov = linea.split('   ')[1].replace(".", "").strip()
			if (repite == 1):
				linea_nombre += linea_nombre_prov
			else:
				linea_nombre = linea_nombre_prov
				repite = 1
	filetoprint.write(tabulate(array.values(),headers="firstrow"))
	filetoprint.close()