#!/usr/bin/env python

A_COEFF             = 3.817
B_COEFF             = 994.667
U_IN                = 5.0
R2_RESISTANCE       = 1515.0
ERROR_RETURN_VALUE  = 1000

# Converts the voltage to temperature in Celsius.
# Calculation is based on resistance divider equation. We know that the measured voltage value is calculated based on the following equation: Uout = Uin * (R2 / R1 + R2)
# From the calculation above we are curious about R1 resistance and it can be calculated R1 = ((Uin * R2) / Uout) - R2
# Since the PTC sensor is a linear sensor so it's resistance changes linearly to the temperature changes and we know the characteristics of it, then we can do an extrapolation based on the linear lines equation we derive from the sensor's known characteristics.
# A linear line's equation is y = a * x + b. In our case x is the temperature value y is the measured resistance. If we know the resistance then we can calculate the x temperature via the following equation: x = (y - b) / a.
# a and b can be calculated based on the sensor's characteristics.
# For the PTC1000 the lines a and b parameters are: a = 3.817 and b = 994.667
# In our case Uin = 5Volts and R2 resistance value R2 = 1475Ohms
def convertADCMeasurementToTemperature(ADCmeasurementValue):
    
    if ADCmeasurementValue != 0:
        calculatedResistance    = ((U_IN * R2_RESISTANCE) / ADCmeasurementValue) - R2_RESISTANCE
        calculatedTemperature   = (calculatedResistance - B_COEFF) / A_COEFF
    else:
        # In case the measured value by the ADC is not plausible return a defined erroneous value.
        calculatedTemperature = ERROR_RETURN_VALUE

    return calculatedTemperature

