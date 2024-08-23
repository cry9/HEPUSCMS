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
#for the dry storage (F)
dry_storage = []
#for %RH 1 (in the Thermal Chamber)
RH1 = []
#for the %RH2 (in the Dry Storage)
RH2 = []
#calculated dew point for chamber temp
chamber_dew_point = []
#calculated dew point for the dry storage
storage_dew_point = []
#time for dry storage graph
t3 = []
#time for room graph
t2 = []
#time for final chamber graph
t1 = []
#positions will be for which part of each string for the time data to omit (list of only days)
positions = [[0,3],[5,20]]
#similar idea for whole_dates as positions, only now we plan to save whole dates
whole_dates = [[5,20]]
#x2_positions is for x-axis positions of dashed lines for the room data csv file 
x2_positions = [0]
#x3_positions for x positions of dashed lines for the dry storage file
x3_positions = [0]

#%%% Loading the csv file for reading with earlier data in read mode
#using pandas as earlier ways of reading did not allow column selection
#frame1 is a variable created to hold the data frame loaded in using the read_csv module from the pandas "pd" library
name1 = input('Please enter the .csv file name without ".csv" at the end for the chamber: \n')
#below and above for the chamber data and name1 is for input from the terminal for automated .csv file reading
frame1 = pd.read_csv(f'{name1}.csv')
#reversing order of the data saved using pandas [:rows, :columns] so [:,::-1] would have reversed the columns
frame1_reverse_rows = frame1.iloc[::-1, :]

#name2 will be for inputing which file to read from for the room data
name2 = input('Please enter the .csv file name without ".csv" at the end for the room: \n')
#for room temp we'll use pandas to read
data1 = pd.read_csv(f'{name2}.csv')
#flipping the rows for reading
data1_reverse_rows = data1.iloc[::-1, :]

#name3 will be for inputing which file to read from for the dry storage data
name3 = input('Please enter the .csv file name without ".csv" at the end for the dry storage: \n')
#for room temp we'll use pandas to read
data2 = pd.read_csv(f'{name3}.csv')
#flipping the rows for reading
data2_reverse_rows = data2.iloc[::-1, :]

#selecting specific columns to keep in the data frame for earlier data set
#saving the necessary column with the corrected reversed rows in the appropriate list
room_temp = data1_reverse_rows['RA3E-F52ABC 2118 T&H Sensor [Temperature & Humidity](2)Temperature(F°)'].tolist()
#higher temperature values now as one data set saved to the appropriate list
chamber_temp = frame1_reverse_rows['RA12S-705FAC Thermal Chamber T&H Sensor [Temperature & Humidity](2)Temperature(F°)'].tolist()
#Now the temperature values in fahrenheit for the dry storage
dry_storage = data2_reverse_rows['RA12S-705FAC Big Dry Storage T&H Sensor [Temperature & Humidity](3)Temperature(F°)'].tolist()
#%RH for earlier data thermal chamber
RH1 = frame1_reverse_rows['RA12S-705FAC Thermal Chamber T&H Sensor [Temperature & Humidity](2)Humidity(%RH)'].tolist()
#%RH for dry storage
RH2 = data2_reverse_rows['RA12S-705FAC Big Dry Storage T&H Sensor [Temperature & Humidity](3)Humidity(%RH)'].tolist()
#t2 is for the room data and t1 is for the chamber data, similarly for x2 and x1 (3 is dry storage)
t2 = data1_reverse_rows['Timestamp (America/Chicago)'].tolist()
t1 = frame1_reverse_rows['Timestamp (America/Chicago)'].tolist()
t3 = data2_reverse_rows['Timestamp (America/Chicago)'].tolist() # for dry storage
#creating empty lists with as many entries as rows in each respective .csv file
x2_b = ['']*len(t2)
x1_b = ['']*len(t1)
x3_b= ['']*len(t3)
#for only the days to save for the room chamber and storage
t2_days = [None]*len(t2)
t2_both = [None]*len(t2)
t1_days = [None]*len(t1)
t1_both = [None]*len(t1)
t3_days = [None]*len(t3)
t3_both = [None]*len(t3)
#making axes for both of our eventually plotted graphs first room
i = 0
while i != len(t2):
    #saving the current index of the list for the times from the timestamp into a variable called text
    text = str(t2[i])
    #for both the month and day
    text1 = str(t2[i])
    #here we will truncate the t2 list so that it only has days left
    offsetNextIndexes = 0
    #for loop using position as indexing variable
    for position in positions:
        #here we omit the characters that we dont need for the current element we are on as we are looping through the time array
        text = text[:position[0] + offsetNextIndexes] + text[position[1] + offsetNextIndexes:]
        offsetNextIndexes += position[0] - position[1]
    #saving the concatinated string into the same index for the day list
    t2_days[i] = text  
    #now we will have a list with both month and day left
    offsetNextIndexes = 0
    for day in whole_dates:
        # doing the same operation as before in the above for loop
        text1 = text1[:day[0] + offsetNextIndexes] + text1[day[1] + offsetNextIndexes:]
        offsetNextIndexes += day[0] - day[1]
    #saving
    t2_both[i] = text1
    #testing
    #print(t2_days[i])
    #this needs to be the same interval as the one between each x-axis on the default plot
    if i % 25 == 0:
        #this is saving the whole time stamp
        #x2[i] = t2[i]
        #so that we get month and day data for each line on the x-axis
        x2_b[i] = t2_both[i]
    
    #incrementing
    i += 1
