# ps5-5
# 7-18-2023

import os
import numpy as np
from lsrl_lab717 import *
import math
# from astropy.wcs import WC
# from astropy.skycoord

# solvefielding all the files in cmd line/wcs the file
# read in file as data set
# look for stars in image
# find magitudes of stars in image and their RA and dec


# lowercase = instant magnitude
# uppercase = standard magnitude
v, v_r = np.loadtxt('../../Downloads/starclusterCMD/ps5-5 - Star Cluster Fluxes.csv', skiprows =1, usecols = (3,4), unpack=True, delimiter=',')
# RA, DEC, V, B = np.loadtxt('./color-calibration-lab/sara-apass-data-2.csv', skiprows =1, unpack=True, delimiter=',')


plt.scatter(v_r, v, color = 'c')
for i,label in enumerate(v):
    print(label)
    plt.annotate(str(round(label,2)), (v_r[i], v[i]), fontsize='x-small')

plt.gca().invert_yaxis()
plt.title('Color Index vs Instrumental Magnitude')
plt.xlabel('v-r')
plt.ylabel('v')






plt.show()
