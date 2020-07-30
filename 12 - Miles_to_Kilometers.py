''' Convert Miles to Kilometers
    1 mile = 1.609344 Kilometers'''

usr_mi = float(input("Enter Miles: \n"))

km = usr_mi * 1.609344

print("Kilometers: ", km)

# Other way
def miles_to_kilometers(mi):

    km = 0

    km = mi * 1.609344

    return km


print("Kilometers: ", miles_to_kilometers(usr_mi))
