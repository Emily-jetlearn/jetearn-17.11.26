import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly # same as matplotlib but with higher graphical standards
import plotly.express as px 
import plotly.graph_objects as go 
from plotly.subplots import make_subplots

covid_dataset = 'data science folder\\covid_data.csv'
data = pd.read_csv(covid_dataset)
print(f'\n Covid Data columns: \n {data.columns} \n')

# selecting specific sets of columns from the original dataset
data = data[["Province_State", "Country_Region", 'Last_Update', 
             'Lat', 'Long_', 'Confirmed', 'Recovered', 'Deaths',
       'Active']]

#renaming columns

data.columns = ('state','Country','lastUpdate', 'Lat','Long', 'Confirmed',
                'Recovered','Deaths', 'Active')

print(f'covid dataset after renaming columns: \n')
print(f'\n{data.head} \n')

data['state'].fillna(value = '',inplace = True) #makes changes to the actual dataset
'''fillna (value) - will fill any missing value (NaN)
in this "State" column with an empty string ('')
'''

#top ten most effected countries
top10_confirmed = pd.DataFrame(data.groupby("Country")['Confirmed'].sum().nlargest(10).sort_values(ascending = False))
print(f'\ntop 10 confirmed most affected countries: \n {top10_confirmed}\n countries \n')

print(f'\n top ten countries:\n {top10_confirmed.index} \n')

#creating plotly, express scatter plot
figure1 = px.scatter(top10_confirmed,x=top10_confirmed.index,
                     y="Confirmed",size="Confirmed",size_max = 120,
                     color = top10_confirmed.index,
                     title= "Top 10 countries by confirmed cases")
figure1.write_html("Fig1.html",auto_open=True)

#top 10 countries with the highest number of deaths

top10_deaths = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest().sort_values(ascending=False))
print(f'\n top 10 countries with highest death toll: \n {top10_deaths}\n')

fig = px.bar(top10_deaths,x = "Deaths" , y = top10_deaths.index, 
             height = 600, color = "Deaths", orientation = 'h',
             color_continuous_scale = ['deepskyblue','yellow'], title = 'Top 10 Deaths Cases worldwide')

fig.write_html("fig.html", auto_open = True)


# top 10 recovered countries

top10_recovered = pd.DataFrame(data.groupby("Country")["Recovered"].sum()
                               .nlargest(10).sort_values(ascending = False))
print(f'\n\ntop 10 countries with the most recovered cases: \n {top10_recovered} \n')

fig3 = px.scatter(top10_recovered, x= top10_recovered.index, 
                       y = "Confirmed", size = "top10_recovered", 
                       color = top10_recovered.index,size_max = 120,
                  title = 'top 10 countries with the most recovered cases')
fig3.write_html("fig3.html", auto_open = True)