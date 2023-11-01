#ps4-5
# Red mag, Green mag
import numpy as np
import matplotlib.pyplot as plt

RA, DEC, G, R = np.loadtxt('../../Downloads/ColCal SN 7-31 - apass_data.csv', skiprows =1, unpack=True, delimiter=',')


R = np.round(R, decimals=3)
G = np.round(G, decimals=3)

size = (17.0 - R)*10
plt.scatter(RA, DEC, size, color = 'm')
plt.xlim(RA.max(), RA.min())

for i,label in enumerate(R):
    plt.annotate(str(label) + ", " + str(G[i]), (RA[i], DEC[i]), fontsize='x-small')

# for i,label in enumerate(G):
#     plt.annotate(str(label), (RA[i], DEC[i]), fontsize='x-small')

plt.gca().invert_yaxis()



plt.title('APASS R, V magnitudes')
plt.xlabel('RA')
plt.ylabel('DEC')



plt.show()