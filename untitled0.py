#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:39:15 2024

@author: bryan
"""
#%%% np for math plt for plots and pandas for data + selection
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%% 
#initializing arrays to store desired columns
#for the room temp1 (F)
room_temp = []
#for the chamber temp1 (F)
chamber_temp = []
#for %RH 1
RH1 = []
#calculated dew point for chamber temp
chamber_dew_point = []
#time for room graph
x2 = ['']*1016
t2 = []
#time for final graph
x1 = ['']*519
t1 = []

#%%% Loading the csv file for reading with earlier data in read mode
#using pandas as earlier ways of reading did not allow column selection
#frame1 is a variable created to hold the data frame loaded in using the read_csv module from the pandas "pd" library
#below for the chamber data 
frame1 = pd.read_csv('samples-2024-06-09T23 05 29Z.csv')
#reversing order of the data saved using pandas [:rows, :columns] so [:,::-1] would have reversed the columns
frame1_reverse_rows = frame1.iloc[::-1, :]

#for room temp we'll use pandas to read
data1 = pd.read_csv('samples-2024-05-20T23 07 33Z.csv')
#flipping the rows for reading
data1_reverse_rows = data1.iloc[::-1, :]

#selecting specific columns to keep in the data frame for earlier data set
#saving the necessary column with the corrected reversed rows in the appropriate list
room_temp = data1_reverse_rows['RA3E-F52ABC Red [Temperature](1)Temperature(F°)'].tolist()
#higher temperature values now as one data set saved to the appropriate list
chamber_temp = frame1_reverse_rows['RA3E-F52ABC Blue [Temperature & Humidity](2)Temperature(F°)'].tolist()
#%RH for earlier data
RH1 = frame1_reverse_rows['RA3E-F52ABC Blue [Temperature & Humidity](2)Humidity(%RH)'].tolist()
#t2 is for the room data and t1 is for the chamber data
t2 = data1_reverse_rows['Timestamp (America/Chicago)'].tolist()
t1 = frame1_reverse_rows['Timestamp (America/Chicago)'].tolist()

#making axes for both of our eventually plotted graphs
i = 0
while i != 1016:
    if i % 200 == 0:
        x2[i] = t2[i]
    i += 1
i = 0
while i != 519:
    if i % 100 == 0:
        x1[i] = t1[i]
    i += 1
i = 0 
'''
#testing
while i != 1016:
    print(room_temp[i])
    i += 1

i = 0
while i != 519:
    print(t1[i])    
    i += 1
'''
#%%% Calculating degrees celsius for each temperature that's recorded as fahrenheit
#(5/9)(Tf-32) = Tc where Tf is deg F and Tc is degrees Celsius
i = 0
while i != 1016:
     
    room_temp[i] = (5/9)*(room_temp[i]-32)
    i+=1
#also for the higher temp
i = 0
while i != 519:
     
    chamber_temp[i] = (5/9)*(chamber_temp[i]-32)
    i+=1  

#%%% Calculating the dew point 
#Ts = (b*alpha(T,RH)) / (a - alpha(T,RH))
#where Ts is dew point in celsius
#T is recorded temperature for the room in celcius
#a = 17.625, b = 243.04 and alpha(T,RH) = ln(RH/100) +aT/(b+T)
#defining necessary variables
a = 17.625
b = 243.040
#method for calculating alpha
def calculate_alpha(T,RH):
    #calculating alpha
    alpha = np.log(RH/100) + (a*T/(b+T))
    return alpha

#%%% Dew point calculation
i= 0

while i != 519:
    
    chamber_dew_point.append(b*calculate_alpha(int(chamber_temp[i]), RH1[i]) / (a - calculate_alpha(int(chamber_temp[i]), RH1[i])) )
    i+=1    

#%%% 
plt.figure()
plt.plot(t2,room_temp, label='Room Temp', color = 'blue')
#plt.plot(room_temp )
plt.ylabel("Room Temperature (Deg C)")
plt.ylim(-20,100)
plt.xticks(t2, x2)
plt.xticks(rotation = 30)
plt.show()

plt.figure()
plt.plot(t1,RH1, label = '%RH', color = 'blue')
#plt.plot(RH1, label = '%RH', color = 'blue')
plt.plot(t1,chamber_temp, label='Chamber Temp', color = 'green')
#plt.plot(chamber_temp, label = 'Chamber Temp', color = 'green')
plt.plot(t1,chamber_dew_point, label = 'Dew Point', color = 'red')
#plt.plot(chamber_dew_point, label = 'Dew Point', color = 'red')
plt.ylabel("%RH, Chamber Temp, & Dew Point (Deg C)")
plt.ylim(-100,100)
plt.xticks(t1,x1)
plt.xticks(rotation = 30)
plt.legend()
plt.show()



