# color calibration lab 2023 yspa
# 7-18-2023

import os
import numpy as np
from lsrl_lab717 import *
# from astropy.wcs import WC
# from astropy.skycoord

# solvefielding all the files in cmd line/wcs the file
# read in file as data set
# look for stars in image
# find magitudes of stars in image and their RA and dec


# lowercase = instant magnitude
# uppercase = standard magnitude
b, v = np.loadtxt('./color-calibration-lab/our-data.csv', skiprows =1, usecols = (5,6), unpack=True, delimiter=',')
RA, DEC, V, B = np.loadtxt('./color-calibration-lab/sara-apass-data-2.csv', skiprows =1, unpack=True, delimiter=',')

# RA = RA*15
# DEC = DEC*100
inst_bv = b-v
std_bv = B-V

# graph(inst_bv, std_bv)


V = np.round(B, decimals=3)


size = (17.0 - B)*10
plt.scatter(RA, DEC, size, color = 'm')
plt.xlim(RA.max(), RA.min())

for i,label in enumerate(B):
    plt.annotate(str(label), (RA[i], DEC[i]), fontsize='x-small')

plt.title('APASS V magnitudes')
plt.xlabel('RA')
plt.ylabel('DEC')






plt.show()