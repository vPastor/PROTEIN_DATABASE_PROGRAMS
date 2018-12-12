import sys
import gzip
#si pasan menos o mas de 4 argumentos, correccion de errores
if (len(sys.argv)>4 or len(sys.argv)<4):
    print ('Numero de argumentos invalidos')
else:
    to_print=""
    tax_id = sys.argv[1]
    compressed_uniprot_file = gzip.open(sys.argv[2],"r")
    proteina=""
    linea_descripcion=""
    printea=0
    repetidoOC=0
    for linea  in  compressed_uniprot_file:
        linea = linea.decode()
        if (('ID') == (linea[0:2])):
            linea_id=linea.split("   ")[1] 
        elif linea[0:2] == 'OC':
                dlrp = linea.replace("OC   ", "").replace(";", "|").strip().replace(" ", "")
                if repetidoOC == 0:
                    dlr = line
                    repetidoOC = 1
                else:
                    linea_descripcion += linea
        elif (('AC') == (linea[0:2])):
            linea_ac=linea.split("   ")[1].replace("\n","")
        elif (('OX') == (linea[0:2])):
            linea_prueba = linea.split('   ')
            linea_prueba=linea_prueba[1].split('=')
            linea_prueba=linea_prueba[1].replace(".", "").strip().replace(";","")
            #.split("; ")[]
        #print (linea[0:2])
        elif (('//') == (linea[0:2])):
            printea=0
            if (linea_prueba==tax_id):
                cabecera ="\n" + "> linea ac: " + linea_ac + "; linea id:" + linea_id + "; linea prueba: " + linea_prueba + "; "
                to_print += cabecera + linea_descripcion
        elif (printea==1):
            linea_descripcion+=linea.split("   ")[1]
        elif (('SQ') == (linea[0:2])):
            printea = 1
            linea_descripcion=""
    output_file=open(sys.argv[3], 'w') 
    output_file.write(to_print) 