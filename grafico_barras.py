
##################################################
####### CREANDO GRAFICO DE BARRAS APILADAS #######
##################################################
#Creado por Wendy Lizarraga


#Asignar una columna de mes al metadata.csv que siga "MES_AÑO"
#pasos previos
import pandas as pd
df1 = pd.read_csv("metadata.csv")
df1
data = df1[["FECHA_TM","MES","LINAGES"]]
data
data.to_csv("datos.csv", sep=',', index=False)



###OPCION1.-Genera un grafico de barras apiladas con todos los valores de porcentaje
..............................

#Importar librerias
import matplotlib.pyplot as plt
import pandas as pd


#Preparación de datos
df1 = pd.read_csv('datos.csv')
df1
conteos_se = df1.groupby(['MES','LINAGES']).size().reset_index(name='Recuento')
print(conteos_se)
conteos_se.to_csv("nuevo.csv", sep=',', index=False)


#Ordenar los meses
df2 = pd.read_csv('nuevo.csv')
#Cambiar los meses
orden_meses = ['ENERO_2024', 'FEBRERO_2024', 'MARZO_2024', 'ABRIL_2024', 'MAYO_2024', 'JUNIO_2024', 'JULIO_2024', 'AGOSTO_2024', 'SETIEMBRE_2024','OCTUBRE_2024','NOVIEMBRE_2024','DICIEMBRE_2024','ENERO_2025']

# Convertir la columna 'Mes' a un tipo categórico con el orden correcto
df2['MES'] = pd.Categorical(df2['MES'], categories=orden_meses, ordered=True)
df3 = df2.sort_values('MES')


# Reorganizar los datos para crear el gráfico apilado
pivot_df = df3.pivot_table(index='MES', columns='LINAGES', values='Recuento', aggfunc='sum', fill_value=0)

# Asegurarse de que las filas (índice MES) estén en el orden correcto
pivot_df = pivot_df.reindex(orden_meses)

# Calcular el porcentaje de cada linaje por mes
totales_por_mes = pivot_df.sum(axis=1)
porcentajes_df = pivot_df.div(totales_por_mes, axis=0) * 100

# Crear el gráfico de barras apiladas
ax = porcentajes_df.plot(kind='bar', stacked=True, figsize=(10, 6), cmap='tab20', width=0.7)

# Personalizar etiquetas y título
#plt.title('Secuenciación de linajes de SARS-CoV-2 por mes - 2024', fontsize=20)
plt.xlabel('Periodo', fontsize=24)
plt.ylabel('% Linajes', fontsize=24)
plt.xticks(rotation=45, ha='right', fontsize=16)
plt.yticks(fontsize=18)

# Agregar etiquetas de linajes y porcentajes en las barras con 2 decimales
for bars, linage in zip(ax.containers, pivot_df.columns):
    # Iterar sobre los valores y calcular el porcentaje
    for i, bar in enumerate(bars):
        if bar.get_height() > 0:  # Solo si el valor de la barra es mayor que 0
            porcentaje = porcentajes_df.iloc[i][linage]
            ax.text(
                bar.get_x() + bar.get_width() / 2,  # Posición X
                bar.get_y() + bar.get_height() / 2,  # Posición Y
                f'{linage}\n{porcentaje:.2f}%',  # Etiqueta con linaje y porcentaje con 2 decimales
                ha='center', va='center', fontsize=22, color='black'
            )

# Agregar leyenda
plt.legend(title='Linajes de SARS-COV-2', bbox_to_anchor=(1.05, 1), loc='upper left')

# Ajustar diseño para evitar cortes
plt.tight_layout()
plt.show()





###OPCION2.-Genera un grafico de barras apiladas con solo los valores de porcentaje > 5%
..............................

#Importar librerias
import matplotlib.pyplot as plt
import pandas as pd


#Preparación de datos
df1 = pd.read_csv('datos.csv')
df1
conteos_se = df1.groupby(['MES','LINAGES']).size().reset_index(name='Recuento')
print(conteos_se)
conteos_se.to_csv("nuevo.csv", sep=',', index=False)


#Ordenar los meses
df2 = pd.read_csv('nuevo.csv')
#Cambiar los meses
orden_meses = ['ENERO_2024', 'FEBRERO_2024', 'MARZO_2024', 'ABRIL_2024', 'MAYO_2024', 'JUNIO_2024', 'JULIO_2024', 'AGOSTO_2024', 'SETIEMBRE_2024','OCTUBRE_2024','NOVIEMBRE_2024','DICIEMBRE_2024','ENERO_2025']

# Convertir la columna 'Mes' a un tipo categórico con el orden correcto
df2['MES'] = pd.Categorical(df2['MES'], categories=orden_meses, ordered=True)
df3 = df2.sort_values('MES')


# Reorganizar los datos para crear el gráfico apilado
pivot_df = df3.pivot_table(index='MES', columns='LINAGES', values='Recuento', aggfunc='sum', fill_value=0)

# Asegurarse de que las filas (índice MES) estén en el orden correcto
pivot_df = pivot_df.reindex(orden_meses)

# Calcular el porcentaje de cada linaje por mes
totales_por_mes = pivot_df.sum(axis=1)
porcentajes_df = pivot_df.div(totales_por_mes, axis=0) * 100

# Crear el gráfico de barras apiladas
ax = porcentajes_df.plot(kind='bar', stacked=True, figsize=(10, 6), cmap='tab20', width=0.7)

# Personalizar etiquetas y título
#plt.title('Secuenciación de linajes de SARS-CoV-2 por mes - 2024', fontsize=20)
plt.xlabel('Periodo', fontsize=24)
plt.ylabel('% Linajes', fontsize=24)
plt.xticks(rotation=45, ha='right', fontsize=16)
plt.yticks(fontsize=18)

# Agregar etiquetas de linajes y porcentajes en las barras con 2 decimales
for bars, linage in zip(ax.containers, pivot_df.columns):
    # Iterar sobre los valores y calcular el porcentaje
    for i, bar in enumerate(bars):
        if bar.get_height() > 0:  # Solo si el valor de la barra es mayor que 0
            porcentaje = porcentajes_df.iloc[i][linage]
            if porcentaje > 5.00:
            	ax.text(
                    bar.get_x() + bar.get_width() / 2,  # Posición X
                    bar.get_y() + bar.get_height() / 2,  # Posición Y
                    f'{linage}\n{porcentaje:.2f}%',  # Etiqueta con linaje y porcentaje con 2 decimales
                    ha='center', va='center', fontsize=22, color='black'
                    )

# Agregar leyenda
plt.legend(title='Linajes de SARS-COV-2', bbox_to_anchor=(1.05, 1), loc='upper left')

# Ajustar diseño para evitar cortes
plt.tight_layout()
plt.show()


