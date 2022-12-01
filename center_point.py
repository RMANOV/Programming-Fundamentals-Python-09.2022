

# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines. 
# Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. 
# The resulting coordinates must be formatted to the lower integer.


def get_distance_from_center(x, y):
    return (x ** 2 + y ** 2) ** 0.5

def get_closest_point(x1, y1, x2, y2):
    distance_1 = get_distance_from_center(x1, y1)
    distance_2 = get_distance_from_center(x2, y2)
    if distance_1 <= distance_2:
        return (x1, y1)
    else:
        return (x2, y2)

def print_point(x, y):
    print(f"({int(x)}, {int(y)})")

def main():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x, y = get_closest_point(x1, y1, x2, y2)
    print_point(x, y)

main()