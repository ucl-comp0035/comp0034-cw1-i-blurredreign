from pathlib import Path
import pandas as pd
BRENTDAILY_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'df_brent_daily_cleaned.csv')
cols=['Date','Price']
yearlist=[]
df_brentdaily = pd.read_csv(BRENTDAILY_DATA_FILEPATH, usecols=cols)
for i in df_brentdaily.loc[:,"Date"]:
    yearlist.append(i)

test=yearlist[0].split("-")

years=[]
for i in range(len(yearlist)):
    splitlist=yearlist[i].split("-")
    years.append(str(splitlist[0]))

years=[*set(years)]
print(years)
years.sort(key=int)
print(years)
x=df_brentdaily[df_brentdaily["Date"].str.contains("2002")==True]
