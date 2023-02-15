from pathlib import Path

from dash import Dash, html, dcc, Input,Output
import dash_bootstrap_components as dbc
from pathlib import Path
import pandas as pd
import plotly.express as px
#-------
# Charts
#-------
BRENTDAILY_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'df_brent_daily_cleaned.csv')
BRENTMONTHLY_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'df_brent_monthly_cleaned.csv')
NATGASDAILY_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'df_natgas_daily_cleaned.csv')
NATGASMONTHLY_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'df_natgas_monthly_cleaned.csv')
WTIDAILY_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'df_wti_daily_cleaned.csv')
WTIMONTHLY_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'df_wti_monthly_cleaned.csv')
cols=['Date','Price']
df_brent_daily = pd.read_csv(BRENTDAILY_DATA_FILEPATH, usecols=cols)
df_brent_monthly = pd.read_csv(BRENTMONTHLY_DATA_FILEPATH, usecols=cols)
df_natgas_daily = pd.read_csv(NATGASDAILY_DATA_FILEPATH, usecols=cols)
df_natgas_monthly= pd.read_csv(NATGASMONTHLY_DATA_FILEPATH, usecols=['Month', 'Price'])
df_wti_daily = pd.read_csv(WTIDAILY_DATA_FILEPATH, usecols=cols)
df_wti_monthly = pd.read_csv(WTIMONTHLY_DATA_FILEPATH, usecols=cols)


line_brent_daily = px.line(df_brent_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                          )
line_brent_monthly=px.line(df_brent_monthly,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          )
line_natgas_daily=px.line(df_natgas_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''} ,
                          )
line_natgas_monthly=px.line(df_natgas_monthly,
                          x='Month',
                          y='Price',
                          labels={'Month': '', 'Price': ''},
                          )
line_wti_daily=px.line(df_wti_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          )
line_wti_monthly=px.line(df_wti_monthly,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          )

def yearlist_func(dataframe):
    # When the function is called, the function returns a list containing each year found in the Dates column of the input dataframe.

    yearlist=[]
    for i in dataframe.loc[:,"Date"]:
        yearlist.append(i)
    
    years=[]
    for i in range(len(yearlist)):
        splitlist=yearlist[i].split("-")
        years.append(str(splitlist[0]))
    years=[*set(years)] # set removes duplicate values, leaving us with a list of all years
    years.sort(key=int)
    return years

brentyears=yearlist_func(df_brent_daily)
brentyears.insert(0,str("All"))
natgasyears=yearlist_func(df_natgas_daily)
natgasyears.insert(0,str("All"))
wtiyears=yearlist_func(df_wti_daily)
wtiyears.insert(0,str("All"))

graphs=[str("Line"),str("Bar")]

#-------
# Dash app
#-------
app = Dash(__name__, 
external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Oil and Gas Prices'),
    html.P('View graphs representing the price of Brent, Natural Gas and WTI over time.',className='lead'),
    html.Br(),

    ## BRENT ##

    html.H2("Oil Prices"),
    html.Br(),
    html.P('Europe Brent and WTI (Western Texas Intermediate) Spot Prices (Daily/Monthly) from EIA U.S. (Energy Information Administration).',className='lead'),
    html.Br(),
    html.H3('Europe Brent Spot Price FOB (Dollars per Barrel)'),
    html.Br(),
    dbc.Row([
        # Brent Daily row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select1",
             options=[{"label": x, "value": x} for x in brentyears],
             value="All",
             clearable=False),
            html.Br(),
            html.H4("Select Graph Type"),
            dcc.Dropdown(id="graph-select1",
             options=[{"label": x, "value": x} for x in graphs],
             value="Line",
             clearable=False),
             
        ]),
        # Brent Daily GRAPH
        dbc.Col(width=9, children=[
            html.H4('Brent Daily'),
            dcc.Graph(id='brent-daily', figure=line_brent_daily),
        ]),
    ]),
    html.Br(),
    dbc.Row([
        # Brent Monthly row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select2",
             options=[{"label": x, "value": x} for x in brentyears],
             value="All",
             clearable=False
            ),
            html.Br(),
            html.H4("Select Graph Type"),
            dcc.Dropdown(id="graph-select2",
             options=[{"label": x, "value": x} for x in graphs],
             value="Line",
             clearable=False),
        ]),
        # Brent Monthly graph
        dbc.Col(width=9, children=[
            html.H4('Brent Monthly'),
            dcc.Graph(id='brent-monthly', figure=line_brent_monthly),
        ]),
    ]),

