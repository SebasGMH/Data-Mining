"""
Covid Data Project
"""
import pandas as pd
import plotly.express as px
covid_df = pd.read_csv('COVID.csv')
#print(covid_df)

deathHospital = covid_df[['HOSPITALIZED_COUNT','DEATH_COUNT']]
#print(deathHospital)
fig = px.scatter(deathHospital, x='HOSPITALIZED_COUNT', y='DEATH_COUNT', 
                 width=350, height=250)
fig.show()