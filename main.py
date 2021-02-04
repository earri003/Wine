import pathlib
import argparse
import os 
import matplotlib.pyplot as plt
import plotly.express as px
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
    merged_df['country'] = merged_df['country'].fillna('Unknown')
    merged_df['points'] = merged_df['points'].fillna(0)
    merged_df['price'] = merged_df['price'].fillna(0)
    merged_df['province'] = merged_df['province'].fillna('Unknown')
    merged_df['region_1'] = merged_df['region_1'].fillna('Unknown')
    merged_df['variety'] = merged_df['variety'].fillna('Unknown')
    merged_df['winery'] = merged_df['winery'].fillna('Unknown')
    merged_df['taster_name']= merged_df['taster_name'].fillna('Unknown')
    merged_df['title']= merged_df['title'].fillna('Unknown')
    merged_df['description']= merged_df['description'].fillna('Unknown')
    merged_df = merged_df.drop(['region_2', 'taster_twitter_handle', 'designation'], 1)
    # print(merged_df)
    return (merged_df)

#Getting dataframes based off the country
def get_country(df: pd.DataFrame, country) -> Dict:
    # print (df['country'])
    # df1 = df[df['country'].str.contains(country)] 
    df1 = df[df['country'].str.contains(country)] 
    # df1.country
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
def get_variety(df: pd.DataFrame, variety) -> Dict:
    # print (df['country'])
    df1 = df[df['variety'].str.contains("Pinot Noir")] 
    return (df1)
    # print(df1['variety'])

#Getting dataframes based off the types  of wine
def get_winery(df: pd.DataFrame, winery) -> Dict:
    # print (df['country'])
    df1 = df[df['winery'].str.contains("Roco")] 
    return (df1)
    #print(df1)

#Getting dataframes based off the types  of wine
def get_taster_name(df: pd.DataFrame, name) -> Dict:
    # print (df['country'])
    df1 = df[df['taster_name'].str.contains("Roger Voss")] 
    # print(df1)
    return (df1)


def country_chosen(df: pd.DataFrame) -> Dict:
    print(df['country'])
    pass

def show_graphs(df: pd.DataFrame, args_i) -> Dict:

    df1 = df[["taster_name", "country", "price"]]
    df1 = df.groupby(["taster_name", "country"], as_index=False).median()

    fig = px.bar(df1, x="taster_name", y="price", color="country", barmode="group")
    fig.show()

    df2 = df[["variety", "points", "price"]]
    df2 = df.groupby(["variety", "points"], as_index=False).median()
    fig = px.bar(df2, x="variety", y="points", color="price", barmode="group")
    fig.show()

    df3 = df[["country", "province", "region_1"]]
    df3 = df.groupby(["country", "province"], as_index=False).median()
    fig = px.bar(df3, x="country", y="province", barmode="group")
    fig.show()


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
    parser.add_argument('--graphs', type=str)
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
        winery=get_winery(df, winery_arg)
        print(winery)
        print('Winery: ', args.winery )
    if args.variety:
        variety_arg  =  args.variety
        variety=get_variety(df, variety_arg)
        print(variety)
        print('Variety: ', args.variety)
    if args.taster:
        taster_arg  =  args.taster
        taster=get_taster_name(df, taster_arg)
        print(taster)
        print('Taster  Name: ', args.taster )
    if args.graphs:
        graphs_arg  =  args.graphs
        show_graphs(df, graphs_arg)
        print('Shown graph of : ', args.graphs )

    get_regions(df) #not finished


if __name__ == "__main__":
    main()
