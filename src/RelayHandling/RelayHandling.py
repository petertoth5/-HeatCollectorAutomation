#!/usr/bin/env python

import paho.mqtt.client as mqtt

MQTT_SHELLY_RELAY_COMMAND_TOPIC = "SunCollector_Shelly/command/switch:0"
MQTT_SHELLY_RELAY_ON_COMMAND = "on"
MQTT_SHELLY_RELAY_OFF_COMMAND = "off"

def temperature_control(rooftemp, tanktemp, mqttc):
    try:
        # Function to control relay based on temperature difference
        if rooftemp > tanktemp + 7:
            mqttc.publish(MQTT_SHELLY_RELAY_COMMAND_TOPIC, MQTT_SHELLY_RELAY_ON_COMMAND)
            print("Relay state: ", MQTT_SHELLY_RELAY_ON_COMMAND)
            return "Relay ON"
        elif rooftemp < tanktemp + 3:
            mqttc.publish(MQTT_SHELLY_RELAY_COMMAND_TOPIC, MQTT_SHELLY_RELAY_OFF_COMMAND)
            print("Relay state: ", MQTT_SHELLY_RELAY_OFF_COMMAND)
            return "Relay OFF"
        else:
            return "No action needed"
    except TypeError as e:
        print(f"Error: {e}. Please ensure both inputs are numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        