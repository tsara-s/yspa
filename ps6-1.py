#ps6-1

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
# temp, humidity, altitude, pressure = np.loadtxt('../Balloon Flight/datalog.csv', usecols = (4,5,6,7), unpack=True, delimiter=', ')



with open("../Balloon Flight/datalog.csv", 'rb') as f:
  raw_data = f.read()
raw_data = str(raw_data)
raw_data = raw_data.split(', SLOW')
print(type(raw_data))
# raw_data = open("../Balloon Flight/datalog.csv")


# raw_data=open('../Balloon Flight/datalog.csv', encoding="utf8", errors='ignore')


time=[] #0
latitude=[] #1
longitude=[] #2
elevation = [] #3
temperature = [] #4
humidity = [] #5
altitude = [] #6
pressure = [] #7
dropped = [] #8
geigerInfo = [] #9
uSvHR = [] # 14

# datas = []
# lines = 0
# 
# try:
#     for line in raw_data:
#         curr = line.strip(',\n')
#         curr = curr.split(',')
#         if len(curr)==16:
#             datas.append(curr)
#             lines+=1
# except UnicodeDecodeError:
#     pass
# 
# 
# 
# for data in datas:
#     time.append(float(data[0][2:]))
#     try:
#         latitude.append(float(data[1]))
#     except ValueError:
#         latitude.append(float("NaN"))
#     
#     try:
#         longitude.append(float(data[2]))
#     except ValueError:
#         longitude.append(float("NaN"))
#     
#     try:
#         elevation.append(float(data[3]))
#     except ValueError:
#         elevation.append(float("NaN"))
#         
#         
#     
#     temperature.append(float(data[4]))
#     humidity.append(float(data[5]))
#     altitude.append(float(data[6]))
#     pressure.append(float(data[7]))
#     dropped.append(data[8])
#     geigerInfo.append(data[9:])
#     uSvHR.append(data[14])


for line in raw_data:
    
    if(len(line.split(',')) == 15):
        data = line.split(', ')
        time.append(float(data[0][2:]))
        try:
            latitude.append(float(data[1]))
        except ValueError:
            latitude.append(float("NaN"))
        
        try:
            longitude.append(float(data[2]))
        except ValueError:
            longitude.append(float("NaN"))
        
        try:
            elevation.append(float(data[3]))
        except ValueError:
            elevation.append(float("NaN"))
            
            
        
        temperature.append(float(data[4]))
        humidity.append(float(data[5]))
        altitude.append(float(data[6]))
        pressure.append(float(data[7]))
        dropped.append(data[8])
        geigerInfo.append(data[9:])
#         uSvHR.append(data[14])
            

#     print(data)
#     print(type(data[0]))
#     print(any(map(str.isdigit, data[0])))
    #check if string can be mapped to float
#     if(len(data)>16): 
#         if(any(map(str.isdigit, data[0])) and any(map(str.isdigit, data[1])) and
#            any(map(str.isdigit, data[2])) and any(map(str.isdigit, data[6])) and
#            any(map(str.isdigit, data[4])) and any(map(str.isdigit, data[5])) and
#            any(map(str.isdigit, data[-4]))): 
#             if(float(data[2])<-65):
#                 try:
#                     altitude.append(float(data[6]))
#                     time.append(float(data[0]))
#                     latitude.append(float(data[1]))
#                     longitude.append(float(data[2]))
#                     temperature.append(float(data[4]))
#                     humidity.append(float(data[5]))
#                     
#                     usv.append(float(data[-4]))
#                 except:
#                     pass

skipcount2 = 0

for line in raw_data:
    data2 = line.split(',')
    if(len(data2)==16 and any(map(str.isdigit, data2[14])) and any(map(str.isdigit, data2[6]))):
        uSvHR.append(float(data2[14]))
        altitude.append(float(data2[6]))
    else:
        skipcount2 +=1
        pass

print(skipcount2)

# smoothing the data
timeNew=[] #0
latitudeNew=[] #1
longitudeNew=[] #2
elevationNew = [] #3
temperatureNew = [] #4
humidityNew = [] #5
altitudeNew = [] #6
pressureNew = [] #7
droppedNew = [] #8
geigerInfoNew = geigerInfo #9
uSvHRNew = []


for i in range(0, len(time), 10):
    timeNew.append(time[i])
    latitudeNew.append(latitude[i])
    longitudeNew.append(longitude[i])
    elevationNew.append(elevation[i])
    temperatureNew.append(temperature[i])
    humidityNew.append(humidity[i])
    altitudeNew.append(altitude[i])
    pressureNew.append(pressure[i])
    droppedNew.append(dropped[i])
    
