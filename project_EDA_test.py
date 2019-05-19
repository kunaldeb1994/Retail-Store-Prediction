import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

'''Gender base plotting'''
def gender_plot(self):
        df['Gender'].fillna(method='ffill',inplace=True)
        gender_data= plt.pie(df['Gender'].value_counts(),
                        labels=['Male','Female'],
                        shadow=True,
                        autopct='%1.1f%%',
                        explode = (0, 0.1),
                        startangle=90)
        return(gender_data)

'''Age base plotting'''
'''For filling blank dates(NAN) and NANA values'''
def age_group(self):
        df['DOB'].fillna(method='ffill',inplace=True)
        df['DOB'].replace(to_replace='NANA',
                          value='2019-04-02',
                          inplace=True)
        df['DOB']=pd.to_datetime(df['DOB']) #to date time is a function which converts string into date format
        # for col in df:
        #         print(type(df["DOB"][1]))
        column_1 = df['DOB'].loc[:]
        datestamp=pd.DataFrame({"year": column_1.dt.year,
                      # "month": column_1.dt.month,
                      # "day": column_1.dt.day,
                      # "hour": column_1.dt.hour,
                      # "dayofyear": column_1.dt.dayofyear,
                      # "week": column_1.dt.week,
                      # "weekofyear": column_1.dt.weekofyear,
                      # "dayofweek": column_1.dt.dayofweek,
                      # "weekday": column_1.dt.weekday,
                      # "quarter": column_1.dt.quarter,
                     })

        '''extraction of age from DOB'''

        cst_dob=datestamp.year
        df['age']=2019-cst_dob
        df['age_group'] = 'NA'
        df['age_group'][(df['age'] >= 30) &  (df['age']<=60)]= 'family' #age_group is a column with value NA
        df['age_group'][(df['age'] > 18) & (df['age'] <= 29)] = 'youth'
        df['age_group'][(df['age'] <= 18) & (df['age']>=10)] = 'teen'
        df['age_group'][df['age'] >=61 ]='senior_c'
        # print(df['age_group'].value_counts())

        '''ploting AgeGroup'''
        agcount=df['age_group'].value_counts()
        a_objects=('Family','Youth','Senior Citizen','NA','Teen')
        y_pos=np.arange(len(a_objects))
        age_grp = plt.bar(y_pos,agcount,align='center',alpha=0.5)
        plt.xticks(y_pos,a_objects)
        plt.ylabel('count')
        plt.title('Age Group')

        # age_grp= plt.pie(df['age_group'].value_counts(),
        #                 labels=['Family','Youth','Senior Citizen','NA','Teen'],
        #                 shadow=True,
        #                 autopct='%1.1f%%',
        #                 explode = (0.1, 0,0,0,0),
        #                 startangle=180)
        return age_grp


'''For item counts or unique items count'''
# for col in df:
#         print(df["customerID"].value_counts())
#         break

if __name__ == '__main__':
        # header = ['customerID', 'DOB', 'Gender', 'State', 'PinCode', 'transactionDate',
        #           'store_code', 'store_description', 'till_no',
        #           'transaction_number_by_till', 'promo_code', 'promotion_description',
        #           'product_code', 'product_description', 'sale_price_after_promo', 'discountUsed']
        df = pd.read_csv("E:\\Project-Predective Analysis of Retail sales\\Projectdata.csv")
        gender_obj=gender_plot(df['Gender'])
        plt.show(gender_obj)
        age_obj=age_group(df['DOB'])
        # grp_obj=df.groupby(['transactionDate'])
        plt.show(age_obj)


