import math

def calculate_wind_chill(t, v):
    if abs(t) > 50 or v < 3 or v > 120:
        print("Error: Invalid input values. Temperature (t) must be within -50 to 50 (absolute value), and wind speed (v) must be between 3 and 120.")
        return None

    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v**0.16
    return w

t = float(input("Enter the temperature (in Fahrenheit): "))

v = float(input("Enter the wind speed (in miles per hour): "))

wind_chill = calculate_wind_chill(t, v)

if wind_chill is not None:
    print(f"Wind chill for temperature {t}°F and wind speed {v} mph: {wind_chill:.2f}")