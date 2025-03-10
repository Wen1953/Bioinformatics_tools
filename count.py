#######################################################
########SCRIPT PARA CONTAR VALORES EN UN TXT ##########
######################################################


#1.Define la funcion "contar_repeticiones"
def contar_repeticiones(archivo):
    # Abre el archivo en modo lectura, lee y dividelo
    with open("regiones.txt", 'r') as file:
        contenido = file.read()
        palabras = contenido.split()
            
        # Crea un diccionario nuevo para almacenar las repeticiones de palabras
        conteo_palabras = {}
            
        # Cuenta las repeticiones de cada palabra
        for palabra in palabras:
            palabra = palabra.lower()
            conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1           
        return conteo_palabras


#2.Otorga los valores
archivo = "regiones.txt"
palabras_a_contar = ["amazonas","ancash","apurimac","arequipa","ayacucho","cajamarca","callao","cusco","huancavelica","huanuco","ica","junin","la_libertad","lambayeque","lima","loreto","madre_de_dios","moquegua","pasco","piura","puno","san_martin","tacna","tumbes","ucayali"]
conteo = contar_repeticiones(archivo)
# Mostrar el conteo de repeticiones de las palabras
if conteo:
    print("Conteo de repeticiones de palabras:")
    for palabra in palabras_a_contar:
        print(f"{palabra}: {conteo.get(palabra, 0)}")
