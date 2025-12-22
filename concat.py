import pandas as pd
from pathlib import Path


BASE_PATH = Path(__file__).resolve()
BASE_DIR = BASE_PATH.parent
FILES_PATH = BASE_DIR / 'documents'

def exec(out_filename:str='output') -> Path:
    files = list(FILES_PATH.glob("*.csv"))
    df_list = [pd.read_csv(file) for file in files]
    argosDf = pd.concat(df_list, axis=0)
    outpath = FILES_PATH / f'{out_filename}.csv'
    argosDf.to_csv(outpath, index=False)
    print(len(df_list), "archivos consolidados")

    return outpath


if __name__ == '__main__':
    exec()