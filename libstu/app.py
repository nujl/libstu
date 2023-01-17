from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
 
dt=pd.read_csv("data/dt.csv")
zt=pd.read_csv("data/zt.csv")
if 'Unnamed: 0' in zt.columns:
    zt = zt.drop(columns=["Unnamed: 0"])
 
def color_discrete_map_generator(sub):
   lul = px.colors.sequential.dense
   if sub=="Overall":
       col_map = {
           'None': lul[2],
           '2 Advanced Courses': lul[8],
           'Prep Courses': lul[5],
           '1 Advanced Course':lul[6],
           '3 Advanced Courses':lul[10],
           '3 Advanced Courses|Prep Course':lul[11],
           "1 Advanced Course|Prep Course":lul[7],
           "2 Advanced Courses|Prep Course":lul[9]
         }
   else:
       col_map={
           "None":lul[2],
           "Prep Courses":lul[5],
           f"AP {sub}":lul[8],                               
           f"AP {sub}|Honors {sub}|Prep Course":lul[11],
           f"AP {sub}|Prep Courses":lul[9],          
           f"AP {sub}|Honors {sub}":lul[10],
           f"Honors {sub}":lul[6],              
           f"Honors {sub}|Prep Courses":lul[7]
       }
  
  
   return col_map
 
def bar_graph(sub):
    if sub=="EMS": sub='Overall'
    temp = dt[f"{sub}_color_map"].value_counts()
    fig = px.bar(temp.values, color=temp.keys(), color_discrete_map=color_discrete_map_generator(sub), text=[f"{round(v*100/dt.shape[0], 1)}%" for v in temp.values])
    fig.update_traces(textposition="outside")
    fig.update_layout(
        title="Count",
        height=550,
        width=300,
        template='seaborn',
        yaxis={'title':'test', 'visible': True, 'title':None, 'showgrid':True, 'showticklabels':False},
        xaxis={'visible':True, 'title':None, 'showgrid':True, 'showticklabels':False},
        margin=dict(
            l = 10,        # left
            r = 10,        # right
            t = 50,        # top
            b = 10,        # bottom
        ),
        legend=dict(
        title="Types of Students",
        orientation="v",
        yanchor="top",
        y=0.99,
        xanchor="right",
        x=0.99,
        bgcolor="#EBECF0",
        bordercolor="Black",
        borderwidth=2,
        font=dict(size=13)),
        showlegend=False

    )
    return fig
 
 
def sub_plot(sub, color_toggle):
    if sub in ['English', 'Math', 'Science']:
        if color_toggle == 'Off':
            color_option = ['black']*501
            color_map_option = None
            legend_option = False
        else:
            color_option=f"{sub}_color_map"
            color_map_option=color_discrete_map_generator(sub)
            legend_option = True
        fig = px.scatter(
            data_frame = dt,
            x=f"{sub} Avg",
            y=f"{sub} ACT",
            color=color_option,
            color_discrete_map=color_map_option,
            opacity=0.8,
            trendline="ols",
            trendline_scope="overall",
            trendline_color_override="red",
            
        )
 
        fig.update_traces(marker={'size': 12})
 
        fig.update_layout(
            height=600,
            width=1000,
            title=f"{sub} Average VS {sub} ACT",
            template="seaborn",
            showlegend=legend_option,
            legend=dict(
            title="Types of Students",
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="#EBECF0",
            bordercolor="Black",
            borderwidth=2,
            font=dict(size=12)),
            margin=dict(
                l = 10,        # left
                r = 10,        # right
                t = 50,        # top
                b = 10,        # bottom
            ),
        )
        return fig
    elif sub == "Overall":
        if color_toggle == 'Off':
            color_option = ['black']*501
            color_map_option = None
            legend_option = False
        else:
            color_option=f"{sub}_color_map"
            color_map_option=color_discrete_map_generator(sub)
            legend_option = True
        fig = px.scatter(
           data_frame = dt,
           x="Last GPA",
           y="Composite ACT",
           color=color_option,
           color_discrete_map=color_map_option,
           opacity=0.8,
           trendline="ols",
           trendline_scope="overall",
           trendline_color_override="red",
          
       )
 
        fig.update_traces(marker={'size': 12})
 
        fig.update_layout(
            height=600,
            width=1000,
            title="GPA VS ACT",
            template="seaborn",
            showlegend=legend_option,
            legend=dict(
            title="Types of Students",
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="#EBECF0",
            bordercolor="Black",
            borderwidth=2,
            font=dict(size=12)),
            margin=dict(
                l = 10,        # left
                r = 10,        # right
                t = 50,        # top
                b = 10,        # bottom
            ),
        )
        return fig
    elif sub == "EMS":
        if color_toggle == 'Off':
            color_option = ['black']*501
            color_map_option = None
            legend_option = False
        else:
            color_option='Overall_color_map'
            color_map_option=color_discrete_map_generator('Overall')
            legend_option = True
        fig = px.scatter(
           data_frame = dt,
           x='EMS Avg',
           y='EMS ACT',
           color=color_option,
           color_discrete_map=color_map_option,
           opacity=0.8,
           trendline="ols",
           trendline_scope="overall",
           trendline_color_override="red"
       )
 
        fig.update_traces(marker={'size': 12})
 
        fig.update_layout(
            height=600,
            width=1000,
            title="English, Math, and Science Only",
            template="seaborn",
            showlegend=legend_option,
            legend=dict(
            title="Types of Students",
            orientation="v",
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="#EBECF0",
            bordercolor="Black",
            borderwidth=2,
            font=dict(size=12)),
            margin=dict(
                l = 10,        # left
                r = 10,        # right
                t = 50,        # top
                b = 10,        # bottom
            ),
        )
        return fig
 

