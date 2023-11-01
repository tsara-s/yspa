#least squares regression lab 7-17
import numpy as np
import matplotlib.pyplot as plt


#part a
# x1 = np.array([10,8,13,9,11,14,6,4,12,7,5])
# y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
# 
# 
# y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
# 
# y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
# 
# x4 = np.array([8,8,8,8,8,8,8,19,8,8,8])
# y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.5, 5.56, 7.91, 6.89])

# ps4x = np.array([1.1, 1.6, 2.0, 2.1, 2.9, 3.2,
#                  4.4, 4.9])
# ps4y = np.array([72.61, 72.91, 73, 73.11, 73.52, 73.7,  74.26, 74.51])


def calc_m(xlist, ylist):
    avgY = 0
    avgX = 0
    
    for i in range(0, len(ylist)):
        avgX += xlist[i]
        avgY += ylist[i]
    
    avgX /= len(xlist)
    avgY /= len(ylist)
    
    totalN=0
    totalD=0
    
    for i in range(0, len(ylist)):
        num = xlist[i]*ylist[i] - xlist[i]*avgY
        denom = xlist[i]**2 - xlist[i]*avgX
        
        totalN += num
        totalD += denom
        
    m = totalN/totalD
    return m
    
    




# part b
def calc_lsrl(xlist, ylist):
    
    N = len(xlist)
    totX = np.sum(xlist)
    totXsq = np.sum(np.multiply(xlist, xlist))
    totY = np.sum(ylist)
    totxiyi = np.sum(np.multiply(xlist, ylist))
    
#     for i in range(0, len(ylist)):
#         totxiyi += xlist[i]*ylist[i]
#         totXsq = xlist[i]**2
    
    sqmat = np.array([[N, totX], [totX, totXsq]])
    sqmat = np.linalg.inv(sqmat)
    ymat = np.array([totY, totxiyi])
    
    out = np.dot(sqmat, ymat)
    
    
    
    
#     chisq = np.sum(np.multiply(ylist-(out[1]*xlist+out[0]), ylist-(out[1]*xlist+out[0])))
# #     print(ylist-(out[1]*xlist+out[0]))
#     
#     std = np.sqrt(chisq/(N-2))
#     print(std)
    
    return out


# print(calc_lsrl(x1, y1))



# m = calc_m(x1, y1)

# line1:
# m = 0.75
# b = 1
# 
# #line2: 
# m = 0.4
# b = 4
# 
# #Line3:
# m =10/13
# b = 0.5
# 
# #Line4:
# m = 5/11
# b = 3.3

# xLine = np.linspace(4, 14, 20)
# yLine = m*xLine + b
# 
# plt.plot(xLine, yLine)
# plt.xlabel('x')
# plt.ylabel('y')
# 
# plt.plot(x1, y1, '.')
# 
# #a = actual
# b1a = calc_lsrl(x1, y1)[0]
# m1a = calc_lsrl(x1, y1)[1]
# xaLine = np.linspace(4, 14, 20)
# yaLine = m1a*xLine + b1a
# plt.plot(xaLine, yaLine)
# 
# plt.show()



# Seconday Task
# from astropy.table import Table
# data=Table.read("Hubble_data.txt", format='ascii')
# 
# dist = data['distance']
# vel = data['velocity']
# 
# slope = calc_lsrl(dist, vel)[1]
# b = calc_lsrl(dist, vel)[0]
# 
# xLine = np.linspace(dist.min(), dist.max(), len(dist))
# yLine = slope*xLine + b
# 
# plt.plot(dist, vel, '.')
# 
# plt.plot(xLine, yLine)
# plt.xlabel('distance (Mpc)')
# plt.ylabel('velocity (km/s)')
# 
# plt.show()


def graph(xlist, ylist):
    slope = calc_m(xlist, ylist)
    b = calc_lsrl(xlist, ylist)[0]
    
    
#     xLine = np.linspace(xlist.min(), xlist.max(), len(xlist))
    xLine = xlist
    yLine = slope*xLine + b
    print("y = " + str(slope) + "x + " + str(b))

#     plt.plot(xlist, ylist, '.')

    plt.plot(xLine, yLine)
#     plt.xlabel('x')
#     plt.ylabel('y')

#     plt.show()

