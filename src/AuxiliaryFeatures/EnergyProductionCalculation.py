def calculate_energy(volume_liters, temp_initial, temp_final, time_seconds, SunCollectorGenerating):
    """
    Calculate the power consumption of heating water.

    Parameters:
    volume_liters (float): Volume of water in liters.
    temp_initial (float): Initial temperature of water in degrees Celsius.
    temp_final (float): Final temperature of water in degrees Celsius.
    time_seconds (float): Time taken to heat the water in seconds.

    Returns:
    float: Power consumption in watts (W).
    """
    # Specific heat capacity of water (J/g°C)
    specific_heat_capacity = 4.18

    # Convert volume from liters to kilograms (1 liter of water = 1 kg)
    mass_kg = volume_liters

    # Calculate the temperature change
    delta_temp = temp_final - temp_initial

    # Calculate the heat energy required (Q = m * c * ΔT)
    heat_energy_joules = mass_kg * specific_heat_capacity * delta_temp * 1000  # Convert kg to grams

    # Calculate the power consumption (P = Q / t)
    power_watts = heat_energy_joules / time_seconds

    if (power_watts > 0 and SunCollectorGenerating == True):

        return power_watts
    
    else:
        
        return 0
