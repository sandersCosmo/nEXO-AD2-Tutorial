'''
AD2 Wave Generator

Outputs a square wave from the AnalogOut Channel 1

author: Nick Sanders
date: 8-1-2022

To run:
python wavegen.py
'''
import numpy as np
import sys
import time
from tqdm import tqdm
import matplotlib.pyplot as plt
from ctypes import *
sys.path.insert(0, 'C:/Program Files (x86)/Digilent/WaveFormsSDK/samples/py')
from dwfconstants import *
dwf = cdll.dwf

'''
Pulse Parameters
'''
pulse_freq = 500  #Hz
offset = 0.0  #V
amplitude = 0.1  #V

hdwf = c_int()  #Variable to write device ID

print("Opening first device")
dwf.FDwfDeviceOpen(c_int(-1), byref(hdwf))  #Open AD2

if hdwf.value == hdwfNone.value:
    szError = create_string_buffer(512)
    dwf.FDwfGetLastErrorMsg(szError);
    print("failed to open device\n"+str(szError.value))
    quit()
    

'''
Generate Pulse
'''
dwf.FDwfAnalogOutNodeEnableSet(hdwf, c_int(0), c_int(0), c_bool(True))            #Enable Pulse Gen
dwf.FDwfAnalogOutNodeFunctionSet(hdwf, c_int(0), c_int(0), funcSquare)            #Set wave type
dwf.FDwfAnalogOutNodeFrequencySet(hdwf, c_int(0), c_int(0), c_double(pulse_freq)) #Frequency
dwf.FDwfAnalogOutNodeOffsetSet(hdwf, c_int(0), c_int(0), c_double(offset))        #Offset
dwf.FDwfAnalogOutNodeAmplitudeSet(hdwf, c_int(0), c_int(0), c_double(amplitude))  #Amplitude
dwf.FDwfAnalogOutConfigure(hdwf, c_int(0), c_bool(True))                          #Turn Generator on

x = input('Press Enter to Stop')

dwf.FDwfAnalogOutConfigure(hdwf, c_int(0), c_bool(False))  #Turn Generator off
dwf.FDwfDeviceCloseAll()  #Close AD2