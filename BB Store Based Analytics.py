import pandas as pd
from matplotlib import pyplot as plt
desired_width = 400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)
report=pd.read_csv("E:\\Project-Predective Analysis of Retail sales\\Projectdata.csv")
df=pd.DataFrame(report)
# print(df.head(3))


df['transactionDate']= pd.to_datetime(df['transactionDate'])
df=df.set_index('transactionDate')

# df['transactionDate'].loc[start:end]
report1=df.groupby('store_description')['sale_price_after_promo'].sum().sort_values(ascending=False)
print(report1)


indore_malhar_sale=df.loc[df['store_description']=='BB-INDORE-MALHAR MEGA MALL']['sale_price_after_promo'].sum()
print(indore_malhar_sale)
indore_treasure_sale=df.loc[df['store_description']=='BB-INDORE-TREASURE ISLAND']['sale_price_after_promo'].sum()
print(indore_treasure_sale)
total_indore_sale=indore_malhar_sale+indore_treasure_sale
print(total_indore_sale)
# report=report.append({'store_description':'total_indore_sale'},{'sale_price_after_promo':total_indore_sale})
# print(report)
# Z={'BB-HUBLI-GOKUL ROAD-AKSHAY CEN':417342.20,'BB-JAMSHEDPUR-NH-33':324091.98,'BB-MADURAI-KOCHADAI VILLAGE':247566.41,
#    'BB-AMRITSAR-TRILIUM MALL':134807.24,'BB-LUDHIANA-FEROZEPUR-MF':91265.31,'BB_indore_sale':total_indore_sale}
# print(Z)
# print(df.loc[df['store_description']=='BB-INDORE-MALHAR MEGA MALL ',:],'for malgar')

'''adding columns with year, month and weekdays'''
df['Year']=df.index.year
print(df['Year'])
df['Month']=df.index.month
df['Day']=df.index.weekday_name
print(df.sample(5)) #report.sample is used to sample out



'''stores performance on the basis of year'''
start='2016-01-01'
end='2016-12-01'
year2015=df.loc[start:end]
print("this is year",year2015)
yearwise_beststore2015=year2015.groupby(["store_description",'Year','Month','Day'])['sale_price_after_promo'].sum().sort_values(ascending=False)

print(yearwise_beststore2015)






'''plotting sales in the basis of city store'''
# city=Z

# plt.bar(city,align='center',color='g')
# plt.xticks(city,fontsize=8) #here rotation 90 is used to make the lsbels in a vertical.
# plt.ylabel('sales')
# plt.show()

'''88888888888888888888888task remaining888888888888'''
'''# add column related to indore sale like df['indore sale']=

#to add weekdays days={sunday:0,monday:1,.....} using df.apply(lambda: x=days

#convert the float no. of years into integer'''

