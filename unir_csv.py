###############################################
########SCRIPT PARA CONCATENAR 2 CSV ##########
###############################################

#Importar libreria "pandas"
import pandas as pd

# Read CSV files into dataframes
df1 = pd.read_csv('metadata.csv')
df2 = pd.read_csv('nextrain2gisaid.csv')

# Merge dataframes
merged_df = pd.merge(df1, df2, on='CODIGO')
merged_df.to_csv('nuevo.csv', sep=';')
