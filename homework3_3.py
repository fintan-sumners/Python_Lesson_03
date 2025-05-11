# This programme converts celsius to fahrenheit
# User inputs degrees in celsius 
celsius = float(input('Input degrees celsius: ')) # Defines degrees in celsius

# Celsius to fahrenheit calculation
fahrenheit = (celsius * 9/5) + 32

# Celsius
print(f'{celsius:.1f}°C')

# Fahrenheit
print(f'{fahrenheit:.1f}°F')

print(f'{celsius:.1f}°C is equal to {fahrenheit:.1f}°F') 