# nEXO-AD2-Tutorial

A brief description of using the Digilent Analog Discovery 2 pulse generator and digital oscilloscope.

## Analog Discovery 2

The AD2 with the BNC adapter board has 2 oscilloscope channels and 2 waveform generator channels. The scope channels each have a jumper to switch between AC and DC inputs, and the generator channels each have a jumper to select 50 or 0 ohm output impedance.

## Getting Started

### Installation
First, you will need to install the Waveforms software following the instructions [here](https://digilent.com/reference/software/waveforms/waveforms-3/getting-started-guide). Once that is done, the scripts in this repository should be ready to run.

The scripts in this repository assume you are running on Windows. If using a different OS, there are some nuances to importing certain packages. All the examples included with the SDK should show you what to change for your OS.

### C types
The SDK is actually written in C, but supports a front end in many languages, including python. Because of this, any values passed to any of the package's functions need to be ctype variables. This is done using the ```ctypes``` python package, which is probably already included in your python distribution. This means we are also capable of working with pointers, which many functions require. The ```byref``` function passes a pointer to the variable included in its argument.

### Testing
To test that everything is running smoothly, it is probably easiest to do a test run using ```wavegen.py```. This script simply creates a square wave out of channel 1. The parameters of the pulse can be edited within the script. Just connect this to another oscilloscope to be sure that the pulse generated looks as expected.

You may get an import error for a file called ```dwfconstants```. This file is a text file included in the Waveforms SDK that contains the values for many constants used in both these scripts and Digilent's examples. By default, it is installed to ```C:/Program Files (x86)/Digilent/WaveFormsSDK/samples/py```. If this is not the case for you, either copy that file to the same directory as the script, or change the path in the line above the import statement to the location of the file.

## The Sampler

The primary purpose of this repository is to use the AD2 as a cheap multichannel analyzer. ```AD2_sampler.py``` is the script that does this. It first genreates a square wave in output channel 1, then begins collecting triggered data in both oscilloscope channels. The sampling and trigger parameters are given as additional command line arguments.

To run the script use: ```python AD2_sampler.py <sample_rate (MHz)> <V_trig (V)> <nwaves> <name>```. ```sample_rate``` is the inverse of the time step between consecutive samples in MHz, ```V_trig``` is the voltage to set the trigger in volts, ```nwaves``` is the number of triggered pulses to record, and ```name``` is the name of the file in which to write the data to.

The data from both channels is stored in a single numpy array, named ```all_data``` and written to ```<name>.npy```. The structure of this array is ```[channel, trigger, sample]```. For example, if you wanted to grab the full first waveform in channel 2, you would use ```all_data[1,0,:]```.

## Further Examples

The Waveforms developers have left a lot of example scripts for a wide array of uses. By default, they are located at ```C:\Program Files (x86)\Digilent\WaveFormsSDK\samples\py```

## References

[Waveforms SDK Reference Manual](https://digilent.com/reference/software/waveforms/waveforms-sdk/reference-manual)
