import pandas as pd
#esta funcion sirve si y solo si es necesario transforma el xlsx a csv, me gusta decir si y solo si xdxd
pd.read_excel('encuesta.xlsx').to_csv('encuestas.csv', index=False)