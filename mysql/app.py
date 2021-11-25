import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import mysql.connector
import plotly.graph_objs as go

user_name = os.environ.get('DB_USER')
password = os.environ.get('DB_PASS')

cnxn = mysql.connector.connect(host='mysql',
                               user='root',
                               password='12345678',
                               db='Datos')

datos_tables=pd.read_sql('SELECT * FROM casos', cnxn)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

trace = go.Bar(x=datos_tables.municipio, y=datos_tables.numcasos, name='# Contagiados Risaralda')
 
datos_tables=pd.read_sql('SELECT * FROM CasosAtla', cnxn)

trace2 = go.Bar(x=datos_tables.municipio, y=datos_tables.confirmados, name='# Contagiados Atlantico')

datos_tables=pd.read_sql('SELECT * FROM CasosChoco', cnxn)

trace3 = go.Bar(x=datos_tables.municipio, y=datos_tables.numcasos, name='# Contagiados Choco')

app.layout = html.Div([
    html.Div(
        className="row",
        children=[
            html.Div(
                
                children=[
                    html.Div(
                        children=dcc.Graph(
                            id='left-graph',
                            figure={

                                'data': [trace],                            
                                'layout': {
                                    'height': 550,
                                    'margin': {
                                        'l': 30, 'b': 50, 't': 100, 'r': 0
                                    },
                                    'title':'Risaralda',
                                 'showlegend': True ,
                                 'legend': {
                                     'x': 1.2,
                                     'y': 1,
                                      }, 
                                 'xaxis':{ 'tickangle':15},
                                 'plot_bgcolor':'rgb(230, 230,230)'
                                }
                            }
                        )
                    )
                ]
            ),
            html.Div(
                
                children=html.Div([
                    dcc.Graph(
                        id='right-top-graph',
                        figure={
                            'data': [trace2],
                            'layout': {
                                    'height': 550,
                                    'margin': {
                                        'l': 30, 'b': 50, 't': 100, 'r': 0
                                    },
                                    'title':'Atlantico',
                                 'showlegend': True ,
                                 'legend': {
                                     'x': 1.2,
                                     'y': 1,
                                      }, 
                                 'xaxis':{ 'tickangle':15},
                                 'plot_bgcolor':'rgb(230, 230,230)'
                                }
                        }
                    ),
                ])
            ),
            html.Div(
                
                children=html.Div([
                    dcc.Graph(
                        id='right-bottom-graph',
                        figure={
                            'data': [trace3],
                            'layout': {
                                    'height': 550,
                                    'margin': {
                                        'l': 30, 'b': 100, 't': 100, 'r': 0
                                    },
                                    'title':'Choco',
                                 'showlegend': True ,
                                 'legend': {
                                     'x': 1.2,
                                     'y': 1,
                                      }, 
                                 'xaxis':{ 'tickangle':15},
                                 'plot_bgcolor':'rgb(230, 230,230)'
                                }
                        }
                    ),
                ])
            )
        ]
    )
])


def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)