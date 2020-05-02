import pandas as pd

import numpy as np

#Loads the csv file as Dataframe object

df = pd.DataFrame.from_csv('ss13hil.csv')

pd.set_option('display.max_columns', 500)

pd.set_option('display.width', 1000)

l2=[]

l2.append("English only")

l2.append("Spanish")

l2.append("Other Indo-European languages")

l2.append("Asian and Pacific Island languages")

l2.append("Other language")

l2.append("ALL")

df_HHL = pd.DataFrame(l2)

df2=df.groupby(['HHL','ACCESS'])['WGTP'].sum().unstack(level=1)

s=df2.sum().sum()

df3=df2.sum()

l3=[0]

for i in range(len(df3)):
    l3.append(df3[i+1])

df4=pd.DataFrame([l3])

df2=pd.concat([df2,df4],ignore_index=True)

df2=pd.concat([df2,df2.sum(axis=1)],axis=1,ignore_index=True)

df2=df2.apply(lambda x:100*x/s)

df2=df2.applymap(lambda x:'%.2f%%'%x)

frames=[df_HHL,df2]

result = pd.concat(frames,axis=1,ignore_index=True)

result.columns=['Household Language','Dummy','Yes w/ subs.','Yes wo/ subs.','No','All']

result=result.drop(result.columns[[1]],axis=1)

print result,'\n'