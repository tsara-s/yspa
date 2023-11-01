# ps6-3

import numpy as np
import matplotlib.pyplot as plt
from lsrl_lab717 import *
import math
e = math.e




# def besttransformations(A, x_0, originalX, sigma):
#     chisq = np.zeros((len(A), len(x_0)))
#     for a in range(0, len(A)):
#         for x in range(0, len(x_0)):
#             chisq[a][x] = A[a]*e**((x_0[x]-originalX)**2/(2*sigma**2)).sum()
#             
# 
#             
#             
#     print(A[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)[0]])
#     print(x_0[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)[1]])
    
    
    
    
    
    
    
    
    

intensities = np.loadtxt('../specout.csv', unpack=True, delimiter=',')

px = np.array([i for i in range(0, len(intensities))])

plt.title('Intensity vs. Pixel Value')

# plt.plot(px, intensities, '.')
plt.xlabel('pixel value')
plt.ylabel('intensity')



bg = np.loadtxt('../ps5-1 - specout-noextremes.csv', usecols = (0), unpack=True, delimiter=',')

px_new = [i for i in range(0, len(bg))]
px_new = np.array(px_new)
# plt.plot(px_new, bg, '.')


# graph(px_new, bg)
# plt.title('Continuum Background with Linear Fit')
# plt.xlabel('pixel value')
# plt.ylabel('intensity')
# plt.show()


intensities_clean = intensities - 1.5453704123758107*px - 134.35617021276607
# y = 1.5453704123758107x + 134.35617021276607


plt.gca().invert_xaxis()
# plt.show()

def triple_gaussian(x, *p):
    return p[0]*e**(-(p[1]-x)**2/(2*p[2]**2)) + p[3]*e**(-(p[4]-x)**2/(2*p[5]**2)) + p[6]*e**(-(p[7]-x)**2/(2*p[8]**2))


# peak, center, sigma for three gaussians

p_init = np.array([3150, 173, 4, 888, 408, 4, 452, 480, 4])
fit0 = triple_gaussian(px, *p_init)

# x01 = 173
# x02 = 408
# x03 = 481
# 
# A1 = 3150
# A2 = 888
# A3 = 440
# sigma = 5
# Y1 = A1*e**(-(x01-px)**2/(2*sigma**2))
# Y2 = A2*e**(-(x02-px)**2/(2*sigma**2))
# Y3 = A3*e**(-(x03-px)**2/(2*sigma**2))
# # intensities_clean1 = intensities[:325]
# 
# A2 = np.linspace(0,2000,1)
# X1 = np.linspace(350,450,1)
# intensities_clean2 = intensities[325:450]
# 
# A2 = np.linspace(0,2000,1)
# X1 = np.linspace(450,520,1)
# intensities_clean3 = intensities[450:]


px = 840-px
plt.gca().invert_xaxis()

plt.xlabel('wavelength (nm)')
plt.title('Intensity vs. Wavelength')

plt.plot(px, intensities_clean, '.', px, fit0, '-')
plt.show()

