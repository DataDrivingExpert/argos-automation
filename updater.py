import gspread
import pandas as pd
from gspread_dataframe import set_with_dataframe
from dotenv import load_dotenv
import os

load_dotenv()

gc = gspread.service_account()

# Abrir documentos
ing_doc = gc.open_by_url(os.getenv('PB_ING'))
edu_doc = gc.open_by_url(os.getenv('PB_EDU'))

ing_ws = ing_doc.worksheet('Argos')
edu_ws = edu_doc.worksheet('Argos')

# Leer documento consolidado
data = pd.read_csv('documents/output.csv')

data["ID BANNER"] = data["ID BANNER"].astype(str)
data["CELULAR"] = data["CELULAR"].astype(str)

# Filtrar por programas
ing = data.query('PROGRAMA == "DI194_413" or PROGRAMA == "DI172_413"')
edu = data.loc[~data["PROGRAMA"].isin(ing["PROGRAMA"].unique())]

ing = ing.query('`VERSION PROGRAMA` in ["V002", "V004"]')
edu = edu.query('`VERSION PROGRAMA` == "V001"')

# Verificación de seguridad
assert not ing.empty and not edu.empty, "Deteniendo la ejecución para evitar sustitución con DataFrame vacío."

# print(ing.head(), ing.shape)
# print(edu.head(), edu.shape)

# Cargar datos
ing_ws.clear()
set_with_dataframe(ing_ws,ing,row=1,col=1,resize=True)

edu_ws.clear()
set_with_dataframe(edu_ws, edu, row=1,col=1, resize=True)
