# data mining lab

import pandas as pd
import datetime
from datetime import date
import math

import numpy as np
import matplotlib.pyplot as plt
 
# reading the CSV file
sr1 = pd.read_csv('../New Haven Weather Data/Condition_Sunrise_1.csv')
sr2 = pd.read_csv('../New Haven Weather Data/Condition_Sunrise_2.csv')


sunrise1 = pd.DataFrame(sr1)
sunrise1.columns = ['date', 'temp', 'conditions', 'highSR', 'lowSR']

sunrise2 = pd.DataFrame(sr2)
sunrise2.columns = ['date', 'temp', 'conditions', 'highSR', 'lowSR']

combined_data = pd.concat([sunrise1, sunrise2], ignore_index=True, sort=False)


dates = combined_data['date']
conditions = combined_data['conditions']
low = combined_data['lowSR']
# clear nights are described as clear or fair
# any nights otherwise are cloudy - observing not possible






clearct = 0
cloudyct = 0

for i in conditions:
#     print(i)
    if("Fair"==i or "Clear"==i or "Sunny"==i or "Mostly Clear"==i):
        clearct +=1
    else:
        cloudyct += 1

print("Ratio of cloudy to clear nights in New Haven: " + str(cloudyct) + "/" + str(clearct))








monthclears = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0, 'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}
# monthclouds = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0, 'June': 0, 'July': 0, 'August': 0, 'September': 0, 'October': 0, 'November': 0, 'December': 0}

# difference in number of clear days and number of cloudy days
# because there is not the same amount of data available for all days
for i in range(0, len(dates)):
    month = dates[i].split()[0]


    if("Fair"==conditions[i] or "Clear"==conditions[i] or "Sunny"==conditions[i] or "Mostly Clear"==conditions[i]):
        monthclears[month] += 1
    else:
        monthclears[month] -= 1 
print("Clear days each month: ")

# for key, val in monthclears.items():
#     print(str(key) + ':' + str(val))
# print(monthclears)
print("")


monthslist = list(monthclears.keys())
daycountlist = list(monthclears.values())
for i in range(0, len(monthslist)):
    monthrange = ""
    totcleardays = 0
    for j in range(0, 3):
        monthrange += monthslist[(i+j)%12] + " "
        totcleardays += daycountlist[(i+j)%12]
#     print(monthrange)
#     print(totcleardays)
    
print("The three month range with the lowest number of clear days - cloudy days is June-August, with 9 more clear than cloudy days. ")
print("\n")

plt.bar(monthslist, daycountlist)
plt.xlabel('Month')
plt.ylabel('Clear Days - Cloudy Days')
plt.title("Difference in Number of Clear Days and Number of Cloudy Days per Month")
plt.show()





#days of the week by clear days
weekdayclears = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}

for i in range(0, len(dates)):
    monthalpha = dates[i].split()[0]
    year = int(dates[i].split()[2])
    day = int(dates[i].split()[1][0:-1])
    
    for j in range(0, len(monthslist)):
        if(monthalpha==monthslist[j]):
            monthnum = j+1
            break
    formatted_day = datetime.datetime(year, monthnum, day)
#     print(formatted_day.strftime('%A'))
    day_of_week = formatted_day.strftime('%A')
    
    if("Fair"==conditions[i] or "Clear"==conditions[i] or "Sunny"==conditions[i] or "Mostly Clear"==conditions[i]):
        weekdayclears[day_of_week] += 1
    else:
        weekdayclears[day_of_week] -= 1 

print(weekdayclears)
for key, val in weekdayclears.items():
    print(str(key) + ':' + str(val))
print("The day of the week with the most clear days is Saturday, with 263 clear days. To maximize clear nights, Saturday would be the best day for public nights.")




clear_lows = 0
cloudy_lows = 0
for i in range(0, len(dates)):
#     print(i)
    if("Fair"==conditions[i] or "Clear"==conditions[i] or "Sunny"==conditions[i] or "Mostly Clear"==conditions[i]):
        clear_lows += low[i]
    else:
        if(not math.isnan (low[i])):
#             print(low[i])
            cloudy_lows += low[i]
      
    
print(clear_lows/clearct)
print(cloudy_lows/cloudyct)
print(cloudy_lows/cloudyct-clear_lows/clearct)
# print(cloudyct)
print("It is slightly colder on average on clear nights, by 0.38 deg Celsius.")