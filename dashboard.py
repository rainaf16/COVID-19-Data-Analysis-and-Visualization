import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Data Collection
data_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
df = pd.read_csv(data_url)
df.fillna(method='ffill', inplace=True)
df['date'] = pd.to_datetime(df['date'])

# Filter data for a specific country (e.g., Malaysia)
country = 'Malaysia'
df_country = df[df['location'] == country]

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='cases-graph'),
    dcc.Slider(
        id='date-slider',
        min=0,
        max=len(df_country)-1,
        value=0,
        marks={i: str(date) for i, date in enumerate(df_country['date'].dt.strftime('%Y-%m-%d').unique())},
        step=None
    )
])

@app.callback(
    Output('cases-graph', 'figure'),
    Input('date-slider', 'value')
)
def update_figure(selected_date):
    filtered_df = df_country.iloc[:selected_date+1]
    fig = px.line(filtered_df, x='date', y='new_cases', title=f'COVID-19 New Cases in {country}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
