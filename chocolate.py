import pandas as pd

# 1. 파일 경로 (이미 폴더 안이라서 파일 이름만 적으면 돼요!)
file_path = 'Coffee Shop Sales.xlsx' 

# 2. 엑셀 파일 불러오기
df = pd.read_excel(file_path)

# 3. 'Drinking Chocolate' 카테고리 데이터만 필터링
chocolate_df = df[df['product_category'] == 'Drinking Chocolate'].copy()

# 4. 날짜 형식을 컴퓨터가 인식하게 변환
chocolate_df['transaction_date'] = pd.to_datetime(chocolate_df['transaction_date'])

# 5. 같은 날짜끼리 묶어서 판매량 합계 구하기
daily_sales = chocolate_df.groupby('transaction_date')['transaction_qty'].sum().reset_index()

# 6. 컬럼 이름 정리
daily_sales.columns = ['Date', 'Actual_Sales']

# 7. 최종 결과물 저장
daily_sales.to_excel('hot_chocolate_final.xlsx', index=False)

print("추출 완료")