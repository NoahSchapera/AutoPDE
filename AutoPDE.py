# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:07:07 2023

@author: Eden Schapera
"""
import os

# Data collection function
def collectData(wavelength_select, wavelength, wavelength_index, voltage_400, voltage_500_589, testing):
    
    # Using wavelength_select, provided by user, identify actual wavelength and index from arrays
    wl_choice = wavelength[wavelength_select]
    wl_index_choice = wavelength_index[wavelength_select]
    
    print(" ")
    print(" ")
    input("Connect flasher to " + wl_choice + "nm : ENTER")
    print(" ")    
    
    # Identify which voltage path to use (determined by wavelength)
    if wavelength_select == 0:
        voltage_steps = voltage_400
    else:
        voltage_steps = voltage_500_589    
    
    
    # Iterate through all voltages in path
    for v in voltage_steps:
        # stall user to change voltage
        input("Set voltage to " + v + " volts : ENTER")
        
        # call command through commandline
        if testing == True:
            print("~/PDEDAQ/PDEDAQ -of " +"../"+ SN+"/"+SIPM+"_"+SN+"_"+wl_choice+"nm_"+v+"V_"+date+ " -w " + wl_index_choice + " -inputrange 1")
        else:
            os.system("~/PDEDAQ/PDEDAQ -of " +"../"+ SN+"/"+SIPM+"_"+SN+"_"+wl_choice+"nm_"+v+"V_"+date+ " -w " + wl_index_choice + " -inputrange 1")
        print(" ")

# analysis of data
def analyzeData(wavelength_select, wavelength, wavelength_index, voltage_400, voltage_500_589, testing, sr, ws, sz):
    # Using wavelength_select, provided by user, identify actual wavelength and index from arrays
    wl_choice = wavelength[wavelength_select]
    wl_index_choice = wavelength_index[wavelength_select]
    
    # Identify which voltage path to use (determined by wavelength)
    if wavelength_select == 0:
        voltage_steps = voltage_400
    else:
        voltage_steps = voltage_500_589    
    
    
    print("Analyzing " + wl_choice+"nm data.")
    print(" ")
    
    # Index of voltage step loop, use while loop instead of for loop to allow for repeat analysis
    i = 0
    while i < len(voltage_steps):
        #Get current voltage from path
        v = voltage_steps[i]
        
        repeat_flag = input("Next, analysis for " + v + "V: ENTER or 'r' to repeat previous voltage analysis: ")
        
        # If repeat is indicated, back up by decreasing index, and find new voltage. 
        if repeat_flag == 'r':
            i -= 1
            v = voltage_steps[i]
            print("Backing up... Repeating analysis for V = " + v + "V")
        
        
        # call command line function to preform analysis
        if testing == True:
            print("~/PDEAnalysis/PDEAnalysis -if " +"../"+ SN+"/"+SIPM+"_"+SN+"_"+wl_choice+"nm_"+v+"V_"+date+ " -wl " + wl_index_choice + \
                  " -of test" + \
                  " -cf ../calibrations/calib" + date + \
                  " -sr " + sr + " -ws " +  ws + " -sz " + sz)
        else:
            os.system("~/PDEAnalysis/PDEAnalysis -if " +"../"+ SN+"/"+SIPM+"_"+SN+"_"+wl_choice+"nm_"+v+"V_"+date+ " -wl " + wl_index_choice + \
                    " -of test" + \
                    " -cf ../calibrations/calib" + date + \
                    " -sr " + sr + " -ws " +  ws + " -sz " + sz)
        print(" ")
        
        # Increase index by one to move onto next voltage
        i+=1

# main loop of program
def statusLoop(status, wl_input, wavelength, wavelength_index, voltage_400, voltage_500_589, testing):
    
    if status == 'c': 
        
        # if all, repeat for all wavelengths
        if wl_input == 3:
            for wl in range(len(wavelength)):
                collectData(wl, wavelength, wavelength_index, voltage_400, voltage_500_589, testing)
        
        #else, only do one wavelength
        else: 
            collectData(wl_input, wavelength, wavelength_index, voltage_400, voltage_500_589, testing)
            
        # After data collection is complete, proceed to analysis if desired
        print("Data collection complete. ")
        ana = input("Preform analysis? y/n : ")
        
        # Recursively call status loop with analysis mode enabled. 
        if ana == 'y':
            statusLoop('a', wl_input, wavelength, wavelength_index, voltage_400, voltage_500_589, testing)
        
    elif status == 'a':
        
        # Input relevant parameters
        sr = input('Splitting Ratio: ')
        ws = input('Wave Start: ')
        sz = input('Wave Size: ')
        
        # if user selected 'all', repeat analysis for all wavelengths
        if wl_input == 3:
            for wl in range(len(wavelength)):
                analyzeData(wl, wavelength, wavelength_index, voltage_400, voltage_500_589, testing, sr, ws, sz)
        
        #else, only do one wavelength
        else: 
            analyzeData(wl_input, wavelength, wavelength_index, voltage_400, voltage_500_589, testing, sr, ws, sz)


#initializing variables

# Name of SIPM used for Trinity Demonstrator
SIPM = "S14161-6050HS-04"
# Wavelengths available in flashing setup
wavelength = ["400", "500", "589"]
# Index of wavelengths above in the analysis / data collection programs
wavelength_index = ["1", "3", "4"]

# Voltage paths for data collection / analysis
voltage_400 = ["41.0", "41.5", "42.0", "43.0", "45.0"]
voltage_500_589 = ["41.0", "41.5", "42.0", "42.5"]


#Begin


print("AutoPDE : Ver. 1.3 : 26 / 06 / 2023")
print("by Eden Schapera")
print("----------------------------")
test_input = input("Testing? y/n : ")
status = input("Collection or Analysis? c/a : ")

# testing parser
if test_input == "y":
    testing = True
else: 
    testing = False


# input vals
print(" ")
date = input("Date DDMMYYYY : ")
SN = input("Directory Name (SN) : ")


wl_input = int(input("Select wavelength: 400nm (0), 500nm (1), 589nm (2), all (3) : "))
        
statusLoop(status, wl_input, wavelength, wavelength_index, voltage_400, voltage_500_589, testing)

