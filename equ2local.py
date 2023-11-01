import numpy as np

pi = np.pi

def altitude(lat, dec, HA):

    HA = HA*15*(pi/180)
    lat = lat*(pi/180)
    dec = dec*(pi/180)
    sin_h = np.sin(lat)*np.sin(dec) + np.cos(lat) * np.cos(dec) * np.cos(HA)
    
    h = np.arcsin(sin_h)
    h = h*(180/pi)
    return h

def azimuth(dec, HA, h):
    
    dec = dec*(pi/180)
    HA = HA*15*(pi/180)
    h = h*(pi/180)
    
    sin_A = -np.cos(dec)*np.sin(HA)/np.cos(h)
    
    azi = np.arcsin(sin_A)
    
    return azi*(180/pi)


def hour_angle(local_time, long, day, RA):
    GST0 = 6.68333
    long /= 15
    
    HA = local_time +4 - long + GST0 + 4*day/60 - RA
    
    return HA


def convert(lat, long, local_time, dec, day, RA):
    
    HA = hour_angle(local_time, long, day, RA)
    print(HA)
    
    print("Altitude: " + str(altitude(lat, dec, HA)) + "\n" + "Azimuth: " + str(azimuth(dec, HA, altitude(lat, dec, HA))))


convert(41.3, 72.9, 23.8, 19.33, 191, 21.75)