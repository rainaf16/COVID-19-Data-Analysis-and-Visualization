import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Data Collection
data_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
df = pd.read_csv(data_url)

# Data Cleaning
df.fillna(method='ffill', inplace=True)
df['date'] = pd.to_datetime(df['date'])

# Exploratory Data Analysis


print("Descriptive Statistics:")
print(df.describe())

# Time series analysis for a specific country (e.g. Malaysia)
country = 'Malaysia'
df_country = df[df['location'] == country]

plt.figure(figsize=(10, 5))
plt.plot(df_country['date'], df_country['new_cases'], label='New Cases')
plt.plot(df_country['date'], df_country['new_deaths'], label='New Deaths')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title(f'COVID-19 New Cases and Deaths in {country}')
plt.legend()
plt.show()

# Geographic distribution 
world_data = df.groupby('location')['total_cases'].max().reset_index()

plt.figure(figsize=(15, 10))
world_pivot = world_data.pivot_table(values='total_cases', index='location', aggfunc='sum')
sns.heatmap(world_pivot, annot=True, fmt="g", cmap='viridis')
plt.title('Total COVID-19 Cases by Country')
plt.show()


# Line plot for trends over time
fig = px.line(df_country, x='date', y='new_cases', title=f'COVID-19 New Cases in {country}')
fig.show()

# Bar chart for total cases comparison
fig = px.bar(world_data, x='location', y='total_cases', title='Total COVID-19 Cases by Country')
fig.show()
