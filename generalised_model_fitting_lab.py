# generalized model fitting lab
#7/25


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import math
from scipy import interpolate



# #let’s test x from -3 to 3 and y from -2 to 2
# x=np.linspace(-3,3,40)
# y=np.linspace(-2,2,40)
# 
# 
# #look up the documentation for meshgrid to find out what it does, particularly look at the examples at the bottom
# xv,yv=np.meshgrid(x,y)
# 
# 
# #calculate chi2 on the grid of values
# chi2=1/(3*np.exp(-((xv+1.01)**2+(yv+0.811)**2)/0.005)+np.exp(-((xv-
# 1)**2+yv**2)))
# 
# 
# #chi2 will naturally be a 1D array, but we need it to be a 2D array to
# # make a plot with imshow. np.reshape can handle that
# chi2=np.reshape(chi2,(len(x),len(y)))
# 
# 
# plt.imshow(chi2,origin='lower',extent=(-3,3,-2,2), norm=LogNorm()) #extent tells imshow what the x and y range are
# plt.colorbar()
# 
# plt.show()



'''Create a “model” that is composed of 13 data points from x=-7 to x=+7 drawn from the function y = e −x . Create both a linear and cubic interpolation of the data. Evaluate the two
interpolations at 100 points from -7 to +7. Plot up the “model” and the two interpolations. You plot
should look like mine. Cubic fits produce “smoother” interpolations, but they are subject to massive
over/under-estimates if you have gaps in your model.'''
e = math.e
x= np.linspace(-7,7,13)
y = e**(-x**2)

f_lin = interpolate.interp1d(x, y)
f_cub = interpolate.interp1d(x, y, 'cubic')
print(f_lin)

xlinear = np.linspace(-7,7,100)
ylinear = f_lin(xlinear)

xcubic = np.linspace(-7,7,100)
ycubic = f_cub(xlinear)

plt.xlabel('x')
plt.ylabel('y')



# Supernova data
days = np.array([-4, -2.5, 1, 2])
m = np.array([1.46, 1.87, 1.08, 1.08])
offset = np.array([0.07, 0.09, 0.05, 0.05])

# plt.plot(xcubic, ycubic, '-', days, m, '.')
# 
# plt.show()

# daysnew = np.linspace(-7,7,100)
# bestfit = f_cub(daysnew)
A = np.linspace(-4, 2, 100)
x_0 = np.linspace(-4, 2, 100)

chisq = np.zeros((100, 100))

def besttransformations(A, x_0, function): 
    for a in range(0, len(A)):
        for x in range(0, len(x_0)):
            chisq[a][x] = ((function(days-x_0[x]) + A[a]-m)**2/(offset**2)).sum()

            
            
    print(A[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)[0]])
    print(x_0[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)[1]])


plt.imshow(chisq,origin='lower',extent=(-4,2,-4,2), norm =LogNorm()) #extent tells imshow what the x and y range are
plt.colorbar()

plt.show()


# first try different values of A / vertical offset, try lines for each and find minimum difference
# try x value offset, calc chisq


# plt.plot(days, m, 'o', xcubic-2.95, ycubic+1.07, '-')
# plt.show()