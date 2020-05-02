import pandas as pd

import numpy as np

#Loads the csv file as Dataframe object

df = pd.DataFrame.from_csv('ss13hil.csv')

pd.set_option('display.max_columns', 500)

pd.set_option('display.width', 1000)

l=[]

l.append('low')

l.append('medium')

l.append('high')

df1 = pd.DataFrame(l)

#compute the min and the max of the low row
min1=df['HINCP'].quantile([0,0.3333334]).min()

max1=df['HINCP'].quantile([0,0.3333334]).max()

df2 = df[(df['HINCP'] >= min1) & (df['HINCP'] < max1)]

#compute the min and the max of the medium row
min2=df['HINCP'].quantile([0.3333334,0.66666667]).min()

max2=df['HINCP'].quantile([0.3333334,0.66666667]).max()

df3 = df[(df['HINCP'] >= min2) & (df['HINCP'] < max2)]

#compute the min and the max of the high row
min3=df['HINCP'].quantile([0.6666666667,1]).min()

max3=df['HINCP'].quantile([0.6666666667,1]).max()

df4 = df[(df['HINCP'] >= min3) & (df['HINCP'] <=max3)]

#put the value of min in a data frame
df5=pd.DataFrame([min1, min2, min3])

#put the value of max in a data frame
df6=pd.DataFrame([max1, max2, max3])

#compute the mean and put the value in a data frame
df7=pd.DataFrame([df2['HINCP'].mean(),df3['HINCP'].mean(),df4['HINCP'].mean()])

#compute the sum of WGTP values for the corresponding range of HINCP
df8=pd.DataFrame([df2['WGTP'].sum(),df3['WGTP'].sum(),df4['WGTP'].sum()])

df9=[df5,df6,df7,df8]

df9=pd.concat(df9,axis=1,ignore_index=True)

df9=df9.applymap(lambda x:'%.4f'%x)

df9=pd.concat([df1,df9],axis=1,ignore_index=True)

#name the column
df9.columns=['HINCP','min','max','mean','household_count']

print df9