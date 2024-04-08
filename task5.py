#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.
import math
import os

print("\n\n  input volume:")
v = input()
v = float(v)
os.system('cls')
r = ( 3 * (v / (4 * 3.14)))**0.33333333
r = float(r)
print(f"\n\n  Volume: {r}")


