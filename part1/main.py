import enums, db, vk_api
import pandas as pd
from dash import Dash, html, dcc, dash_table, Input, Output
from config import *


conn = db.init_db()
data = db.get_data(conn)


def convert_to_df(val):
    try:
        df = pd.DataFrame(val, columns=['post_id', 'class', 'post_audios', 'post_photos', 'post_videos', 
                                        'post_docs', 'post_links', 'post_notes', 'post_albums', 'post_postponed', 
                                        'group_id', 'group_activity', 'group_audios', 'group_photos',
                                        'group_videos', 'group_albums', 'group_topics', 'group_docs',
                                        'group_status', 'group_description', 'post_text',
                                        ])
        return df
    except Exception:
        print("failed to convert val to pd.DataFrame")
        raise ValueError


dataset = convert_to_df(data)


def read_dataset():
    return dataset[-config.DATASET_TABLE_SIZE:].to_dict('records')


prev_clicks = 0

app = Dash(__name__)

app.layout = html.Div([
    dcc.Markdown("post id", id='label'),
    dcc.Input(
    id='post_id',
    placeholder='id поста в вк',
    type='text',
    value='-111873189_3426',
    style={'width': '10%'},
    ),
    dcc.Input(
    id='group_ids',
    placeholder='id группы в вк',
    type='text',
    value='',
    style={'width': '10%'},
    ),
    dcc.Dropdown(id='class', options=enums.classes, multi=False, style={'width': '30%'}),
    html.Button(children='Отправить', id='submit-button-state', n_clicks=0),
    dash_table.DataTable(id='table', data=read_dataset())
])

@app.callback(
Output(component_id='table', component_property='data'),
Input('submit-button-state', 'n_clicks'),
Input(component_id='post_id', component_property='value'),
Input(component_id='group_ids', component_property='value'),
Input(component_id='class', component_property='value')
)
def process_callback(n_clicks, post_id, group_ids, _class):
    global dataset, prev_clicks

    if n_clicks == 0 or n_clicks == prev_clicks:
        return read_dataset()
    
    prev_clicks = n_clicks

    if _class == None:
        return read_dataset()
    
    class_id = enums.classes.index(_class)

    data_rows = []
    if post_id == '' or post_id == '-111873189_3426' and group_ids != '':
        groups, posts_data = vk_api.get_posts_data_by_groups(group_ids)
        for group in groups:
            posts = posts_data[group.id]
            for post in posts:
                data = vk_api.get_data_from_group_post(group, post)
                data_rows.append(data)

        for data in data_rows:
            db.insert_data(conn, data, class_id)
    else:
        data = vk_api.get_data(post_id)
        db.insert_data(conn, data, class_id)
    
    data = db.get_data(conn)
    dataset = convert_to_df(data)
    
    return read_dataset()
    

if __name__ == "__main__":
    app.run(debug=True)
