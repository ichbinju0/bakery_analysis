import pandas as pd
df = pd.read_csv('bakery_sales_revised.csv')

muffin = df[df['Item'] == 'Muffin'].copy()
muffin['date_time'] = pd.to_datetime(muffin['date_time'])
muffin['Date'] = muffin['date_time'].dt.date

daily_muffin = muffin.groupby('Date').agg(Actual_Sales=('Item', 'size'), Day_Type = ('weekday_weekend', 'first')).reset_index()

coffee_sales = df[df['Item'] == 'Coffee'].copy()
coffee_sales['Date'] = pd.to_datetime(coffee_sales['date_time']).dt.date
daily_coffee = coffee_sales.groupby('Date').size().reset_index(name='Coffee_Sales')

final = pd.merge(daily_muffin, daily_coffee, on='Date', how='left').fillna(0)
final.to_csv('muffin_coffee_sales.csv', index=False)

print("완료")