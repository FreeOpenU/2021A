import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import plotly

import pandas as pd

# How to store?

df = pd.read_csv('auth.csv')

VALID_USERNAME_PASSWORD_PAIRS = dict(df[['username', 'password']].values.tolist())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    html.H1('Welcome to the app'),
    html.H3('You are successfully authorized'),
], className='container')

# @app.callback(

if __name__ == '__main__':
    app.run_server(debug=True)