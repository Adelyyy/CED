import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('C:/Users/Adel/Desktop/lastcount-NAICS31.csv')
df1=pd.DataFrame(df)
df11 = pd.read_csv('C:/Users/Adel/Desktop/NAICS2 with Graphs - Copy.csv')
aaa = pd.read_csv('C:/Users/Adel/Desktop/WordCounts 222.csv')

trace_foodMan=go.Scatter(x=df1['Year'],
                         y=df1['Food Manufacturing'],
                         name='Food Manufacturing',
                         line=dict(color='#fc0303'))
trace_crop=go.Scatter(x=df1['Year'],
                         y=df1['Crop Production'],
                         name='Crop Production',
                         line=dict(color='#00FFFF'))
trace_bev=go.Scatter(x=df1['Year'],
                         y=df1['Beverage and Tobacco Product Manufacturing'],
                         name='Beverage and Tobacco Product Manufacturing',
                         line=dict(color='#0000A0'))
trace_fish=go.Scatter(x=df1['Year'],
                         y=df1['Fishing, Hunting and Trapping'],
                         name='Fishing, Hunting and_Trapping',
                         line=dict(color='#ADD8E6'))
trace_animal=go.Scatter(x=df1['Year'],
                         y=df1['Animal Production and Aquaculture'],
                         name='Animal Production and Aquaculture',
                         line=dict(color='#0000FF'))
trace_wood=go.Scatter(x=df1['Year'],
                         y=df1['Wood Product Manufacturing'],
                         name='Wood Product Manufacturing',
                         line=dict(color='#ADD8E6'))
trace_comp=go.Scatter(x=df1['Year'],
                         y=df1['Computer and Electronic Product Manufacturing'],
                         name='Computer and Electronic Product Manufacturing',
                         line=dict(color='#800080'))
trace_support=go.Scatter(x=df1['Year'],
                         y=df1['Support Activities for Agriculture and Forestry'],
                         name='Support Activities for Agriculture and Forestry',
                         line=dict(color='#FFFF00'))
trace_Oil=go.Scatter(x=df1['Year'],
                         y=df1['Oil and Gas Extraction'],
                         name='Oil and Gas Extraction',
                         line=dict(color='#00FF00'))
trace_Construction=go.Scatter(x=df1['Year'],
                         y=df1['Construction of Buildings'],
                         name='Construction of Buildings',
                         line=dict(color='#FF00FF'))
trace_nonmetal=go.Scatter(x=df1['Year'],
                         y=df1['Nonmetallic Mineral Product Manufacturing'],
                         name='Nonmetallic Mineral Product Manufacturing',
                         line=dict(color='#FF0000'))
trace_mining=go.Scatter(x=df1['Year'],
                         y=df1['Support Activities for Mining'],
                         name='Support Activities for Mining',
                         line=dict(color='#FF0000'))
trace_util=go.Scatter(x=df1['Year'],
                         y=df1['Utilities'],
                         name='Utilities',
                         line=dict(color='#FF0000'))
trace_heavy=go.Scatter(x=df1['Year'],
                         y=df1['Heavy and Civil Engineering Construction'],
                         name='Heavy and Civil Engineering Construction',
                         line=dict(color='#FFFFFF'))
trace_petro=go.Scatter(x=df1['Year'],
                         y=df1['Petroleum and Coal Products Manufacturing'],
                         name='Petroleum and Coal Products Manufacturing',
                         line=dict(color='#C0C0C0'))
trace_mine=go.Scatter(x=df1['Year'],
                         y=df1['Mining_"except Oil and Gas"'],
                         name='Mining_"except Oil and Gas"',
                         line=dict(color='#808080'))
trace_trade=go.Scatter(x=df1['Year'],
                         y=df1['Specialty Trade Contractors'],
                         name='Specialty Trade Contractors',
                         line=dict(color='#000000'))
trace_Electrical=go.Scatter(x=df1['Year'],
                         y=df1['Electrical Equipment, Appliance, and Component Manufacturing'],
                         name='Electrical Equipment, Appliance, and Component Manufacturing',
                         line=dict(color='#FFA500'))
trace_Chemical=go.Scatter(x=df1['Year'],
                         y=df1['Chemical Manufacturing'],
                         name='Chemical Manufacturing',
                         line=dict(color='#A52A2A'))
