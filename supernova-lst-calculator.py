import numpy as np
import matplotlib.pyplot as plt



def altitude(lat, dec, HA):
# this function calculates the altitude for a given latitude , declination , andhour angle
    HA = HA*15*(np.pi/180)
    lat = lat*(np.pi/180)
    dec = dec*(np.pi/180)
    sin_h = np.sin(lat)*np.sin(dec) + np.cos(lat) * np.cos(dec) * np.cos(HA)
    h = np.arcsin(sin_h)
    h = h*(180/np.pi)
    return h

def EDT(HA, RA, long , day):
    # this function calculates the EDT for a given hour angle, rightascension , longitude ,
# and day of the year.
    long = long/15
    GST_0 = 6.6833
    UT = HA + RA - long - GST_0 - (4*day)/60
    return UT-7

HA = np.linspace(0, 24, 240)
HA = HA - 12

sRA = 2
sDec = 84.75
h = altitude(41.3, sDec, HA)
EDT = EDT(HA, sRA, -72.9, 193)

# plot of the altitude vs. universal time at the Leitner Family Observatory
plt.scatter(EDT+24, h, color='red', s = 10)
plt.axhline(y = 40, color = 'r', linestyle = '-')
plt.axhline(y = 20, color = 'r', linestyle = '-')

plt.axvline(x = -3, color = 'b', linestyle = '-')
plt.axvline(x = 2, color = 'b', linestyle = '-')
plt.axvline(x = -2, color = 'b', linestyle = '-')
plt.axvline(x = 0, color = 'b', linestyle = '-')

plt. xlabel('EDT Time (EDT/hour)')
plt. ylabel('Altitude (h/degree)')
plt. title('Altitude vs. EDT at the Leitner Observatory')
plt.axis('tight')

# plt.savefig('2023kvp.png', dpi = 300)

plt.show()
