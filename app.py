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
cols = ['Date', 'Price']



line_brent_daily = px.line(df_brent_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                          template="simple_white"
                          )
line_brent_monthly=px.line(df_brent_monthly,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          template="simple_white"
                          )
line_natgas_daily=px.line(df_natgas_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''} ,
                          template="simple_white"
                          )
line_natgas_monthly=px.line(df_natgas_monthly,
                          x='Month',
                          y='Price',
                          labels={'Month': '', 'Price': ''},
                          template="simple_white"
                          )
line_wti_daily=px.line(df_wti_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          template="simple_white"
                          )
line_wti_monthly=px.line(df_wti_monthly,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          template="simple_white"
                          )

def yearlist_func(dataframe):
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
natgasyears=yearlist_func(df_natgas_daily)
wtiyears=yearlist_func(df_wti_daily)

app = Dash(__name__, 
external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)
app.layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Oil and Gas Prices'),
    html.P('View graphs representing the price of Brent, Natural Gas and WTI over time.',
           className='lead'),
    html.Br(),

    ## BRENT ##
    html.H2('Europe Brent Spot Price FOB (Dollars per Barrel)'),
    html.Br(),
    dbc.Row([
        # Brent Daily row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select1",
             options=[{"label": x, "value": x} for x in brentyears],
             value=""),
        ]),
        # Brent Daily GRAPH
        dbc.Col(width=9, children=[
            html.H2('Brent Daily'),
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
             value=""),
        ]),
        # Brent Monthly graph
        dbc.Col(width=9, children=[
            html.H2('Brent Monthly'),
            dcc.Graph(id='brent-monthly', figure=line_brent_monthly),
        ]),
    ]),


    ## NATURAL GAS ##
    html.H2('Europe Natural Gas Spot Price FOB (Dollars per Barrel)'),
    html.Br(),
    dbc.Row([
        # Natgas Daily row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select3",
             options=[{"label": x, "value": x} for x in natgasyears],
             value=""),
        ]),
        # Natgas Daily GRAPH
        dbc.Col(width=9, children=[
            html.H2('Natural Gas Daily'),
            dcc.Graph(id='natgas-daily', figure=line_natgas_daily),
        ]),
    ]),
    html.Br(),
    dbc.Row([
        # Natgas Monthly row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select4",
             options=[{"label": x, "value": x} for x in natgasyears],
             value=""),
        ]),
        # Natgas Monthly GRAPH
        dbc.Col(width=9, children=[
            html.H2('Natural Gas Monthly'),
            dcc.Graph(id='natgas-monthly', figure=line_natgas_monthly),
        ]),
    ]),


## WTI ##
    html.H2('Europe WTI Spot Price FOB (Dollars per Barrel)'),
    html.Br(),
    dbc.Row([
        # WTI Daily row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select5",
             options=[{"label": x, "value": x} for x in wtiyears],
             value=""),
        ]),
        # WTI Daily GRAPH
        dbc.Col(width=9, children=[
            html.H2('WTI Daily'),
            dcc.Graph(id='wti-daily', figure=line_wti_daily),
        ]),
    ]),
    html.Br(),
    dbc.Row([
        # WTI Monthly row
        dbc.Col(width=3, children=[
            html.H4("Select Date"),
            dcc.Dropdown(id="year-select6",
             options=[{"label": x, "value": x} for x in wtiyears],
             value=""),
        ]),
        # WTI Monthly GRAPH
        dbc.Col(width=9, children=[
            html.H2('WTI Monthly'),
            dcc.Graph(id='wti-monthly', figure=line_wti_monthly),
        ]),
    ]),


])

## BRENT
@app.callback(
    Output("brent-daily", "figure"),
    Input("year-select1", "value")
    )
