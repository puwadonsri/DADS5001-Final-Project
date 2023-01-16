#import library
import pymongo
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import dash
from dash import Input, Output, dcc, html, dash_table, Dash 
import plotly.graph_objs as go
import plotly.express as px
import dash_bootstrap_components as dbc

#import css
sns.set_style("dark")
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.youtube
collection = db.chat_analytics
collection_2 = db.chat_log

# Get data from MongoDB
data = list(collection.find().sort("setAmount", -1).limit(10))
name=[]
amount=[]
for x in data:
    tmp = list(x.values())
    name.append(tmp[1])
    amount.append(tmp[2])
    lst1 = name
    lst2 = amount
    dict = {'Name': lst1, 'Total': lst2} 
    df = pd.DataFrame(dict) 

l1 = lst1
l2 = lst2
df2 = df

# Get data from MongoDB
data_p2 = list(collection.find())
name_p2=[]
amount_p2=[]
for x_p2 in data_p2:
    tmp_p2 = list(x_p2.values())
    name_p2.append(tmp_p2[1])
    amount_p2.append(tmp_p2[2])
    lst1_p2 = name_p2
    lst2_p2 = amount_p2
    dict_p2 = {'Name': lst1_p2, 'Total': lst2_p2} 
    df_p2 = pd.DataFrame(dict_p2) 

l1_p2 = lst1_p2
l2_p2 = lst2_p2
df2_p2= df_p2

#group person
# Get data from MongoDB
data_p3 = list(collection_2.find())

date_p3=[]
name_p3=[]
chat_p3=[]
for x_p3 in data_p3:
    tmp_p3 = list(x_p3.values())
    date_p3.append(tmp_p3[1][0:10])
    name_p3.append(tmp_p3[2])
    chat_p3.append(tmp_p3[3])
    lst = [date_p3,name_p3,chat_p3]
    dict_p3 = {'Date': date_p3, 'Name': name_p3, 'Chat': chat_p3} 
    df_p3 = pd.DataFrame(dict_p3)  
    
df2_p3 = df_p3.groupby(['Name'])['Name'].count().sort_values(ascending=False)
dtl = df2_p3.to_dict()
df_list_p3_k = dtl.keys()
df_list_p3_v = dtl.values()

list_k = list(df_list_p3_k)
list_v = list(df_list_p3_v)
dict_kv = {'Name': list_k, 'Total': list_v} 
df_kv = pd.DataFrame(dict_kv)
 

# print (list_k)
# print (type(list_k))


#group by date
data_p4 = list(collection_2.find())
date_p4=[]
name_p4=[]
chat_p4=[]
for x_p4 in data_p4:
    tmp_p4 = list(x_p4.values())
    date_p4.append(tmp_p4[1][0:10])
    name_p4.append(tmp_p4[2])
    chat_p4.append(tmp_p4[3])
    lst = [date_p4,name_p4,chat_p4]
    dict_p4 = {'Date': date_p4, 'Name': name_p4, 'Chat': chat_p4} 
    df_p4 = pd.DataFrame(dict_p4)  
    
df2_p4 = df_p4.groupby(['Date'])['Date'].count()
dtl4 = df2_p4.to_dict()
df_list_p4_k = dtl4.keys()
df_list_p4_v = dtl4.values()

list_k4 = list(df_list_p4_k)
list_v4 = list(df_list_p4_v)
dict_kv4 = {'Date': list_k4, 'Total': list_v4} 
df_kv4 = pd.DataFrame(dict_kv4)

#table1
data_table = dash_table.DataTable(
    id='table-virtualization',
        data=df2.to_dict('records'),
        columns=[
            {'name': i, 'id': i} for i in df2.columns
        ],
        fixed_rows={ 'headers': True, 'data': 0 },
        style_cell={
            'textAlign':'center',
            'whiteSpace': 'normal'
        },
        
        virtualization=True,
        page_action='none'
)

