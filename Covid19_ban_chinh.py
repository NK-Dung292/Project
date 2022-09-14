import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
df1 = pd.read_csv('G:/COVID 19/country_wise_latest.csv')
df2 = pd.read_csv('G:/COVID 19/covid_19_clean_complete.csv')
df3 = pd.read_csv('G:/COVID 19/day_wise.csv')
df4 = pd.read_csv('G:/COVID 19/full_grouped.csv')
df5 = pd.read_csv('G:/COVID 19/usa_county_wise.csv')
df6 = pd.read_csv('G:/COVID 19/worldometer_data.csv',dtype={'Population':str,'TotalRecovered':str,'ActiveCases':str,'TotalTests':str})

#_____________ Top 10 Countries of Most Active Cases" _____________________________________ 
df_Most_Active_Cases = df1[['Country/Region','Active']].sort_values(by=['Active'],ascending=False).head(10)
df1.info()
df_Most_Active_Cases.plot(rot=12,x="Country/Region", y="Active", color='green', kind="bar", 
                          figsize=(12,8),title ="Top 10 Countries of Most Active Cases")
plt.show()

#_____________ Top 10 Countries of Deaths Cases __________________________________________
df_Deaths_Cases = df1[['Country/Region','Deaths']].sort_values(by=['Deaths'],ascending=False).head(10)
df_Deaths_Cases.plot(rot=12,x="Country/Region", y="Deaths", color='red', kind="bar", 
                     figsize=(12, 8),title ="Top 10 Countries of Deaths Cases")
plt.show()

#_____________ Top 10 Countries of Recovered Case _______________________________________
df_Recovered_Cases = df1[['Country/Region','Recovered']].sort_values(by=['Recovered'],ascending=False).head(10)
df_Recovered_Cases.plot(rot=12,x="Country/Region", y="Recovered", color='blue', kind="bar", 
                        figsize=(9, 8),title ="Top 10 Countries of Recovered Cases")
plt.show()

#_____________ Countries in WHO Region _______________________________________________________
df_area = df1.groupby(['WHO Region'])[['Country/Region']].count() 
df_area.set_axis(['Total Countries'], axis= 'columns',inplace=True) 
df_area = df_area.sort_values(['Total Countries'], ascending=False)
plot = df_area.plot.pie(y='Total Countries',autopct='%1.0f%%', figsize=(15, 12))

#_____________ Total Cases Active, Deaths, Recovered _________________________________________
df_WHO_Region = df1.groupby(['WHO Region'])[['Active','Deaths','Recovered']].sum()
df_WHO_Region.sort_values(['Active'], ascending=False, inplace=True)
df_WHO_Region.plot.bar(rot=0,figsize = (15,12),title ="Total Cases Active, Deaths, Recovered",color={"Active": "green", "Deaths": "red","Recovered":"blue"})

#______________ Stats of new cases of covid in 2020 __________________________________________
df3['Date'] = pd.to_datetime(df3['Date'])
df3['Month'] = df3['Date'].dt.month
df_Covid_Cases = df3.groupby(['Month'])[['New cases','New deaths','New recovered']].sum()
df_Covid_Cases.set_axis(['Active', 'Deaths', 'Recovered'],axis = 'columns',inplace=True)
df_Covid_Cases = df_Covid_Cases.sort_values('Active',ascending=False)
lines = df_Covid_Cases.plot.line(rot=0,figsize = (9,8),title ="Stats of new cases of covid in 2020",color={"Active": "green", "Deaths": "red","Recovered":"blue"})

#______________________ total cases in Europe and Asia __________________________
df_tongsoca = df6.groupby('Continent').sum()['TotalCases'].reset_index()
df_Europe = df_tongsoca[df_tongsoca.Continent == 'Europe']
df_Asia = df_tongsoca[df_tongsoca.Continent == 'Asia']
df_tongsoca.plot(rot=12,x="Continent", y="TotalCases", color='green', kind="bar", 
                          figsize=(12,8),title ="Total cases in Europe and Asia")
plt.show()

#_____________________ Where is the population highest and the percent of total cases/population
df6['Population'] = df6['Population'].fillna(0) 
df6 = df6.astype({'Population': 'int32'}) 
df_Population = df6.groupby(['Continent']).sum()['Population'] 
df6['Percent'] = (df6['TotalCases']/df6['Population'])*100 # what percent of population infected with covid 19
df_Percent = df6[['Continent','Population','TotalCases','Percent']].sort_values('Percent',ascending = False)
df_Percent = df_Percent.groupby(['Continent'])[['Percent']].sum()
ax = df_Percent.plot.barh(rot=0,figsize = (15,12),title ="Percent")

#______________________ Percent of Deaths  _______________________________________________
df6['Death']=(df6['TotalDeaths']/df6['TotalCases'])*100 # Percent of Deaths 
df6['Continent'] = df6['Continent'].fillna(0)
df6 = df6.drop([156])
df_Death = df6[['Continent','Death']]
df_Death = df_Death.groupby(['Continent'])[['Death']].sum()
ax = df_Death.plot.barh(rot=0,figsize = (15,12),title ="Percent of Deaths")












