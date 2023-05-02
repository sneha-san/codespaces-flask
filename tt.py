# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/MAIF/shapash/master/data/titanicdata.csv')

# Initialize the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
    html.Div(className='row', children='My First App with Data',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30} ),

    html.Div(className='row', children=[
    dcc.RadioItems(options=['Fare','Age'],value='Age',inline=True,id='controls-and-radio-item')
    ]),
    
    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
        dash_table.DataTable(data=df.to_dict('records'), page_size=10)
        ]),
        html.Div(className='six columns', children=[
        dcc.Graph( figure={}, id='controls-and-graph')
        ])
    ])
])
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig=px.histogram(df, x='Sex', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
