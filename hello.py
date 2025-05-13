import pandas as pd
import plotly.express as px
import pandas as pd
import plotly.express as px
from preswald import connect, get_df, query, table, text, plotly

connect()
df = get_df("data/Fruit-Prices-2022.csv")

sql = "SELECT * FROM my_dataset WHERE RetailPrice > 2.0"
filtered_df = query(sql, "data/Fruit-Prices-2022.csv")

text("# Fruit Prices Analysis")
text("This app displays fruit price data.")
table(df, title="Original Fruit Prices Data")
table(filtered_df, title="Fruits with Retail Price Greater Than $2.00")

fig = px.scatter(df, x='RetailPrice', y='CupEquivalentPrice', text='Fruit',
                 title='Retail Price vs. Cup Equivalent Price',
                 labels={'RetailPrice': 'Retail Price (per pound)',
                         'CupEquivalentPrice': 'Price per Cup Equivalent'})

fig.update_traces(textposition='top center', marker=dict(size=12, color='lightcoral'))
fig.update_layout(template='plotly_white')

plotly(fig)

fig_form = px.bar(df, x='Fruit', y='RetailPrice', color='Form',
                  title='Retail Price by Fruit and Form',
                  labels={'RetailPrice': 'Retail Price (per pound)'})
plotly(fig_form)