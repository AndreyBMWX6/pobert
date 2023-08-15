from dash import Dash, html, dcc, Input, Output
import pobert
import vk_api

#
import pandas as pd
import enums

app = Dash(__name__)

prev_clicks = 0

default_text = ''

classes = ['Music', 'Photos', 'Books', 'Films']

prediction = ''

pob = pobert.Pobert()

app.layout = html.Div([
    dcc.Markdown("post id", id='label'),
    dcc.Input(
    id='post_id',
    placeholder='id поста в вк',
    type='text',
    value='',
    style={'width': '20%'},
    ),
    html.Button(children='Отправить', id='submit-button-state', n_clicks=0),
    html.Div(id="prediction", children=default_text),
    html.Div(
        children=[
            dcc.Markdown("Classes:", id='list name'),
            html.Ul(id='list', title='classes', children=[html.Li(i) for i in classes])
        ],
    )
])

@app.callback(
Output(component_id='prediction', component_property='children'),
Input('submit-button-state', 'n_clicks'),
Input(component_id='post_id', component_property='value'),
)
def process_callback(n_clicks, post_id):
    global prev_clicks, prediction

    if n_clicks == 0 or n_clicks == prev_clicks:
        return default_text
    
    prev_clicks = n_clicks

    if post_id == '':
        prediction = default_text
    else:
        data = vk_api.get_data(post_id)
        prediction = pob.predict(data) # tokenizer

    return prediction


if __name__ == "__main__":
    app.run(debug=True)
