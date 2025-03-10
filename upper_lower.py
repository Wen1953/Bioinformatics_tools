#############################################################
######## SCRIPT PARA CAMBIAR MAYUSCULA A MINUSCULA ##########
#############################################################

#Cambiar upper case/lower case
names = ["LIMA", "UCAYALI", "CUSCO", "TACNA"]
names_changed = [i.lower() for i in names]
print(names_changed)
#Resultado
['lima', 'ucayali', 'cusco', 'tacna']

#save names_changed in txt file
>>> with open('nombres.txt', 'w') as f:
...     for line in names_changed:
...             f.write(line)
...             f.write('\n')
