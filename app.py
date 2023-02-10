from pathlib import Path

from dash import Dash, html, dcc
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

cols = ['Date', 'Price']
df_brentdaily = pd.read_csv(BRENTDAILY_DATA_FILEPATH, usecols=cols)
df_brentmonthly = pd.read_csv(BRENTMONTHLY_DATA_FILEPATH, usecols=cols)
df_natgasdaily = pd.read_csv(NATGASDAILY_DATA_FILEPATH, usecols=cols)
df_natgasmonthly= pd.read_csv(NATGASMONTHLY_DATA_FILEPATH, usecols=['Month', 'Price'])
df_wtidaily = pd.read_csv(WTIDAILY_DATA_FILEPATH, usecols=cols)
df_wtimonthly = pd.read_csv(WTIMONTHLY_DATA_FILEPATH, usecols=cols)

line_brent_daily = px.line(df_brentdaily,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          template="simple_white"
                          )
line_brent_monthly=px.line(df_brentmonthly,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          template="simple_white"
                          )
line_natgas_daily=px.line(df_natgasdaily,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''} ,
                          template="simple_white"
                          )
line_natgas_monthly=px.line(df_natgasmonthly,
                          x='Month',
                          y='Price',
                          labels={'Month': '', 'Price': ''},
                          template="simple_white"
                          )
line_wti_daily=px.line(df_wtidaily,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          template="simple_white"
                          )
line_wti_monthly=px.line(df_wtimonthly,
                          x='Date',
                          y='Price',
                          labels={'Date': '', 'Price': ''},
                          template="simple_white"
                          )
app = Dash(__name__, 
external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

app.layout = dbc.Container(
    [
        html.H1("Oil and Gas Prices"),
        html.H2("Do the monthly and daily graphs follow similar trends?"),
        dcc.Graph(
            id='line_brent_daily',
            figure=line_brent_daily
        ),
        dcc.Graph(
            id='line_brent_monthly',
            figure=line_brent_monthly
        )
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)