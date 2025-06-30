
def circle_perimeter(radius):
 """Returns the perimeter (circumference) of a circle with given radius."""
 return 2 * math.pi * radius

def main():
# Get radius as a floating-point number
 p = float(input("Enter the circle’s radius: "))
# Calculate perimeter
p = circle_perimeter()
# Display result
print(f"The perimeter of a circle with radius {p} is {p:.2f}")

if __name__ == "__main__":
 main()