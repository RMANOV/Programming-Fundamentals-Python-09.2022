

# You will be given the coordinates of four points. 
# The first and the second pair of points form two different lines. 
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" 
# starting from the point which is closer to the center of the coordinate system (0, 0). 
# You can reuse the method that you wrote for the previous problem. 
# If the lines are of equal length, print only the first one. 
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

def get_line_length(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def print_point(x, y):
    # print(f"({int(x)}, {int(y)})")
    # print results on the same line
    print(f"({int(x)}, {int(y)})", end="")

def main():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    x4 = float(input())
    y4 = float(input())
    x, y = get_closest_point(x1, y1, x2, y2)
    x5, y5 = get_closest_point(x3, y3, x4, y4)
    line_1 = get_line_length(x1, y1, x2, y2)
    line_2 = get_line_length(x3, y3, x4, y4)
    if line_1 >= line_2:
        # Print points from the longest and closest line        
        print_point(x2, y2)
        print_point(x1, y1)
    else:
        print_point(x4, y4)
        print_point(x3, y3)
        
    #     print_point(x, y)
    #     print_point(x5, y5)
    # else:
    #     print_point(x5, y5)
    #     print_point(x, y)

main()