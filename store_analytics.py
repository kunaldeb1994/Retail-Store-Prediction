import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
desired_width = 400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)

df1 = pd.read_csv("E:\\Project-Predective Analysis of Retail sales\\Projectdata.csv")
df = pd.DataFrame(df1)
df['transactionDate'] = pd.to_datetime(df['transactionDate'])


cols=['customerID','DOB','Gender','store_code','PinCode',
      'till_no','transaction_number_by_till','promotion_description']
df.drop(cols,axis=1,inplace=True)
df=df.sort_values('transactionDate')
# print(df)
df=df.set_index('transactionDate')
# print(df)
start='2016-01-01'
end='2017-03-27'
df=df.loc[start:end]

def store_analytics():
      store_performance=df.groupby('store_description')["sale_price_after_promo"].sum().sort_values()

      top=store_performance.sort_values()
      '''all store performance'''
      print("this is top",top)
      '''top performing store '''
      print('is the best performing store',top.nlargest(1))

      '''worst performing store '''
      print('is the worst performing store',top.nsmallest(1))
      return store_performance,top
store_analytics()


''' average sale of the store '''
def average_store_sale():
      df['Month']=df.index.month
      average_sale=df.groupby('store_description')["sale_price_after_promo"].mean().sort_values()
      print(df.head())
      print(average_sale)

      store_monthwise = df.groupby(['store_description', 'Month'])['sale_price_after_promo'].count()
      print(store_monthwise)
      return average_sale,store_monthwise
avrg=average_store_sale()

'''finding stats for individual stores'''
# indore_megamall=df.loc[df['store_description'] =='BB-AMRITSAR-TRILIUM MALL'][["sale_price_after_promo",'Month']]
# print(indore_megamall.sort_index())



'''stardard deviation of store from average sales'''
stardard_deviation=avrg[1].std()
print(stardard_deviation)

'''create def functions and use normalization for every objects'''
"""use lambda function for every function"""
'''first groupby by city then by month wise for average sale'''


