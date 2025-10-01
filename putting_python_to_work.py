# Get the radius of the circle from the user
import math
# testing grade 6
radius = float(input("Enter the radius of the circle: "))

# Calculate the diameter of the circle
diameter = 2 * radius

# Calculate the circumference of the circle
circumference = 2 * math.pi * radius

# Calculate the area of the circle
area = math.pi * radius**2

# Print the values for the user
print(f"For a circle with radius {radius}:")
print(f"The diameter is {diameter}")
print(f"The circumference is {circumference}")
print(f"The area is {area}")
