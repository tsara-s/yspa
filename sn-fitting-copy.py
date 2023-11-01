import matplotlib.pyplot as plt
import numpy as np
# from generalised_model_fitting_lab import *
import matplotlib.lines as mlines
from matplotlib.colors import LogNorm
from scipy import interpolate


timeReds = np.array([2460141.656,
2460146.884,
2460148.762,
2460152.911,
2460153.781,
2460154.854,
2460159.843])
errorReds = np.array([0.07146419037,
0.4646647963,
0.09305807855,
1.323722641,
0.1852969847,
0.1991805189,
0.120404777])
reds = np.array([18.743,
17.861,
18.521,
18.651,
18.583,
18.557,
18.956])

redshift = 0.214
reds +=redshift
timeReds -= 2400000.5


timeGreens = np.array([2460141.651,
2460146.89,
2460148.755,
2460152.905,
2460153.775,
2460154.814,
2460159.852])
errorGreens = np.array([0.07146419037,
0.4646647963,
0.09305807855,
1.323722641,
0.1852969847,
0.1991805189,
0.120404777])
greens = np.array([19.296,
18.171,
19.013,
19.259,
19.274,
18.43,
19.259])


greenshift = 0.309
greens+= greenshift
timeGreens -= 2400000.5


TypeIaDays = np.array([-9.888536,
-8.174646,
-6.632145,
-5.089644,
-3.204365,
-2.518809,
-1.147697,
0.394804,
1.937305,
2.965639,
6.907586,
10.335366,
15.134258,
18.733427,
24.560653,
32.958714])

TypeIaDays += 2460144.5- 2400000.5

TypeIaMag = np.array([-14.001578,
-14.994168,
-15.995169,
-17.004583,
-17.997173,
-18.291585,
-18.745821,
-19.065469,
-19.141175,
-19.090704,
-18.712174,
-18.476645,
-18.299997,
-18.165409,
-17.929879,
-17.416760])

#60144
TypeIaDays, TypeIaMag = np.loadtxt('../../Downloads/SNe_models/TypeIa_days_abs.txt', skiprows =1, unpack=True, delimiter=',')
TypeIaDays += 2460144.5 - 2400000.5

TypeIbDays, TypeIbMag = np.loadtxt('../../Downloads/SNe_models/TypeIb_days_abs.TXT', skiprows =1, unpack=True, delimiter=',')
TypeIbDays += 2460144.5 - 2400000.5



TypeIIbDays, TypeIIbMag = np.loadtxt('../../Downloads/SNe_models/TypeIIb_days_abs.txt', skiprows =1, unpack=True, delimiter=',')
TypeIIbDays += 2460144.5 - 2400000.5



TypeIILDays, TypeIILMag = np.loadtxt('../../Downloads/SNe_models/TypeIIL_days_abs.txt', unpack=True, delimiter=',')
TypeIILDays += 2460144.5 - 2400000.5


TypeIIPDays, TypeIIPMag = np.loadtxt('../../Downloads/SNe_models/TypeIIP_days_abs.txt', skiprows =1, unpack=True, delimiter=',')
TypeIIPDays += 2460144.5 - 2400000.5

# timeReds, errorReds, reds


f_cubIa = interpolate.interp1d(TypeIaDays, TypeIaMag, 'cubic')
# magfitIa = f_cub(TypeIaDays)

f_cubIb = interpolate.interp1d(TypeIbDays, TypeIbMag, 'cubic')
f_cubIIb = interpolate.interp1d(TypeIIbDays, TypeIIbMag, 'cubic')
f_cubIIL = interpolate.interp1d(TypeIILDays, TypeIILMag, 'cubic')
f_cubIIP = interpolate.interp1d(TypeIIPDays, TypeIIPMag, 'cubic')


# magfitIb = f_cub(TypeIbDays)




A = np.linspace(36.5, 38.5, 100)
x_0 = np.linspace(-2.5, 0.5, 100)



xshift = 0
yshift = 0
def besttransformations(A, x_0, function, x1, y, offset):
    
#     chival = []
#     x_val = []
#     y_val = []
    chisq = np.zeros((100, 100))
    for a in range(0, len(A)):
        for x in range(0, len(x_0)):
#             print(x1-x_0[x])
#             print(function(x1-x_0[x]))
            try:
                chisq[a][x] = ((function(x1-x_0[x]) + A[a]-y)**2/(offset**2)).sum()
            except ValueError:
                chisq[a][x] = np.inf
    chisq /= (len(x1)-2)
    print(A[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)[0]])
    print(x_0[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)[1]])
    
    print(chisq[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)])
    xshift = A[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)[0]]
    yshift = x_0[np.unravel_index(np.argmin(chisq, axis=None), chisq.shape)[1]]
    return chisq

chisq = besttransformations(A, x_0, f_cubIa, timeReds, reds, errorReds)
# besttransformations(A, x_0, f_cubIIP, timeGreens, greens, errorGreens)

plt.imshow(chisq,origin='lower',extent=(-2.5,0.5, 36.5, 38.5), vmax=2.2 ) #extent tells imshow what the x and y range are
plt.colorbar()

plt.show()

# print(chisq)
# print(np.argmin(TypeIaMag+37.97979797))
# print((TypeIaDays[8]-1.010101))

