graus_celsius = float(input("digite quantos graus celsius deseja converter: "))

fahrenheit = (graus_celsius * 1.8) + 32
kelvin = graus_celsius + 273.15

print(f"{graus_celsius:.2f}ºC equivalem a {fahrenheit:.2f}ºF e a {kelvin:.2f}K")
