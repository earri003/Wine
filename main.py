import pathlib
import argparse
import os 
import matplotlib.pyplot as plt
import plotly.express as px
from typing import Union, Dict
import pandas as pd 
from pathlib import Path
from urllib.request import urlopen
import json
import country_converter as coco
from sklearn.preprocessing import OrdinalEncoder
thisdir = pathlib.Path(__file__).resolve().parent
savedir= thisdir.joinpath("plots")
savedir.mkdir(exist_ok=True, parents=True)

cc = coco.CountryConverter()


def load_wine_data(path: pathlib.Path) -> pd.DataFrame:
    path_files=  Path(path).glob('*.csv')
    list_of_dataframes = []
    for i in path_files:
        # df = pd.read_csv(i)
        list_of_dataframes.append(pd.read_csv(i))
    merged_df = pd.concat(list_of_dataframes)
    return (merged_df)

def fix_dataframe(df):
    df['country'] = df['country'].fillna('Unknown')
    df['points'] = df['points'].fillna(0)
    df['price'] = df['price'].fillna(0)
    df['province'] = df['province'].fillna('Unknown')
    df['region_1'] = df['region_1'].fillna('Unknown')
    df['variety'] = df['variety'].fillna('Unknown')
    df['winery'] = df['winery'].fillna('Unknown')
    df['taster_name']= df['taster_name'].fillna('Unknown')
    df['title']= df['title'].fillna('Unknown')
    df['description']= df['description'].fillna('Unknown')
    df.loc[df["country"] == "England", "country"] = "Britain"
    countries = df["country"][df["country"] != "Unknown"].unique().tolist()
    convert = dict(zip(countries, cc.convert(countries, to="ISO3")))
    # print(merged_df['country'].tolist())
    df["iso3"] = df["country"].map(convert)
    df = df.drop(['region_2', 'taster_twitter_handle', 'designation'], 1)
    df.drop_duplicates(inplace=True)
    return (df)


#Getting dataframes based off the country
def get_country(df: pd.DataFrame, country) -> Dict:
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

#Getting dataframes based off the types  of wine
def get_variety(df: pd.DataFrame, variety) -> Dict:
    # print (df['country'])
    df1 = df[df['variety'].str.contains(variety)] 
    return (df1)
    # print(df1['variety'])

#Getting dataframes based off the types  of wine
def get_winery(df: pd.DataFrame, winery) -> Dict:
    # print (df['country'])
    df1 = df[df['winery'].str.contains(winery)] 
    return (df1)
    #print(df1)

#Getting dataframes based off the types  of wine
def get_taster_name(df: pd.DataFrame, name) -> Dict:
    # print (df['country'])
    df1 = df[df['taster_name'].str.contains(name)] 
    # print(df1)
    return (df1)

def cleanData(df: pd.DataFrame):
    df1=df.drop(['Unnamed: 0','designation','description','region_1','region_2','taster_name','taster_twitter_handle','title','iso3'],axis=1)
    df1=df1.dropna(how='any')
    return (df1)


def show_graphs(df: pd.DataFrame, args_i) -> Dict:

    df1 = df[["taster_name", "country", "price"]]
    df1 = df.groupby(["taster_name", "country"], as_index=False).median()
    fig1 = px.bar(df1, x="taster_name", y="price", color="country", barmode="group")

    df2 = df[["variety", "points", "price"]]
    df2 = df.groupby(["variety", "points"], as_index=False).median()
    fig2 = px.bar(df2, x="variety", y="points", color="price", barmode="group")

    df3 = df[["country", "province", "region_1"]]
    df3 = df.groupby(["country", "province"], as_index=False).median()
    fig3 = px.bar(df3, x="country", y="province", barmode="group")

    fig4 = px.scatter_geo(df, locations="iso3", color="points", hover_name="country", size= "price" , projection="natural earth")

    if args_i=="show":
        fig1.show()
        fig2.show()
        fig3.show()
        fig4.show()
    elif args_i=="write":
        fig1.write_html(str(savedir.joinpath('figure1.html')))
        fig2.write_html(str(savedir.joinpath('figure2.html')))
        fig3.write_html(str(savedir.joinpath('figure3.html')))
        fig4.write_html(str(savedir.joinpath('figure4.html')))

def main():
    data_path= thisdir.joinpath('data')
    df=load_wine_data(data_path)
    df=fix_dataframe(df)
    df['price'] = df['price'].astype('int64')
    # df_ml['price'] = df_ml['price'].astype('int64')


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
    # print(df.dtypes)
    # enc = OrdinalEncoder()
    # df["make_code"] = enc.fit_transform(df[["country"]])
    # df[["country", "make_code"]].head(11)
    # print(df)
    # df.to_csv('testing.csv')



if __name__ == "__main__":
    main()
