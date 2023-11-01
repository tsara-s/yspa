'''use astropy tables to read in the
file. Make a plot showing all of the
isochrones in the file. Use the
headers in the file to determine
which columns to use.'''

# isochrone lab
#yapsi_w_X0p655234_Z0p004766

import numpy as np
from astropy.table import Table
import matplotlib.pyplot as plt


# print(np.log10((0.004766/0.655234)/0.0230005))
#B-V in x
#V in y

data=Table.read('../Yapsi Isochrones/yapsi_w_X0p655234_Z0p004766.dat',format='ascii')

ages = np.unique(data['col1'])
V = np.unique(data['col6'])
B_V = np.unique(data['col8'])


# preliminary task - plot all the isochrones

# for i in ages:
#     
#     mask = np.where(data['col1']==i)
#     V = data[mask]['col6']
#     B_V = data[mask]['col8']
# #     print('\n')
#     plt.plot(B_V, V)


# isochrone where age==0.001

mask = np.where(data['col1']==0.001)
V = data[mask]['col6']
B_V = data[mask]['col8']

plt.gca().invert_yaxis()
plt.plot(B_V, V)
plt.title('Isochrones')
plt.xlabel('B-V')
plt.ylabel('V')
# plt.show()
    


V,BV=np.loadtxt('../Yapsi Isochrones/color_corrected_CMD_data.txt')
for point in V:
    plt.scatter(BV, V, 1, edgecolors='none', color='m')


# ((V>9),(V<16),(BV>-0.2),(BV<0.7))

# NANmask = np.where(~(np.isnan(V)) or (np.isnan(BV)))
# 
# 
# NANmask = np.where(~np.isnan(BV))

MSmask = (V>9)&(V<16)&(BV>-0.2)&(BV<0.7)
# print(MSmask)
V_masked = V[MSmask]
BV_masked = BV[MSmask]



BV_model=data[mask]['col8']
V_model=data[mask]['col6']
for i in range(len(BV_model)):
    try:
        if BV_model[i+1]>BV_model[i]:
            break
    except IndexError:
        i=len(BV_model)
        break
    
BV_model=BV_model[:i]
V_model=V_model[:i]


plt.show()