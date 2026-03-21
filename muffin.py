import pandas as pd

df = pd.read_csv('bakery_sales_revised.csv')

muffin = df[df['Item'] == 'Muffin'].copy()

muffin['date_time'] = pd.to_datetime(muffin['date_time'])

muffin['Date'] = muffin['date_time'].dt.date

daily_muffin = muffin.groupby('Date').size().reset_index(name='Muffin Sales')

print(daily_muffin.head(10))