trace_text=go.Scatter(x=df1['Year'],
                         y=df1['Textile Mills'],
                         name='Textile Mills',
                         line=dict(color='#800000'))
trace_Apparel=go.Scatter(x=df1['Year'],
                         y=df1['Apparel Manufacturing'],
                         name='Apparel Manufacturing',
                         line=dict(color='#008000'))
trace_Leather=go.Scatter(x=df1['Year'],
                         y=df1['Leather and Allied Product Manufacturing'],
                         name='Leather and Allied Product Manufacturing',
                         line=dict(color='#808000'))
trace_trans=go.Scatter(x=df1['Year'],
                         y=df1['Transportation Equipment Manufacturing'],
                         name='Transportation Equipment Manufacturing',
                         line=dict(color='#728C00'))
trace_print=go.Scatter(x=df1['Year'],
                         y=df1['Printing and Related Support Activities'],
                         name='Printing and Related Support Activities',
                         line=dict(color='#C2DC50'))
trace_plastic=go.Scatter(x=df1['Year'],
                         y=df1['Plastics and Rubber Products Manufacturing'],
                         name='Plastics and Rubber Products Manufacturing',
                         line=dict(color='#694FDB'))
trace_Primary=go.Scatter(x=df1['Year'],
                         y=df1['Primary Metal Manufacturing'],
                         name='Primary Metal Manufacturing',
                         line=dict(color='#FFFFA0'))
trace_fabric=go.Scatter(x=df1['Year'],
                         y=df1['Fabricated Metal Product Manufacturing'],
                         name='Fabricated Metal Product Manufacturing',
                         line=dict(color='#FFA1FF'))
trace_machine=go.Scatter(x=df1['Year'],
                         y=df1['Machinery Manufacturing'],
                         name='Machinery Manufacturing',
                         line=dict(color='#CD6FCD'))
trace_furniture=go.Scatter(x=df1['Year'],
                         y=df1['Furniture and Related Product Manufacturing'],
                         name='Furniture and Related Product Manufacturing',
                         line=dict(color='#6ECC6E'))
trace_Miscellaneous=go.Scatter(x=df1['Year'],
                         y=df1['Miscellaneous Manufacturing'],
                         name='Miscellaneous Manufacturing',
                         line=dict(color='#CC6E6E'))
trace_Textile=go.Scatter(x=df1['Year'],
                         y=df1['Textile Product Mills'],
                         name='Textile Product Mills',
                         line=dict(color='#6ECCCC'))
trace_none=go.Scatter(x=[],
                         y=[],
                        line=dict(color='#ffffff'))
data=[trace_animal,trace_Apparel,trace_bev,trace_Chemical,trace_comp,trace_Construction, trace_crop, trace_Electrical,
      trace_fabric, trace_fish, trace_foodMan, trace_furniture, trace_heavy, trace_Leather, trace_machine, trace_Miscellaneous,
      trace_nonmetal, trace_Oil, trace_petro, trace_plastic, trace_Primary, trace_print, trace_support,
      trace_text, trace_Textile, trace_trade, trace_trans,trace_util, trace_wood,trace_mine,trace_mining]
