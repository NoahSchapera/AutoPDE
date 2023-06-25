# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 13:07:07 2023

@author: Eden Schapera
"""
import os

def collectData(wavelength_select, wavelength, wavelength_index, voltage_400, voltage_500_589, testing):
    
    wl_choice = wavelength[wavelength_select]
    wl_index_choice = wavelength_index[wavelength_select]
    
    print(" ")
    print(" ")
    input("Connect flasher to " + wl_choice + "nm : ENTER")
    
    if wavelength_select == 0:
        voltage_steps = voltage_400
    else:
        voltage_steps = voltage_500_589    
    
    print(" ")
    for v in voltage_steps:
        input("Set voltage to " + v + " volts : ENTER")
        if testing == True:
            print("~/PDEDAQ/PDEDAQ -of " +"../"+ SN+"/"+SIPM+"_"+SN+"_"+wl_choice+"nm_"+v+"V_"+date+ " -w " + wl_index_choice + " -inputrange 1")
        else:
            os.system("~/PDEDAQ/PDEDAQ -of " +"../"+ SN+"/"+SIPM+"_"+SN+"_"+wl_choice+"nm_"+v+"V_"+date+ " -w " + wl_index_choice + " -inputrange 1")
        print(" ")

#initializing variables

testing = True

date = "23062023"
SIPM = "S14161-6050HS-04"
SN = "SN14_v2"

wavelength = ["400", "500", "589"]
wavelength_index = ["1", "3", "4"]
voltage_400 = ["41.0", "41.5", "42.0", "43.0", "45.0"]
voltage_500_589 = ["41.0", "41.5", "42.0", "42.5"]

# begin program
print('Welcome to the AutoPDE workflow')
print("V1.1 - 23 / 06 / 2023")
print("by Eden Schapera")
print("----------------------------")
test_input = input("Testing? y/n : ")

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

# if all, repeat for all wavelengths
if wl_input == 3:
    for wl in range(len(wavelength)):
        collectData(wl, wavelength, wavelength_index, voltage_400, voltage_500_589, testing)

#else, only do one wavelength
else: 
    collectData(wl_input, wavelength, wavelength_index, voltage_400, voltage_500_589, testing)
        
     