'''
#uncomment this block if the data in your .csv file for the dry storage is 2 days or longer

#making axes for both of our eventually plotted graphs next the dry storage
i = 0
while i != len(t3):
    #saving the current index of the list for the times from the timestamp into a variable called text
    text3 = str(t3[i])
    #for both the month and day
    text4 = str(t2[i])
    #here we will truncate the t2 list so that it only has days left
    offsetNextIndexes1 = 0
    #for loop using position as indexing variable
    for position in positions:
        #here we omit the characters that we dont need for the current element we are on as we are looping through the time array
        text3 = text3[:position[0] + offsetNextIndexes] + text3[position[1] + offsetNextIndexes:]
        offsetNextIndexes += position[0] - position[1]
    #saving the concatinated string into the same index for the day list
    t3_days[i] = text3  
    #now we will have a list with both month and day left
    offsetNextIndexes = 0
    for day in whole_dates:
        # doing the same operation as before in the above for loop
        text4 = text4[:day[0] + offsetNextIndexes] + text4[day[1] + offsetNextIndexes:]
        offsetNextIndexes += day[0] - day[1]
    #saving
    t3_both[i] = text4
    #testing
    #print(t2_days[i])
    #this needs to be the same interval as the one between each x-axis on the default plot
    if i % 50 == 0:
        #this is saving the whole time stamp
        #x2[i] = t2[i]
        #so that we get month and day data for each line on the x-axis
        x2_b[i] = t2_both[i]
    
    #incrementing
    i += 1
'''    
#If one were to make  dashed lines for the chamber and the dry storage data, respectively, then,
#they should uncomment the above block and add a new block for the chamber following the lead of the above block
#now the chamber needs labels for the x-axis, this is in under the below block
i = 0
while i != len(t1):
    #testing
    #print(t1_both[i])
    #here to have displayed timestamps(must be same increment as generic default graph)
    if i % 20 == 0:  
        #getting data for x-axis
        x1_b[i] = t1[i]
    i+=1
#testing
#print(x1_b)
#list to hold the month and day corresponding to each dashed line plotted for room data
x2_month_dates = [x2_b[0]]
#now for the positions of the dashed lines being a day between each other for room data
i = 1
while i != len(t2):
    if int(t2_days[i]) != int(t2_days[i-1]):
        #for the x-axis position of dashed lines
        x2_positions.append(i) 
        #for the x-axis labels planned to correspond with respective dashed lines
        x2_month_dates.append(t2_both[i])#NEW
    
    else:
        x2_month_dates.append('')
    i += 1



#list to hold the month and day corresponding to each dashed line plotted
# if dashed lines are desired, the above block for the room data should be used instead of the below block