'''Model Shifts (red A, red x_0, green A, green x_0):
Ia
37.474747474747474
-1.0101010101010104
37.97979797979798
-0.6060606060606055

Ib
36.717171717171716
-0.030303030303030276
37.27272727272727
0.7575757575757578

IIb
35.35353535353536
1.2727272727272727
35.95959595959596
1.2121212121212122

IIL
35.95959595959596
-2.0202020202020203
36.464646464646464
-1.5656565656565657

IIP
35.25252525252525
0.6060606060606061
35.75757575757576
1.2626262626262625'''




#red fitting curves
plt.plot(TypeIaDays-1.01010101, TypeIaMag+37.474747474747474, label = 'Type Ia', zorder =9, color = 'red')
# plt.plot(TypeIbDays-0.030303030303030276, TypeIbMag+36.717171717171716, label = 'Type Ib', linestyle = 'dashed')
# plt.plot(TypeIIbDays+1.27272727272727, TypeIIbMag+35.35353535353536, label = 'Type IIb', linestyle = 'dashed')
# plt.plot(TypeIILDays-2.0202020202020203, TypeIILMag+35.95959595959596, label = 'Type IIL', linestyle = 'dashed', color = 'cyan')
# plt.plot(TypeIIPDays+0.6060606060606061, TypeIIPMag+35.25252525252525, label = 'Type IIP', linestyle = 'dashed', color = 'magenta')

#green fitting curves
plt.plot(TypeIaDays-0.6060606060606055, TypeIaMag+37.97979797979798, label = 'Type Ia', zorder =9, color = 'green')
# plt.plot(TypeIbDays+0.7575757575757578, TypeIbMag+37.27272727272727, label = 'Type Ib', linestyle = 'dashed')
# plt.plot(TypeIIbDays+1.2121212121212122, TypeIIbMag+35.95959595959596, label = 'Type IIb', linestyle = 'dashed')
# plt.plot(TypeIILDays-1.5656565656565657, TypeIILMag+36.464646464646464, label = 'Type IIL', linestyle = 'dashed', color = 'cyan')
# plt.plot(TypeIIPDays+1.2626262626262625, TypeIIPMag+35.75757575757576, label = 'Type IIP', linestyle = 'dashed', color = 'magenta')

# plt.plot(TypeIaDays, magfit)
plt.errorbar(timeReds, reds, yerr=errorReds, xerr=None, capsize=5, color='black', fmt='o', barsabove = True, zorder=10)
plt.errorbar(timeGreens, greens, yerr=errorGreens, xerr=None, capsize=5, color='black', fmt='o', barsabove = True, zorder=10)
plt.legend()
plt.xlim(min(TypeIaDays), 60190)
plt.xlabel('Modified Julian Day Number')
plt.ylabel('Sloan g Magnitude')
plt.title('Sloan g Magnitude vs Modified Julian Day Number')

plt.gca().invert_yaxis()

plt.show()




plt.plot(TypeIaDays-0.6060606060606055, TypeIaMag+37.97979797979798, zorder =9, color = 'xkcd:forest green', linestyle = 'dotted')
plt.errorbar(timeGreens, greens, yerr=errorGreens, xerr=None, capsize=5, color='green', fmt='o', barsabove = True, zorder=10, label = 'r')
plt.xlim(min(TypeIaDays), 60190)
plt.xlabel('Modified Julian Day Number')
plt.ylabel('Sloan g Magnitude')
plt.title('Sloan g Magnitude vs Modified Julian Day Number')

plt.gca().invert_yaxis()

plt.show()





plt.plot(TypeIaDays-1.01010101, TypeIaMag+37.474747474747474, zorder =9, color = '', linestyle = 'dotted')
plt.errorbar(timeReds, reds, yerr=errorReds, xerr=None, capsize=5, color='red', fmt='o', barsabove = True, zorder=10, label = 'r')
plt.xlim(min(TypeIaDays), 60190)
plt.xlabel('Modified Julian Day Number')
plt.ylabel('Sloan r Magnitude')
plt.title('Sloan r Magnitude vs Modified Julian Day Number')

plt.gca().invert_yaxis()

plt.show()





TypeIaDays -= 60144
timeReds -= 60144
timeGreens -= 60144

greens += 3

plt.plot(TypeIaDays-1.01010101, TypeIaMag+37.474747474747474, zorder =9, color = 'black')
plt.plot(TypeIaDays-0.6060606060606055, TypeIaMag+37.97979797979798 +3, zorder =9, color = 'black')
plt.errorbar(timeReds, reds, yerr=errorReds, xerr=None, capsize=5, color='red', fmt='o', barsabove = True, zorder=10, label = 'r')
plt.errorbar(timeGreens, greens, yerr=errorGreens, xerr=None, capsize=5, color='green', fmt='o', barsabove = True, zorder=10, label = 'g')
plt.fill_between(timeGreens, greens-errorGreens, greens+errorGreens, color ='green', alpha = 0.3)
plt.fill_between(timeReds, reds-errorReds, reds+errorReds, color = 'red', alpha =0.3)


plt.legend()
plt.xlim(min(TypeIaDays), 60190 - 60144)
plt.xlabel('Days after r-band Maximum', fontsize = 10)
plt.ylabel('Sloan Magnitude + Offset', fontsize = 10)
plt.title('SN 2023mnc rg fit with Type Ia model curve', fontsize = 10)
plt.gca().invert_yaxis()
plt.text(30, 23.3, 'g+3.0', fontsize=12)
plt.show()





