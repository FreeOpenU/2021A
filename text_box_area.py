import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) 

graph_card = dbc.Card(
    [
        dbc.CardBody(
            [dbc.Textarea(id='textzone',
            value='',
            bs_size="lg",
            className="mb-3", placeholder="Please enter statement here"),
                            ])])

app.layout = html.Div([
    
    dbc.Row([html.H1('Please inter a statement in proper')], justify="around"),
    
    dbc.Row([html.H1('grammar with all implied clauses.')], justify="around"),
    
    dbc.Row([dbc.Col(graph_card, width=8)], justify="around"),
    
    dbc.Row([dbc.Col(dbc.Button("Send to sNLP", id="prushbutton", className="mr-2"),width={ 'offset':9})]),
    
    dbc.Row([html.Div(id='textoutput', style={'whiteSpace': 'pre-line','left margin': '10'})])
])




@app.callback(
                Output('textoutput', 'children'),
                [Input('pushbutton', 'n_clicks'),Input('textzone', 'value')]
)

def text_output(n,value):
    
    if n!=None:
        
        output='{}'.format(value)
    
    return output

if __name__ == "__main__":
    app.run_server(debug=False)