#     geigerInfoNew.append(geigerInfo[i])


# get relevant data (we don't want the data from the drive back)
timeNew = timeNew[:500]
latitudeNew = latitudeNew[:500]
longitudeNew = longitudeNew[:500]
elevationNew = elevationNew[:500]
temperatureNew = temperatureNew[:500]
humidityNew = humidityNew[:500]
altitudeNew = altitudeNew[:500]
pressureNew = pressureNew[:500]
droppedNew = droppedNew[:500]
geigerInfoNew = geigerInfoNew[:500]
uSvHR = uSvHR[:500]
print(uSvHR)

CPS = []
CPM = []
usv = []


# clean geiger data
# for i in geigerInfoNew:
# #     print(geigerInfoNew)
#     CPS.append(float(i[1]))
#     CPM.append(float(i[3]))
#     try:
#         usv.append(float(i[5][1:]))
#     except ValueError:
#         usv.append(float("NaN"))


def inst_deriv(x1, x2, y1, y2):
    return (x2-x1)/(y2-y1)

groundspeed = []
for i in range(len(timeNew)-1):
    groundspeed.append(inst_deriv(altitudeNew[i], altitudeNew[i+1], timeNew[i], timeNew[i+1]))


maxalt = np.argmax(altitudeNew)

print('or here??')


# plt.plot(altitude[150:2975], uSvHR[150:2975])
# plt.plot(altitude[2975:3740], uSvHR[2975:3740], linestyle = 'dashed')
# plt.xlabel("Altitude (m)")
# plt.ylabel("Radiation (uSv/hr)")
# plt.title("Radiation vs Altitude")
# 
# plt.show()



fig, (ax0, ax1, ax2) = plt.subplots(1, 3)
ax0.plot(timeNew[0:maxalt+1], altitudeNew[0:maxalt+1], '-')
ax0.plot(timeNew[maxalt+1:], altitudeNew[maxalt+1:], '-', linestyle = 'dashed')
ax0.set_xlabel("Time (s)")
ax0.set_ylabel("Altitude (m)")
ax0.set_title("Altitude vs Time")
ax1.plot(altitudeNew[0:maxalt+1], temperatureNew[0:maxalt+1])
ax1.plot(altitudeNew[maxalt+1:], temperatureNew[maxalt+1:], '-', linestyle = 'dashed')
ax1.set_xlabel("Altitude (m)")
ax1.set_ylabel("Temperature (C°)")
ax1.set_title("Temperature vs Altitude")
# axs[0, 2].scatter(altitudeNew, pressureNew, marker='.')
# axs[0, 2].set_xlabel("Altitude (m)")
# axs[0, 2].set_ylabel("Pressure (hPa)")
# axs[0, 2].set_title("Pressure vs Altitude")
ax2.plot(altitudeNew[0:maxalt+1], humidityNew[0:maxalt+1])
ax2.plot(altitudeNew[maxalt+1:], humidityNew[maxalt+1:], '-', linestyle = 'dashed')
ax2.set_xlabel("Altitude (m)")
ax2.set_ylabel("Humidity")
ax2.set_title("Humidity vs Altitude")
# plt.plot(altitudeNew[0:maxalt+1], uSvHR[0:maxalt+1])
# plt.plot(altitudeNew[maxalt+1:], uSvHR[maxalt+1:], '-', linestyle = 'dashed')
# plt.set_xlabel("Altitude (m)")
# plt.set_ylabel("Radiation (uSv/h)")
# plt.set_title("Radiation vs Altitude")



plt.show()




plt.plot(timeNew[:-1], groundspeed, '.', markersize=1)

plt.xlabel('time (s)')
plt.ylabel('ground speed (km/hr)')
# plt.xlim([13000/3600, 22000/3600])
plt.title("Ms. Nucifora and Mr. Warrener's ground speeds")
plt.show()




fig, axs = plt.subplots(2, 2)
axs0.plot(time, altitude, '.', markersize=1)
axs0.set_title('Altitude vs. Time')
axs1.plot(temperature, altitude, '.', markersize=1)
axs1.set_title('Temperature vs. Altitude')
axs[1, 0].plot(humidity, altitude, '.', markersize=1)
axs[1, 0].set_title('Humidity vs. Altitude')
plt.plot(x, altitude, 'tab:red')
plt.set_title('Axis [1, 1]')

