import gspread
import pandas as pd
from gspread_dataframe import set_with_dataframe
from gspread.utils import rowcol_to_a1
from dotenv import load_dotenv
import os

def exec():
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
    ing = pd.concat([
        data.query('PROGRAMA == "DI194_413" and `VERSION PROGRAMA` == "V002"'),
        data.query('PROGRAMA == "DI172_413" and `VERSION PROGRAMA` == "V004"')
    ])
    # Filtrar educación
    edu = data.loc[~data["PROGRAMA"].isin(ing["PROGRAMA"].unique())]
    edu = edu.query('`VERSION PROGRAMA` == "V001"')

    # Verificación de seguridad
    assert not ing.empty and not edu.empty, "Deteniendo la ejecución para evitar sustitución con DataFrame vacío."

    # Map de las columnas para traducir nombre en letra de columna
    cols_map = {
        col_name: rowcol_to_a1(1, i + 1).replace('1', '') 
        for i, col_name in enumerate(ing.columns)
    }
    def buscarv_formula(idx:int) -> str:
        id_banner_col = cols_map["ID BANNER"]
        return f"=BUSCARV({id_banner_col}{idx+2};Postulaciones!A:A;1;FALSO)"

    ing = ing.assign(Cruce=ing.apply(lambda row: buscarv_formula(ing.index.get_loc(row.name)),axis=1))
    edu = edu.assign(Cruce=edu.apply(lambda row: buscarv_formula(edu.index.get_loc(row.name)),axis=1))

    # Cargar datos
    ing_ws.clear()
    set_with_dataframe(ing_ws,ing,row=1,col=1,resize=True)

    edu_ws.clear()
    set_with_dataframe(edu_ws, edu, row=1,col=1, resize=True)

    return True


if __name__ == '__main__':
    exec()