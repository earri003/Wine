from main import *
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

datapath=data_path= thisdir.joinpath('data')
df=load_wine_data(datapath)
print(df.keys)
df = df.drop(['Unnamed: 0', 'description', 'title'], 1)
available_indicators = df.columns
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Wine Review Boxplots',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash for BoxPlots', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='country'
            ),
        ],
        style={'width': '48%', 'display': 'inline-block'}),


        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in ["price", "points"]],
                value='price'
            ),
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    dcc.Graph(id='indicator-graphic')

])

@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
)

def update_graph(xaxis_column_name, yaxis_column_name
                 ):
    x=xaxis_column_name.lower()
    y=yaxis_column_name.lower()
    _df = df[[x, y]]
    # fig = px.bar(_df.groupby([x], as_index=False).median(), x=x, y="price")
    fig = px.box(_df, x=x, y=y, points=False)
    # fig.layout.plot_bgcolor = 'black'
    # fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)