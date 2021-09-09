# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Tyler Mayou
#               NAME OF TEAM MEMBER 3
#               NAME OF TEAM MEMBER 4
# Section:      472/572
# Assignment:   Lab 2A Activity 3
# Date:         September 8, 2021

#imports
import math as m

"""
Method declaration
"""
def get_distance_linear(time):
    return SLOPE * time + YINT

def get_distance_orbit(time):
    return (SLOPE * time + YINT) % ORBIT_CIRCUMFERENCE

"""
Variable declaration
"""
ORBIT_RADIUS = 6745
ORBIT_CIRCUMFERENCE = 2 * m.pi * ORBIT_RADIUS
SLOPE = 21000.0 / 45.0
YINT = -(SLOPE * 10) + 2025

time = 0
final_dist = 0

"""
Main
"""
print(get_distance_linear(time))
print(get_distance_orbit(time))
