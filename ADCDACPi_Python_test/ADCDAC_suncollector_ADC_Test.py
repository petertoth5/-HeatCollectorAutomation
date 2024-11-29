#!/usr/bin/env python

"""
================================================
AB Electronics UK ADC DAC Pi 2-Channel ADC, 2-Channel DAC | ADC Read Demo

run with: python demo_adcread.py
================================================

this demo reads the voltage from channel 1 on the ADC inputs
"""

from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals
                                                    
from statistics import mean 

import time
import os
import paho.mqtt.client as mqtt
import random

# Define Variables
MQTT_BROKER = "192.168.1.100"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_ROOFTEMP_TOPIC = "TemperatureRoof"
MQTT_TANKTEMP_TOPIC = "TemperatureTank"

# Define on_connect event Handler
def on_connect(mosq, obj, rc):
	print ("Connected to MQTT Broker")

# Define on_publish event Handler
def on_publish(client, userdata, mid):
	print ("Message Published...")

try:
    from ADCDACPi import ADCDACPi
except ImportError:
    print("Failed to import ADCDACPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append('..')
        from ADCDACPi import ADCDACPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")


def main():
    '''
    Main program function
    '''
    
    # Initiate MQTT Client
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, client_id)

    # Register Event Handlers
    mqttc.on_publish = on_publish
    mqttc.on_connect = on_connect

    # Connect with MQTT Broker
    mqttc.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL) 

    # create an instance of the ADC DAC Pi with a DAC gain set to 1
    adcdac = ADCDACPi(1)

    # set the reference voltage.  this should be set to the exact voltage
    # measured on the raspberry pi 3.3V rail.
    adcdac.set_adc_refvoltage(3.3)
    
    roofAvgArray = []
    tankAvgArray = []
    
    errorFlagRoof = 0
    errorFlagTank = 0

    while True:

        for x in range(10):
            
            uInRoof = adcdac.read_adc_voltage(1, 0)
            uInTank = adcdac.read_adc_voltage(2, 0)
            
            if uInRoof != 0:
                
                resistanceRoof = ((5.0 * 1475.0) / uInRoof) - 1475.0
                tempRoof = (resistanceRoof - 994.667) / 3.817
                roofAvgArray.append(tempRoof)
                errorFlagRoof = 0
            
            else:
                if errorFlagRoof != 1:
                    errorFlagRoof = 1
                    print("Sensor problem on roof!")
            
            if uInTank != 0:
            
                resistanceTank = ((5.0 * 1475.0) / uInTank) - 1475.0
                tempTank = (resistanceTank - 994.667) / 3.817
                tankAvgArray.append(tempTank)
                errorFlagTank = 0
            
            else:
                errorFlagTank = 1
                
            if x == 9:
                    
                # clear the console
                os.system('clear')
                
                if errorFlagTank != 1:
                    print("Sensor problem in tank!")
                    
                if errorFlagRoof != 1:
                    print("Sensor problem on roof!")
                
                print("Everything OK, measurements:")
                print("Roof Temp:")
                print(round(mean(roofAvgArray), 2), " Celsius")
                # Publish message to MQTT Topic 
                mqttc.publish(MQTT_ROOFTEMP_TOPIC,round(mean(roofAvgArray), 2))

                print("Tank Temp:")
                print(round(mean(tankAvgArray), 2), " Celsius")
                # Publish message to MQTT Topic 
                mqttc.publish(MQTT_TANKTEMP_TOPIC,round(mean(tankAvgArray), 2))
                
                tankAvgArray.clear()
                roofAvgArray.clear()
                    
            time.sleep(0.4)

if __name__ == "__main__":
    main()
