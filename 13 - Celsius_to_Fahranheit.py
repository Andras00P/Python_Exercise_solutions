''' Take the temperature in degrees Celsius and convert it to Fahrenheit '''

def celsius_to_fahrenheit(c):
    f = 0

    f = c * 1.8 + 32
    # f = c * 9/5 + 32

    return f

usr_c = int(input("Enter temperature in Celsius: \n"))
print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(usr_c))