def update_recycling_chart(year_select1):
    try:
        df_brent_daily_copy=df_brent_daily
        df_brent_daily_copy=df_brent_daily_copy[df_brent_daily_copy["Date"].str.contains(year_select1)==True]
        line_brent_daily= px.line(df_brent_daily_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            template="simple_white"
                            )
    except TypeError:
        line_brent_daily=px.line(df_brent_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                          template="simple_white"
                          )
    return line_brent_daily

@app.callback(
    Output("brent-monthly", "figure"),
    Input("year-select2", "value")
    )
def update_recycling_chart(year_select2):
    try:
        df_brent_monthly_copy=df_brent_monthly
        df_brent_monthly_copy=df_brent_monthly_copy[df_brent_monthly_copy["Date"].str.contains(year_select2)==True]
        line_brent_monthly= px.line(df_brent_monthly_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            template="simple_white"
                            )
    except TypeError:
        line_brent_monthly=px.line(df_brent_monthly,
                          x='Date',
                          y='Price',
                          labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                          template="simple_white"
                          )
    return line_brent_monthly


## NATURAL GAS
@app.callback(
    Output("natgas-daily", "figure"),
    Input("year-select3", "value")
    )
def update_recycling_chart(year_select3):
    try:
        df_natgas_daily_copy=df_natgas_daily
        df_natgas_daily_copy=df_natgas_daily_copy[df_natgas_daily_copy["Date"].str.contains(year_select3)==True]
        line_natgas_daily= px.line(df_natgas_daily_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            template="simple_white"
                            )
    except TypeError:
        line_natgas_daily=px.line(df_natgas_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                          template="simple_white"
                          )
    return line_natgas_daily

@app.callback(
    Output("natgas-monthly", "figure"),
    Input("year-select4", "value")
    )
def update_recycling_chart(year_select4):
    try:
        df_natgas_monthly_copy=df_natgas_monthly
        df_natgas_monthly_copy=df_natgas_monthly_copy[df_natgas_monthly_copy["Month"].str.contains(year_select4)==True]
        line_natgas_monthly= px.line(df_natgas_monthly_copy,
                            x='Month',
                            y='Price',
                            labels={'Month': 'Year', 'Price': 'Dollars per Barrel'},
                            template="simple_white"
                            )
    except TypeError:
        line_natgas_monthly=px.line(df_natgas_monthly,
                          x='Month',
                          y='Price',
                          labels={'Month': 'Year', 'Price': 'Dollars per Barrel'},
                          template="simple_white"
                          )
    return line_natgas_monthly

## WTI

## NATURAL GAS
@app.callback(
    Output("wti-daily", "figure"),
    Input("year-select5", "value")
    )
def update_recycling_chart(year_select3):
    try:
        df_wti_daily_copy=df_wti_daily
        df_wti_daily_copy=df_wti_daily_copy[df_wti_daily_copy["Date"].str.contains(year_select3)==True]
        line_wti_daily= px.line(df_wti_daily_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            template="simple_white"
                            )
    except TypeError:
        line_wti_daily=px.line(df_wti_daily,
                          x='Date',
                          y='Price',
                          labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                          template="simple_white"
                          )
    return line_wti_daily

@app.callback(
    Output("wti-monthly", "figure"),
    Input("year-select6", "value")
    )
def update_recycling_chart(year_select4):
    try:
        df_wti_monthly_copy=df_wti_monthly
        df_wti_monthly_copy=df_wti_monthly_copy[df_wti_monthly_copy["Date"].str.contains(year_select4)==True]
        line_wti_monthly= px.line(df_wti_monthly_copy,
                            x='Date',
                            y='Price',
                            labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                            template="simple_white"
                            )
    except TypeError:
        line_wti_monthly=px.line(df_wti_monthly,
                          x='Date',
                          y='Price',
                          labels={'Date': 'Year', 'Price': 'Dollars per Barrel'},
                          template="simple_white"
                          )
    return line_wti_monthly


if __name__ == '__main__':
    app.run_server(debug=True)