def table(sub):
    if sub=="EMS": sub = 'Overall'
    tust = [color_discrete_map_generator(sub)[c] for c in zt.loc[zt["subject"]==sub]["type"]]
    new=[tust if i==1 else ['black']*64 for i in range(zt.loc[zt["subject"]==sub].shape[1])]
    fig = go.Figure(data=[go.Table(
        header=dict(
            # values=zt.loc[zt["subject"]==sub].columns,
            values=['Subject', 'Type of Student', 'Metric', 'Population Standard Devation', 'Sample Size', 'Population Mean', 'Sample Mean', 'Z Score', 'P-Value', 'p≤0.05', 'p≤0.005', 'p≤0.0005', 'p≤0.00005','Right Tail' ],
            line_color='white', fill_color='white',
            align='center', font=dict(color='black', family='Sans-serif', size=14)
        ),
        cells=dict(
            values=[zt.loc[zt["subject"]==sub][col] for col in zt.columns],
            line_color=None,
            align='left', font=dict(color=new, family='Sans-serif', size=15)
        ))
    ])
    fig.update_layout(
            height=400, 
            width=1350,
            template="seaborn",
            margin=dict(
                l = 10,        # left
                r = 10,        # right
                t = 10,        # top
                b = 10,        # bottom
            )
        )
    return fig
 
def threedee(var):
    if var =='ACT':
        fig = px.scatter_3d(dt, x='English ACT', y='Math ACT', z='Science ACT', color='Overall_color_map', color_discrete_map=color_discrete_map_generator("Overall"))
        fig.update_layout(
            height=1100, 
            width=1350,
            template="seaborn"
            # margin=dict(
            #     l = 10,        # left
            #     r = 10,        # right
            #     t = 10,        # top
            #     b = 10,        # bottom
            # )
        )
        return fig
    elif var =='Grades':
        fig = px.scatter_3d(dt, x='English Avg', y='Math Avg', z='Science Avg', color='Overall_color_map', color_discrete_map=color_discrete_map_generator("Overall"))
        fig.update_layout(
            height=1100, 
            width=1350,
            template="seaborn"
            # margin=dict(
            #     l = 10,        # left
            #     r = 10,        # right
            #     t = 10,        # top
            #     b = 10,        # bottom
            # )
        )
        return fig
 
app = Dash(__name__)

server = app.server

 
app.layout = html.Div(id="numerical scatter", children=[
                html.H1("Academics of Liberty Students", style={'color':"black", 'font-family':'Sans-serif'}),
                html.P("Color", style={'color':"black", 'font-family':'Sans-serif'}),
                dcc.RadioItems(
                    id='color_radio',
                    value='On',
                    options=[
                        {'label':'On', 'value':'On'},
                        {'label':'Off', 'value':'Off'}
                    ], style={'color':'black', 'font-family':'Sans-serif', 'font-size':'15'}),
                html.P("Options", style={'color':"black", 'font-family':'Sans-serif'}),
                dcc.RadioItems(
                    id='variables-dropdown',
                    value='Overall',
                    options=[
                        {'label': 'Overall', 'value':'Overall'},
                        {'label': 'English', 'value': 'English'},
                        {'label': 'Math', 'value': 'Math'},
                        {'label': 'Science', 'value': 'Science'},
                        {'label': 'EMS', 'value': 'EMS'}
                    ],  style={'color':"black", 'font-family':'Sans-serif', 'font-size':'15'}),
                html.Div(children=[
                    html.Div(children=[
                        html.Div(children=[dcc.Graph(id='scatter_plot')], style={'float':'left'}),
                        html.Div(children=[dcc.Graph(id="bar")], style={'float':'right'}),
                        html.Div(children=[dcc.Graph(id='table')], style={'float':'left'}),
                        html.H3('3D Visualizations', style={'color':"black", 'font-family':'Sans-serif', 'float':'left'}),  
                        dcc.RadioItems(
                            id='avg_or_act',
                            value='Grades',
                            options=[
                                {'label': 'Grades', 'value':'Grades'},
                                {'label': 'ACT', 'value': 'ACT'}
                            ],  style={'color':"black", 'font-family':'Sans-serif', 'font-size':'15', 'float':'left'}),
                        html.Div(children=[dcc.Graph(id='3d_plot')], style={'color':"black", 'family':'Sans-serif', 'float':'left'}),
                        ], className="container"), 
                ]),
                html.Div(children=[
                    
                ])
])
@app.callback(
   [Output("scatter_plot", "figure"),
   Output("bar", "figure"),
   Output('table', 'figure'),
   Output('3d_plot', 'figure')],
   [Input('color_radio', 'value'),
    Input('variables-dropdown', 'value'),
   Input('avg_or_act', 'value')])
 
def graphs(color_toggle, sub, avg_or_act):
    return sub_plot(sub, color_toggle), bar_graph(sub), table(sub), threedee(avg_or_act)
 
if __name__ == '__main__':
   app.run_server(debug=True)
 
 
 

