import sys
import gzip
#si pasan menos o mas de 3 argumentos, correccion de errores
if (len(sys.argv)>4 or len(sys.argv)<4):
	print ('Numero de argumentos invalidos')
else:
	#inicializamos la variable adn para ir introduciendo datos en ella
    tax_id = sys.argv[1]
    compressed_uniprot_file = gzip.open(sys.argv[2],"r")
    proteina=""
    printea=0
	for linea  in  compressed_uniprot_file:
        linea = linea.decode()
		if (('ID') == (linea[0:2])):
            linea_id=linea.split("   ")[1] 
		elif (('AC') == (linea[0:2])):
            linea_ac=linea.split("   ")[1]
        elif (('OX') == (linea[0:2])):
            linea_prueba = linea.split('   ')
            linea_prueba=linea_prueba[1].split('=')
            linea_prueba=linea_prueba[1].replace(".", "").replace("\n", "").replace(";","")
            if (linea_prueba==tax_id)
            cabecera ="\n" + "> " + linea_ac + "; " + linea_id + "; " + linea_prueba + "; "
            to_print += cabecera + linea_descripcion
            #.split("; ")[]
		#print (linea[0:2])
		elif (('//') == (linea[0:2])):
            printea=0
        elif (printea==1):
            linea_descripcion+=linea.split("   ")[1]
		elif (('SQ') == (linea[0:2])):
			printea = 1
            linea_descripcion=""
    output_file=open(sys.argv[3], 'w') 
    output_file.write(to_print) 