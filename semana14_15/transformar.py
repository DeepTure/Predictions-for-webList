import pandas as pd

pd.read_excel('encuesta.xlsx').to_csv('encuestas.csv', index=False)