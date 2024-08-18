def convert_celsius(temp):
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    return fahrenheit, kelvin

def convert_fahrenheit(temp):
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    return celsius, kelvin

def convert_kelvin(temp):
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return celsius, fahrenheit

def perform_conversion(temp, unit):
    print("Here are the conversions:")
    if unit == 'C':
        fahrenheit, kelvin = convert_celsius(temp)
        print(f"{temp}°C converts to:\n{fahrenheit:.2f} °F\n{kelvin:.2f} K")
    elif unit == 'F':
        celsius, kelvin = convert_fahrenheit(temp)
        print(f"{temp}°F converts to:\n{celsius:.2f} °C\n{kelvin:.2f} K")
    elif unit == 'K':
        celsius, fahrenheit = convert_kelvin(temp)
        print(f"{temp}K converts to:\n{celsius:.2f} °C\n{fahrenheit:.2f} °F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")


temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()


perform_conversion(temperature, unit)
