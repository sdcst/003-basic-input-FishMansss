#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

print("Surface area of a cone: \n")

##A=πr(r+ h2+r2**(1/2) )
print("radius:")
r = input()
print("height:")
h = input()

a = 3.14 * r * ((r + h**2 + r**2)**(1/2) )
a = float(a)
print(f"surface area = {a}")