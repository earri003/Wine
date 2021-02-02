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
    merged_df.dropna(inplace = True) 
    return (merged_df)

def get_country(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df1 = df[df['country'].str.contains("US")] 
    return (df1)
    # print(df1['country'])

def country_chosen(df: pd.DataFrame) -> Dict:
    print(df['points'])
    pass

def main():
    data_path= thisdir.joinpath('data')
    df=load_wine_data(data_path)
    country=get_country(df)
    country_chosen(country)


    

if __name__ == "__main__":
    main()