x3_month_dates = [x3_b[0]]
#now the storage needs labels for the x-axis, this is in under the below block
i = 0
while i != len(t3):
    #testing
    #print(t3_both[i])
    #here to have displayed timestamps(must be same increment as generic default graph)
    if i % 2 == 0:  
        #getting data for x-axis
        x3_b[i] = t3[i]
    i+=1

#testing
#print(x2_month_dates)
#print(x2_b)
#print(x2_positions)
#print(t2_days)
#%%% Calculating degrees celsius for each temperature that's recorded as fahrenheit for the room
#(5/9)(Tf-32) = Tc where Tf is deg F and Tc is degrees Celsius
i = 0
while i != len(t2):
    room_temp[i] = (5/9)*(room_temp[i]-32)
    i+=1
#also for the chamber
i = 0
while i != len(t1):
    chamber_temp[i] = (5/9)*(chamber_temp[i]-32)
    i+=1  
#and the dry storage
i = 0
while i != len(t3):
    dry_storage[i] = (5/9)*(dry_storage[i]-32)
    i+=1  
    
#%%% Calculating the dew point 
#defining necessary variables
a = 17.625
b = 243.040
#method for calculating alpha
def calculate_alpha(T,RH):
    #calculating alpha
    alpha = np.log(RH/100) + (a*T/(b+T))
    return alpha

#%%% Dew point calculation
i= 0 #First the calculation for the thermal chamber
while i != len(t1):
    chamber_dew_point.append(b*calculate_alpha(int(chamber_temp[i]), RH1[i]) / (a - calculate_alpha(int(chamber_temp[i]), RH1[i])) )
    i+=1    
#next, the calculation for the dry storage
i= 0
while i != len(t3):
    storage_dew_point.append(b*calculate_alpha(int(dry_storage[i]), RH2[i]) / (a - calculate_alpha(int(dry_storage[i]), RH2[i])) )
    i+=1  

#%%% Plots must first be plotted generically to find the number to use for ticks in the third block of code written above 
#room plot
fig, ax = plt.subplots()
ax.set_xticks(x2_positions)
#plt.figure()
for x in x2_positions:
    plt.axvline(x=x, color = 'grey', linestyle = '--', linewidth = 2)
plt.plot(t2,room_temp, label='Room Temp', color = 'blue')
#plt.plot(room_temp )
plt.ylabel("Room Temperature (Deg C)")
plt.xlabel("Time")
plt.title("Room Temp vs. Time (Rm. 2118)")
plt.ylim(0,40)
plt.xlim(0,len(t2))
plt.xticks(t2, x2_month_dates)
plt.xticks(rotation = 30)
plt.show()

#If dashed lines are desired for the chamber and dry storage, 
#follow the format of the above block of code for the room plot

#chamber plot
plt.figure()
plt.plot(t1,RH1, label = '%RH', color = 'blue')
#plt.plot(RH1, label = '%RH', color = 'blue')
plt.plot(t1,chamber_temp, label='Chamber Temp', color = 'red')
#plt.plot(chamber_temp, label = 'Chamber Temp', color = 'green')\
plt.plot(t1,chamber_dew_point, label = 'Dew Point', color = 'maroon')
#plt.plot(chamber_dew_point, label = 'Dew Point', color = 'red')
plt.xlim(0, len(t1))
plt.ylim(-75,75)
#labels now with parameters above
plt.xlabel("Time")
plt.ylabel("%RH, Chamber Temp(degC) and Dew Point")
plt.title("Climate Monitoring of TC in Rm. 2118")
plt.xticks(t1,x1_b)
plt.legend()
plt.xticks(rotation = 30)
plt.show()


#dry storage plot
fig, ax = plt.subplots()
ax.set_xticks(x3_positions)
#plt.figure()
for x in x3_positions:
    plt.axvline(x=x, color = 'grey', linestyle = '--', linewidth = 2)
plt.plot(t3,dry_storage, label='Room Temp', color = 'blue')
#plt.plot(dry_storage )
plt.ylabel("Dry Storage Temp (Deg C)")
plt.xlabel("Time")
plt.title("Storage Temp vs. Time (Rm. 2118)")
plt.ylim(0,40)
plt.xlim(0,len(t3))
plt.xticks(t3, x3_b)
plt.xticks(rotation = 30)
plt.show()
