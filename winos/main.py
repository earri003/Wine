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
# from .ml import clean_for_ml
thisdir = pathlib.Path(__file__).resolve().parent
savedir= thisdir.joinpath("plots")
savedir.mkdir(exist_ok=True, parents=True)

from winos.data import load_wine_data, fix_dataframe, get_country, get_price,get_province,get_score,get_taster_name,get_variety,get_winery, show_graphs
from winos.ml import clean_for_ml


def main():
    data_path= thisdir.joinpath('data')
    _df=load_wine_data(data_path)
    df=fix_dataframe(_df)
    # print(df)
    _df['price'] = _df['price'].astype('int64')
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
    parser.add_argument('--ml', type=str)
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
    if args.ml:
        ml_arg  =  args.ml
        clean_for_ml(_df, ml_arg)
        print('data: ', args.ml )

if __name__ == "__main__":
    main()
