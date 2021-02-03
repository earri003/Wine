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

#Getting dataframes based off the country
def get_country(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df1 = df[df['country'].str.contains("US")] 
    return (df1)
    # print(df1['country'])

#Getting dataframes based off the scores
def get_score(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df1=df[df['points'].isin(['94'])]
    return (df1)
    # print(df1['points'])

#Getting dataframes based off the price
def get_price(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df['price'] = df['price'].astype('int64') 
    df1=df[df['price'].isin(['20'])]
    return (df1)
    # print(df1['price'])

#Getting dataframes based off the province
def get_province(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df1 = df[df['province'].str.contains("California")] 
    return (df1)
    # print(df1)

#Getting dataframes based off the regions
def get_regions(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df1 = df[df['region_1'].str.contains("Napa Valley")] 
    # return (df1)
    # print(df1['region_1'])

#Getting dataframes based off the types  of wine
def get_variety(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df1 = df[df['variety'].str.contains("Pinot Noir")] 
    return (df1)
    # print(df1['variety'])

#Getting dataframes based off the types  of wine
def get_winery(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df1 = df[df['winery'].str.contains("Roco")] 
    return (df1)
    print(df1)


def country_chosen(df: pd.DataFrame) -> Dict:
    print(df['country'])
    pass

def main():
    data_path= thisdir.joinpath('data')
    df=load_wine_data(data_path)
    country=get_country(df)
    # country_chosen(country)
    points=get_score(df)
    price=get_price(df)
    province=get_province(df)
    get_regions(df) #not finished
    variety=get_variety(df)
    winery=get_winery(df)

    


    

if __name__ == "__main__":
    main()
