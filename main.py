import pathlib
import argparse
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
    merged_df['country'] = merged_df['country'].fillna('')
    merged_df['points'] = merged_df['points'].fillna(0)
    merged_df['price'] = merged_df['price'].fillna(0)
    merged_df['province'] = merged_df['province'].fillna('')
    merged_df['region_1'] = merged_df['region_1'].fillna('')
    merged_df['variety'] = merged_df['variety'].fillna('')
    merged_df['winery'] = merged_df['winery'].fillna('')
    merged_df['taster_name']= merged_df['taster_name'].fillna('')
    merged_df['title']= merged_df['title'].fillna('')
    merged_df['description']= merged_df['description'].fillna('')
    merged_df = merged_df.drop(['region_2', 'taster_twitter_handle', 'designation'], 1)
    # print(merged_df)
    return (merged_df)

#Getting dataframes based off the country
def get_country(df: pd.DataFrame, country) -> Dict:
    # print (df['country'])
    df1 = df[df['country'].str.contains(country)] 
    #print(df1['country'])
    return (df1)

#Getting dataframes based off the scores
def get_score(df: pd.DataFrame, points) -> Dict:
    # print (df['country'])
    df1=df[df['points'].isin([points])]
    #print(df1['points'])
    return (df1)

#Getting dataframes based off the price
def get_price(df: pd.DataFrame, price) -> Dict:
    df['price'] = df['price'].astype('int64') 
    df1=df[df['price'].isin([price])]
    return (df1)
    # print(df1['price'])

#Getting dataframes based off the province
def get_province(df: pd.DataFrame, providence) -> Dict:
    # print (df['country'])
    df1 = df[df['province'].str.contains(providence)] 
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
    #print(df1)

#Getting dataframes based off the types  of wine
def get_taster_name(df: pd.DataFrame) -> Dict:
    # print (df['country'])
    df1 = df[df['taster_name'].str.contains("Roger Voss")] 
    # print(df1)
    return (df1)


def country_chosen(df: pd.DataFrame) -> Dict:
    print(df['country'])
    pass

def main():
    data_path= thisdir.joinpath('data')
    df=load_wine_data(data_path)

    parser = argparse.ArgumentParser()
    parser.add_argument('--country', type=str)
    parser.add_argument('--score', type=int)
    parser.add_argument('--price', type=int)
    parser.add_argument('--province', type=str)
    parser.add_argument('--region', type=str)
    parser.add_argument('--winery', type=str)
    parser.add_argument('--variety', type=str, nargs='*')
    parser.add_argument('--taster', type=str)
    args = parser.parse_args()
    
    if args.country:
        country_arg  =  args.country
        country=get_country(df,country_arg)
        print(country)
        print(args.country, 'was chosen')

    if args.score:
        score_arg  =  args.score
        points=get_score(df,score_arg)
        print(points)
        print('Points: ', args.score )

    if args.price:
        price_arg  =  args.price
        price=get_price(df,price_arg)
        print(price)
        print('Price: ', args.price )

    if args.province:
        province_arg  =  args.province
        province=get_province(df,province_arg)
        print(province)
        print('Providence: ', args.province )
    if args.region:
        region_arg  =  args.region
        print('Region: ', args.region )
    if args.winery:
        winery_arg  =  args.winery
        print('Winery: ', args.winery )
    if args.variety:
        variety_arg  =  args.variety
        print('Variety: ', args.variety)
    if args.taster:
        taster_arg  =  args.taster
        print('Taster  Name: ', args.taster )

    # data_path= thisdir.joinpath('data')
    # df=load_wine_data(data_path)
    # country=get_country(df,country_arg)
    # print(country)
    # country_chosen(country)
    # points=get_score(df,score_arg)
    # price=get_price(df,price_arg)
    # province=get_province(df,providence_arg)
    get_regions(df) #not finished
    variety=get_variety(df)
    winery=get_winery(df)
    taster=get_taster_name(df)

    



if __name__ == "__main__":
    main()
