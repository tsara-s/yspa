#ps4-5 lsrl

import numpy as np
import matplotlib.pyplot as plt
from lsrl_lab717 import *


r, v, R, V = np.loadtxt('../../Downloads/ps-4-ngc-data/instr-std-finals.csv', skiprows =1, usecols = (2,3,4,5), unpack=True, delimiter=',')

vr = v-r
VR = V-R

Vv = V-v

plt.scatter(VR, Vv, color = 'm')
plt.xlim(VR.max(), VR.min())
plt.title('V-R vs. V-v')
plt.xlabel('V-R')
plt.ylabel('V-v')

plt.gca().invert_xaxis()

graph(VR, Vv)