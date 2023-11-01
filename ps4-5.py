#ps4-5

import numpy as np
import matplotlib.pyplot as plt

RA, DEC, G, R = np.loadtxt('../../Downloads/ps-4-ngc-data/ps4-5-apass_V_data.csv', skiprows =1, unpack=True, delimiter=',')


G = np.round(G, decimals=3)


size = (17.0 - G)*10
plt.scatter(RA, DEC, size, color = 'g')
plt.xlim(RA.max(), RA.min())

for i,label in enumerate(G):
    plt.annotate(str(label), (RA[i], DEC[i]), fontsize='x-small')

plt.title('APASS V magnitudes')
plt.xlabel('RA')
plt.ylabel('DEC')



plt.show()