## WTI ##
    html.Br(),
    html.H3('WTI Spot Price FOB (Dollars per Barrel)'),
    html.Br(),
    dbc.Row([
        # WTI Daily row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select3",
             options=[{"label": x, "value": x} for x in wtiyears],
             value="All",
             clearable=False
             ),
            html.Br(),
            html.H4("Select Graph Type"),
            dcc.Dropdown(id="graph-select3",
             options=[{"label": x, "value": x} for x in graphs],
             value="Line",
             clearable=False),
        ]),
        # WTI Daily GRAPH
        dbc.Col(width=9, children=[
            html.H4('WTI Daily'),
            dcc.Graph(id='wti-daily', figure=line_wti_daily),
        ]),
    ]),
    html.Br(),
    dbc.Row([
        # WTI Monthly row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select4",
             options=[{"label": x, "value": x} for x in wtiyears],
             value="All",
             clearable=False
            ),
            html.Br(),
            html.H4("Select Graph Type"),
            dcc.Dropdown(id="graph-select4",
             options=[{"label": x, "value": x} for x in graphs],
             value="Line",
             clearable=False),
        ]),
        # WTI Monthly GRAPH
        dbc.Col(width=9, children=[
            html.H4('WTI Monthly'),
            dcc.Graph(id='wti-monthly', figure=line_wti_monthly),
        ]),
    ]),

## NATURAL GAS ##
    html.Br(),
    html.H2('Gas Prices'),
    html.P('Major Natural Gas Prices including US Henry Hub (Monthly/Daily). Prices are in nominal dollars. Data comes from EIA U.S. (Energy Information Administration).',className='lead'),
    html.Br(),
    html.H3(' Natural Gas Price (Dollars)'),
    html.Br(),
    dbc.Row([
        # Natgas Daily row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select5",
             options=[{"label": x, "value": x} for x in natgasyears],
             value="All",
             clearable=False
            ),
            html.Br(),
            html.H4("Select Graph Type"),
            dcc.Dropdown(id="graph-select5",
             options=[{"label": x, "value": x} for x in graphs],
             value="Line",
             clearable=False),
        ]),
        # Natgas Daily GRAPH
        dbc.Col(width=9, children=[
            html.H4('Natural Gas Daily'),
            dcc.Graph(id='natgas-daily', figure=line_natgas_daily),
        ]),
    ]),
    html.Br(),
    dbc.Row([
        # Natgas Monthly row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select6",
             options=[{"label": x, "value": x} for x in natgasyears],
             value="All",
             clearable=False
             ),
            html.Br(),
            html.H4("Select Graph Type"),
            dcc.Dropdown(id="graph-select6",
             options=[{"label": x, "value": x} for x in graphs],
             value="Line",
             clearable=False),
        ]),
        # Natgas Monthly GRAPH
        dbc.Col(width=9, children=[
            html.H4('Natural Gas Monthly'),
            dcc.Graph(id='natgas-monthly', figure=line_natgas_monthly),
        ]),
    ]),

])

## BRENT
@app.callback(
    Output("brent-daily", "figure"),
    Input("year-select1", "value"),
    Input("graph-select1","value")
    )
def update_brentdaily_chart(year_select1,graph_select1):
    
    df_brent_daily_copy=df_brent_daily
    if year_select1 !="All":
        df_brent_daily_copy=df_brent_daily_copy[df_brent_daily_copy["Date"].str.contains(year_select1)==True] # Searches dataframe for entries with the corresponding year
    if graph_select1=="Line":
        line_brent_daily= px.line(df_brent_daily_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            markers=True
                            )
    if graph_select1=="Bar":
        line_brent_daily=px.bar(df_brent_daily_copy,
                        x='Date',
                        y='Price',
                        color_discrete_sequence=['black']
                        )
    return line_brent_daily

@app.callback(
    Output("brent-monthly", "figure"),
    Input("year-select2", "value"),
    Input("graph-select2","value")
    )
