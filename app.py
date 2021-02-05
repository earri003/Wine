from main import *
import dash
import dash_html_components as html
import pandas as pd

datapath=data_path= thisdir.joinpath('data')
df=load_wine_data(datapath)
print("loaded data")

def generate_table(dataframe, max_rows=100):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Wine Reivew Data'),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