comn_words=[ 'data' , 'water', 	'sensor' ,	 'energy', 	 'computer' , 'fuel' , 'chemical' ,	 'hydrogen' , 'wireless' , 'mobile'	, 'organic' ,
             'local' ,	 'delivery' , 'real time' ,	 'pharmaceutical' 	, 'manufacturing' 	, 'exhaust' 	, 'software', 'database' ,'construction' ,
             'film' , 'pumps' ,	 'terminal' 	, 'industrial' ,	 'video' 	, 'valves' 	, 'travel' 	, 'fuel cell' 	, 'navigation' ,	 'medical' ,
             'battery', 'nuclear' ,	 'magnetic resonance' ,	 'perforating'	, 'mineral' , 'fertilizer' ,	 'alcohol' ,	 'simulation' ,
             'security' ,	 'gps' ,	 'mapping' 	, 'electronics' ,	 'mobile device' ,	 'audio' 	, 'art' 	, 'laser' ,	 'pipes' ,	 'hardware' ,'transportation',
             'lighting' ,	 'maintenance' , 'internet', 'soil' , 'commercial' ,'recycling' ,	'architecture' ,' flow control device' , 'mining',
             'iron' ,	 'infection' , 'solar' 	, 'hospitality' ,	 'windows' ,	 'golf' 	, 'fluid system' 	, 'towing' 	, 'dental' , 'infrastructure' ,
             'consumer' , 'family' ,'data storage' , 'furniture' , 'controllers' ,	 'semiconductor' 	, 'dietary fiber',  'collaboration' ,	 'spectrometer' 	,
             'messaging' ,	 'monitoring system' ,	 'silver' ,	 'compliance' ,	 'fashion' 	, 'autoimmune disease' ,	 'energy storage' ,	 'cycling' ,
             'resins' ,	 'artificial lift' ,	 'process control' 	, 'instrumentation', 'scheduling' ,	 'advertising' , 'pressure measurement' ,
             'accounting' ,	 'credit' ,	 'printing' 	, 'machining' 	, 'power plant' ,	 'rfid' ,	 'gps receivers' 	 'sand control' , 'shipping'
             'peer to peer' ,	 'fluid storage '	, 'hydrochloric acid' ,	 'global positioning system' ,	 'flow distribution' , 'farming' ,	 'diabetes',
             'manure' ,	 'dsp' ,'cooling system ',	 'children' ,	'civil engineering' ,	'machine learning' ,'telecommunications'
             'sports' ,	 'marketing' ,	 'power distribution' ,	 'greenhouse gas', 	 'wind energy' ,'imagery' ,	 'automotive', 	 'sales' ,	'email' ,'geographic information' ,	 'billing',
             'wearable' ,'vanadium' ,	 'pet' ,	 'medical device ',	 'analytics' ,	' medical imaging' 	, 'cooking' 	, 'fuel supply' 	, 'insurance'
             'fertility' 	, 'sleep apnea '	, 'adult' ,	 'wastewater treatment' ,	 'point of sale', 	 'real time monitoring' ,	 'voip' ,	 'soil remediation',
             'water purification' ,	 'residential' , 'screws' ,	 'employment' 	, 'medical devices' ,	 'limestone' 	, 'logging tools',
             'railroad' ,	 'gas compression' ,	 'oil storage' ,	 'privacy' 	 ,'livestock' ,	 'social' 	, 'gas processing']
datadict = {
                   'Food Manufacturing': trace_foodMan,
                   'Crop Production': trace_crop,
                   'Beverage and Tobacco Product Manufacturing': trace_bev ,
                   'Fishing, Hunting and_Trapping': trace_fish,
                   'Animal Production and Aquaculture': trace_Apparel,
                    'Wood Product Manufacturing':  trace_wood,
                    'Computer and Electronic Product Manufacturing': trace_comp,
                    'Support Activities for Agriculture and Forestry': trace_support,
                    'Oil and Gas Extraction' :	trace_Oil,
                    'Nonmetallic Mineral Product Manufacturing': trace_nonmetal,
                    'Support Activities for Mining': trace_mining,
                    'Construction of Buildings': trace_Construction,
                    'Utilities': trace_util,
                    'Heavy and Civil Engineering Construction ': trace_heavy,
                    'Petroleum and Coal Products Manufacturing ': trace_petro,
                    'Mining_"except Oil and Gas"': trace_mine,
                    'Specialty Trade Contractors': trace_trade,
                    'Electrical Equipment, Appliance, and Component Manufacturing': trace_Electrical,
                    'Chemical Manufacturing': trace_Chemical,
                    'Textile Mills': trace_Textile,
                    'Apparel Manufacturing':trace_Apparel,
                    'Leather and Allied Product Manufacturing':trace_Leather,
                    'Transportation Equipment Manufacturing': trace_trans,
                    'Paper Manufacturing': df1['Paper Manufacturing'],
                    'Printing and Related Support Activities': trace_print,
                    'Plastics and Rubber Products Manufacturing': trace_plastic,
                    'Primary Metal Manufacturing': trace_Primary,
                    'Fabricated Metal Product Manufacturing':  trace_fabric,
                    'Machinery Manufacturing': trace_machine,
                    'Furniture and Related Product Manufacturing': trace_furniture,
                    'Miscellaneous Manufacturing': trace_Miscellaneous,
                    'Textile Product Mills': trace_text,
                     'None':trace_none
                    }
layout1=dict(xaxis={'type': 'log', 'title': 'Year'},
            yaxis={'title': 'IPC count'},
            margin={'l': 80, 'b': 50, 't': 120, 'r': 50},
            title='IPC count according to 3-Digit NAICS Code 1997-2017 ',
            legend=dict(x=-0.1, y=1.2),
            hovermode='closest',
            plot_bgcolor='#f2f2f2',
            font=dict(family='Courier New, monospace', size=14, color='#0d0c0c'),
            )
