#balloon lab 7-28
import numpy as np
import matplotlib.pyplot as plt



raw_data=open('../Balloon Flight/datalog.csv', encoding="utf8", errors='ignore')
time=[]
latitude=[]
longitude=[]
altitude = []
bad = 0
count = 0
for line in raw_data:
    data=line.split(',')
#     print(len(data))
#     print(type(data[0]))
#     print(any(map(str.isdigit, data[0])))
    #check if string can be mapped to float
    if(len(data)>16): 
        if(any(map(str.isdigit, data[0])) and any(map(str.isdigit, data[1])) and any(map(str.isdigit, data[2])) and any(map(str.isdigit, data[6]))): 
            if(float(data[2])<-65):
                count+=1
                time.append(float(data[0]))
                latitude.append(float(data[1]))
                longitude.append(float(data[2]))
                altitude.append(float(data[6]))
    else:
        bad +=1
            
print(bad)
print(len(time))
print(time)
print(latitude)
print(longitude)
print(altitude)

latitude = np.array(latitude)
longitude = np.array(longitude)

# plt.plot(longitude[longitude.argmax():], latitude[longitude.argmax():], '-')
# plt.xlabel('latitude')
# plt.ylabel('longitude')
# plt.title("Ms. Nucifora and Mr. Warrener's drive route")
# plt.show()


avgx_speed = 0
avgy_speed = 0
latitude = np.array(latitude)
longitude = np.array(longitude)

xspeeds = np.zeros(len(longitude) - longitude.argmax())
yspeeds = np.zeros(len(longitude) - longitude.argmax())

groundspeeds = []

for i in range(longitude.argmax(), len(longitude)-1):
    
    '''x = R * cos(lat) * cos(lon)

y = R * cos(lat) * sin(lon)

z = R *sin(lat)'''
    xi = 6371*np.cos(latitude[i])*np.cos(longitude[i])
    xi1 = 6371*np.cos(latitude[i+1])*np.cos(longitude[i+1])
    
    yi = 6371*np.cos(latitude[i])*np.sin(longitude[i])
    yi1 = 6371*np.cos(latitude[i+1])*np.sin(longitude[i+1])
    
    zi = 6371*np.sin(latitude[i])
    zi1 = 6371*np.sin(latitude[i+1])
    
    inst_x = (xi1-xi)/(time[i+1]-time[i])
    inst_y = (yi1-yi)/(time[i+1]-time[i])
    
    avgx_speed += inst_x
    avgy_speed += inst_y
    inst_speed = np.sqrt(inst_x**2 + inst_y**2)
    groundspeeds.append(inst_speed)
    
#     inst_x = (longitude[i+1]-longitude[i])*111/(time[i+1]-time[i])
#     long_conv = 40075 * np.cos(latitude[i]) / 360
#     inst_y = (latitude[i+1]-latitude[i])*long_conv/(time[i+1]-time[i])
#     avgx_speed += inst_x
#     avgy_speed += inst_y
#     inst_speed = np.sqrt(inst_x**2 + inst_y**2)
#     groundspeeds.append(inst_speed)

    
# print(latitude.argmax())
# convert from coordinate degrees to km
# Length in km of 1° of longitude = 40075 km * cos( latitude ) / 360
# avgx_speed *= 111
# avgy_speed *= 111
avg_speed = np.sqrt(avgx_speed**2 + avgx_speed**2)
print(avg_speed)

# print(xspeeds)


# time = [t/3600 for t in time]
plt.plot(time[longitude.argmax()+1:], groundspeeds, '-', markersize=1)

plt.xlabel('time (s)')
plt.ylabel('ground speed (km/hr)')
# plt.xlim([13000/3600, 22000/3600])
plt.title("Ms. Nucifora and Mr. Warrener's ground speeds")
plt.show()