# program to import math

import math
number = float(input("Enter a number: "))

sqrt_value = math.sqrt(number)
print(f"Square root :", sqrt_value)

if number > 0:
    log_value = math.log(number)
    print(f"Natural logarithm : {log_value}")
else:
    print("Natural logarithm is not defined for zero or negative numbers.")

sine_value = math.sin(number)
print("sine:", sine_value)