#table2
data_table_p2 = dash_table.DataTable(
    id='table-virtualization',
        data=df2_p2.to_dict('records'),
        columns=[
            {'name': i, 'id': i} for i in df2_p2.columns
        ],
        fixed_rows={ 'headers': True, 'data': 0 },
        style_cell={
            'textAlign':'center',
            'whiteSpace': 'normal'
        },
        
        virtualization=True,
        page_action='none'
)

#table3
data_table_p3 = dash_table.DataTable(
    id='table-virtualization',
        data=df_kv.to_dict('records'),
        columns=[
            {'name': i, 'id': i} for i in df_kv.columns
        ],
        fixed_rows={ 'headers': True, 'data': 0 },
        style_cell={
            'textAlign':'center',
            'whiteSpace': 'normal'
        },
        
        virtualization=True,
        page_action='none'
)

#table4
data_table_p4 = dash_table.DataTable(
    id='table-virtualization',
        data=df_kv4.to_dict('records'),
        columns=[
            {'name': i, 'id': i} for i in df_kv4.columns
        ],
        fixed_rows={ 'headers': True, 'data': 0 },
        style_cell={
            'textAlign':'center',
            'whiteSpace': 'normal'
        },
        
        virtualization=True,
        page_action='none'
)

#Add Graph 
app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Tab One', value='tab-1-example-graph'),
        dcc.Tab(label='Tab Two', value='tab-2-example-graph'),
    ]),
    html.Div(id='tabs-content-example-graph')
])

####################################---START - UI----######################################
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("SET-หุ้น", className="display-4"),
        html.Hr(),
        html.P("กระแสความสนใจของผู้ที่ต้องการลงทุนหุ้น", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("หุ้นที่ที่ได้รับความสนใจ 10 อันดับ", href="/", active="exact"),
                dbc.NavLink("หุ้นที่ได้รับความสนใจทั้งหมด", href="/page-1", active="exact"),
                dbc.NavLink("ยอดผู้ชมใน 1 สัปดาห์", href="/page-2", active="exact"),
                dbc.NavLink("ยอดผู้ชมตามการติดตาม", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

#---แสดงหน้า Tab
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
                html.H3('หุ้นที่ที่ได้รับความสนใจ 10 อันดับ'),
                #เรียกฟังก์ชั่นตาราง แสดง
                #เรียก กราฟ แสดง
                data_table,
                dcc.Graph(
                    figure={
                        'data': [
                            {'x': l1, 'y': l2, 'type': 'bar', 'name': 'SF'},
                            # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montréal'},
                        ],
                        'layout': {
                            'title': 'Dash Data Visualization'
                        }
                    }
                )
            ])
    elif pathname == "/page-1":
         return html.Div([
            html.H3('หุ้นที่ได้รับความสนใจทั้งหมด'),
            # dcc.Graph(figure=fig),
            data_table_p2,
            dcc.Graph(
                figure={
                    'data': [
                        {'x': l1_p2, 'y': l2_p2, 'type': 'bar', 'name': 'SF'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ])
    elif pathname == "/page-2":
        return html.Div([
            html.H3('ยอดผู้ชมใน 1 สัปดาห์'),
            data_table_p4,
            dcc.Graph(
                figure={
                    'data': [
                        {'x': list_k4, 'y': list_v4, 'type': 'bar', 'name': 'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
            #app.layout 
        ])
    elif pathname == "/page-3":
        return html.Div([
            html.H3('ยอดผู้ชมตามการติดตาม'),
            data_table_p3,
            dcc.Graph(
                figure={
                    'data': [
                        {'x': list_k, 'y': list_v, 'type': 'bar', 'name': 'Montréal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
            #app.layout 
        ])
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),

        ],
        className="p-3 bg-light rounded-3",
    )
##########################################################################

if __name__ == "__main__":
    app.run_server(port=1111)