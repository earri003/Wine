import pathlib
import os 
from typing import Union, Dict
import pandas as pd 
from pathlib import Path
thisdir = pathlib.Path(__file__).resolve().parent 



def load_wine_data(path: pathlib.Path) -> pd.DataFrame:
    path_files=  Path(path).glob('*.csv')
    list_of_dataframes = []
    for i in path_files:
        # df = pd.read_csv(i)
        list_of_dataframes.append(pd.read_csv(i))
    merged_df = pd.concat(list_of_dataframes)
    return (merged_df)

def get_country(df: pd.DataFrame) -> Dict:
    print (df['country'])
    
    pass

def get_taster_info(df: pd.DataFrame) -> Dict:
    pass

def main():
    data_path= thisdir.joinpath('data')
    df=load_wine_data(data_path)
    get_country(df)



if __name__ == "__main__":
    main()
