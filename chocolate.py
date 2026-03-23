import pandas as pd

file_path = 'Coffee Shop Sales.xlsx' 

df = pd.read_excel(file_path)
chocolate_df = df[df['product_category'] == 'Drinking Chocolate'].copy()
chocolate_df['transaction_date'] = pd.to_datetime(chocolate_df['transaction_date'])
daily_sales = chocolate_df.groupby('transaction_date')['transaction_qty'].sum().reset_index()
daily_sales.columns = ['Date', 'Actual_Sales']
daily_sales.to_excel('hot_chocolate_final.xlsx', index=False)

print("추출 완료")
