Informar_proteinas_organismo.py -->

Programa que toma como parametros un fichero comprimido de UniProt, y un fichero de salida txt. El fichero de salida que es generado sera en formato tabular y en cada columna esta el identificador taxonomico, el nombre del organismo, y el numero de proteinas informadas de cada organismo que habia en el fichero comprimido.

Ejecucion (python3 Informar_proteinas_organismo.py [fichero_entrada.gz] [fichero_salida.txt])

grabar_sequencias_FASTA.py -->

Programa que toma como parametros un el identificador taxonomico de una especie, un fichero comprimido de UniProt, y un fichero de salida txt. El fichero de salida que es generado en formato FASTA, en el cual se imprime cada entrada que se encuentre en el fichero con el identificador taxonomico pasado por parametro.

Ejecucion (python3 grabar_sequencias_FASTA.py [identificador_taxonomico] [fichero_entrada.gz] [fichero_salida.txt])
