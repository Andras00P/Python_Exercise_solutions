''' Compute gravitational force between two objects '''


def gravitational_force(m1, m2, d):
    g = 6.673 * (10 ** -11) # Gravitational Constant
    force = 0

    force = (g * m1 * m2) / d ** 2 # Formula for Gravitational Force

    return force

mass_a = float(input("Enter first mass: \n\n"))
mass_b = float(input("Enter sencond mass: \n\n"))
distance = float(input("Distance between the objects: \n\n"))

print("The gravitational force is: ", gravitational_force(mass_a, mass_b, distance))