layout2= dict(
    xaxis={'type': 'log', 'title': 'Year'},
    yaxis={'title': 'Word Count'},
    margin={'l': 80, 'b': 50, 't': 70, 'r': 50},
    title='Top 50 Common word of crunch book in 5 general Industries 1997-2017',
    template='ggplot2',
    plot_bgcolor='#f2f2f2',
    font=dict(family='Courier New, monospace', size=14, color='#0d0c0c'),
    hovermode='closest')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div( [html.H1('Inovation In Calgary')]),
    html.Div([
        dcc.Graph(
            id='ipc count',
            figure={
                'data': [
                    go.Scatter(
                        x=df11['Year'],
                        y=df11['Manufacturing'],
                        name= 'Manufacturing',
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.1, 'color': 'black'}
                        },

                    ),
                    go.Scatter(
                        x=df11['Year'],
                        y=df11['Mining, Quarrying, and Oil and Gas Extraction'],
                        name='Mining, Quarrying, and Oil and Gas Extraction',
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.1, 'color': 'black'}
                        },

                    ),
                    go.Scatter(
                        x=df11['Year'],
                        y=df11['Agriculture, Forestry, Fishing_and_Hunting'],
                        name= 'Agriculture, Forestry, Fishing_and_Hunting',
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.1, 'color': 'black'}
                        },

                    ),
                    go.Scatter(
                        x=df11['Year'],
                        y=df11['Utilities'],
                        name='Utilities',
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.1, 'color': 'black'}
                        },

                    ),
                    go.Scatter(
                        x=df11['Year'],
                        y=df11['Construction'],
                        name='Construction',
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.1, 'color': 'black'}
                        },

                    )
                ],
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'Year'},
                    yaxis={'title': 'IPC count'},
                    margin={'l': 80, 'b': 30, 't': 30, 'r': 50},
                    title='IPC Count In 5 general Industries 1997-2017',
                    template='seaborn',
                    font=dict(family='Courier New, monospace', size=14, color='#0d0c0c'),
                    hovermode='closest'
                  )
            },style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}
        )
        ]),

    html.Div([
        html.Label('Choose an industry: '),
    html.Div([
            dcc.Dropdown(id='input_value1',
                         options=[{'label': s , 'value': s} for s in datadict.keys()] ,
                         value='Food Manufacturing'
                     )],style={'width':'50%', 'margin':10, 'textAlign': 'center'}),
    html.Div([
            dcc.Dropdown(id='input_value2',
                         options=[{'label': s, 'value': s} for s in datadict.keys()],
                         value='Crop Production'
                         )],style={'width':'50%', 'margin':10 ,'textAlign': 'center'})
        ]),

    html.Div([
        dcc.Graph(
            id='IPC count'

        )
    ], style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        html.Label('Choose a keyword: ')]),
    html.Div(
       [
           dcc.Dropdown(id='input_value3',
                        options=[{'label': e, 'value': e} for e in comn_words],
                        value='data'
                        )],style={'width':'50%', 'margin':10, 'textAlign': 'center'}),

   html.Div([
       dcc.Graph(
           id='word_count',
           figure={ }
                  )
       ],
             style={'width': '100%', 'margin': 10, 'textAlign': 'center'})
        ] )

@app.callback(
    dash.dependencies.Output('IPC count', 'figure'),
           [dash.dependencies.Input('input_value1','value'),
         dash.dependencies.Input('input_value2','value')
         ])

def update_figure(input_value1, input_value2):
    figa = []
    figb= []
    i = datadict[input_value1]
    figa.append(i)
    figb = figa
    t=datadict[input_value2]
    figb.append(t)

    return {'data': figb,
            'layout':layout1
            }

@app.callback(
    dash.dependencies.Output('word_count', 'figure'),
    [dash.dependencies.Input('input_value3','value')])
def update_figure(input_value3):
    fig1 = aaa[input_value3]
    fig2=[ go.Scatter(
                        x=aaa['year'],
                        y=fig1,
                        name= input_value3,
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.1, 'color': 'black'}
                        })]
    fig3=fig2


    return {

                'data': fig3,
                'layout': layout2


            }

if __name__ == '__main__':
    app.run_server(debug=True)