def update_brentmonthly_chart(year_select2,graph_select2):
    df_brent_monthly_copy=df_brent_monthly
    if year_select2 !="All":
        df_brent_monthly_copy=df_brent_monthly_copy[df_brent_monthly_copy["Date"].str.contains(year_select2)==True]# Searches dataframe for entries with the corresponding year
    if graph_select2=="Line":
        line_brent_monthly= px.line(df_brent_monthly_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            markers=True
                            )
    if graph_select2=="Bar":
        line_brent_monthly=px.bar(df_brent_monthly_copy,
                        x='Date',
                        y='Price',
                        color_discrete_sequence=['black']
                        )
    return line_brent_monthly

## WTI
@app.callback(
    Output("wti-daily", "figure"),
    Input("year-select3", "value"),
    Input("graph-select3","value")
    )
def update_wtidaily_chart(year_select3,graph_select3):
    df_wti_daily_copy=df_wti_daily
    if year_select3 !="All":
        df_wti_daily_copy=df_wti_daily_copy[df_wti_daily_copy["Date"].str.contains(year_select3)==True]# Searches dataframe for entries with the corresponding year
    if graph_select3=="Line":
        line_wti_daily= px.line(df_wti_daily_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            markers=True
                            )
    if graph_select3=="Bar":
        line_wti_daily=px.bar(df_wti_daily_copy,
                        x='Date',
                        y='Price',
                        color_discrete_sequence=['black']
                        )
    return line_wti_daily

@app.callback(
    Output("wti-monthly", "figure"),
    Input("year-select4", "value"),
    Input("graph-select4","value")
    )
def update_wtimonthly_chart(year_select4,graph_select4):
    df_wti_monthly_copy=df_wti_monthly
    if year_select4 !="All":
        df_wti_monthly_copy=df_wti_monthly_copy[df_wti_monthly_copy["Date"].str.contains(year_select4)==True]# Searches dataframe for entries with the corresponding year
    if graph_select4=="Line":
        line_wti_monthly= px.line(df_wti_monthly_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            markers=True
                            )
    if graph_select4=="Bar":
        line_wti_monthly=px.bar(df_wti_monthly_copy,
                        x='Date',
                        y='Price',
                        color_discrete_sequence=['black']
                        )
    return line_wti_monthly


## NATURAL GAS
@app.callback(
    Output("natgas-daily", "figure"),
    Input("year-select5", "value"),
    Input("graph-select5","value")
    )
def update_natdaily_chart(year_select5,graph_select5):
    df_natgas_daily_copy=df_natgas_daily
    if year_select5 !="All":
        df_natgas_daily_copy=df_natgas_daily_copy[df_natgas_daily_copy["Date"].str.contains(year_select5)==True]# Searches dataframe for entries with the corresponding year
    if graph_select5=="Line":
        line_natgas_daily= px.line(df_natgas_daily_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars / $'},
                            markers=True
                            )
    if graph_select5=="Bar":
        line_natgas_daily=px.bar(df_natgas_daily_copy,
                        x='Date',
                        y='Price',
                        color_discrete_sequence=['black']
                        )
    return line_natgas_daily


@app.callback(
    Output("natgas-monthly", "figure"),
    Input("year-select6", "value"),
    Input("graph-select6","value")
    )
def update_natmonthly_chart(year_select6,graph_select6):
    df_natgas_monthly_copy=df_natgas_monthly
    if year_select6 !="All":
        df_natgas_monthly_copy=df_natgas_monthly_copy[df_natgas_monthly_copy["Month"].str.contains(year_select6)==True]# Searches dataframe for entries with the corresponding year
    if graph_select6=="Line":
        line_natgas_monthly= px.line(df_natgas_monthly_copy,
                            x='Month',
                            y='Price',
                            labels={'Month': 'Year', 'Price': 'Dollars / $'},
                            markers=True
                            )
    if graph_select6=="Bar":
        line_natgas_monthly=px.bar(df_natgas_monthly_copy,
                        x='Month',
                        y='Price',
                        color_discrete_sequence=['black']
                        )
    return line_natgas_monthly


if __name__ == '__main__':
    app.run_server(debug=True)
