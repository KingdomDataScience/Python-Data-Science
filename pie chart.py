import pandas as pd
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches

i=0
j=0
k=0
m=0
n=0
l=0 
#bring in data
df=pd.read_csv('ss13hil.csv')
df1=df.fillna(0)
colomn=df1.loc[: , "HHL"]
for x in colomn:
    if x==0:
        i=i+1
    if x==1:
        j=j+1
    if x==2:
        k=k+1
    if x==3:
        l=l+1
    if x==4:
        m=m+1
    if x==5:
        n=n+1
p=i+j+k+l+m+n
print(colomn)

#setup environment
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

fig_size=plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9
plt.rcParams["figure.figsize"] = fig_size


#labels='blue', 'green','red','yellow','orange','pink'
sizes=[ float(i/float(p)),float(j/float(p)) ,float(k/float(p)) ,float(l/float(p)) ,float(m/float(p)), float(n/float(p))]
colors=['green', 'blue','red','yellow','orange','pink']
plt.pie(sizes, colors=colors)
plt.axis('equal')
ax1.set_title(r'Household languages', fontsize=10)

 
blue_patch = mpatches.Patch(color='blue', label='english only')
plt.legend(handles=[blue_patch])
#ax1.tick_params(labelsize=8)

green_patch = mpatches.Patch(color='green', label='spanish')
plt.legend(handles=[green_patch])
#ax1.tick_params(labelsize=8)

red_patch = mpatches.Patch(color='red', label='other indo-european')
plt.legend(handles=[green_patch])
#ax1.tick_params(labelsize=8)

yellow_patch = mpatches.Patch(color='yellow', label='island and pacific languages')
plt.legend(handles=[green_patch])
#ax1.tick_params(labelsize=8)

orange_patch = mpatches.Patch(color='orange', label='other')
plt.legend(handles=[green_patch])
#ax1.tick_params(labelsize=8)

pink_patch = mpatches.Patch(color='pink', label='vacant')
plt.legend(handles=[green_patch])
#ax1.tick_params(labelsize=8)

plt.legend(handles=[ blue_patch,green_patch,red_patch,yellow_patch,orange_patch,pink_patch],prop={'size': 6})


plt.show()