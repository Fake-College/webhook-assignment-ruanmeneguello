#test
"""Simple script to get a circle radius from the user and compute
diameter, circumference, and area.
"""

import math

def main():
    # Get the radius of the circle from the user
    try:
        r_input = input("Enter the radius of the circle: ").strip()
        radius = float(r_input)
        if radius < 0:
            print("Radius cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value for the radius.")
        return

    # Calculate the diameter of the circle
    diameter = 2 * radius

    # Calculate the circumference of the circle
    circumference = 2 * math.pi * radius

    # Calculate the area of the circle
    area = math.pi * radius ** 2

    # Print the values for the user
    print(f"Radius: {radius:.2f}")
    print(f"Diameter: {diameter:.2f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Area: {area:.2f}")

if __name__ == "__main__":
    main()
