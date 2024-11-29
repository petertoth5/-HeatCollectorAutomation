#!/usr/bin/env python

import time
import os
from ADCDACPi import ADCDACPi

def initADC():
    # create an instance of the ADC DAC Pi with a DAC gain set to 1
    adcdac = ADCDACPi(1)
    # set the reference voltage.  this should be set to the exact voltage
    # measured on the raspberry pi 3.3V rail.
    adcdac.set_adc_refvoltage(3.3)
    return adcdac

def readADCChannelSingle(adcdac, channel):
    return adcdac.read_adc_voltage(channel, 0)
