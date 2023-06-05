import math
import argparse

parser = argparse.ArgumentParser(description="Program calculates the square "
                                 + "of a triangle.")
parser.add_argument('side', type=float, help="Length of a side", nargs=3)
args = parser.parse_args()
sides = args.side


def main():
    if is_valid_triangle() is False:
        return
    square_triangle = calculate_square_triangle()
    print("Square of the triangle is " + str(round(square_triangle, 2)))


def calculate_square_triangle():
    perimeter = calculate_perimeter()
    p = perimeter / 2  # half of the perimeter for the formula
    square = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
    return square


def calculate_perimeter():
    perimeter = 0
    for side in sides:
        perimeter += side
    return perimeter


def is_valid_triangle():
    for side in sides:
        if side <= 0:
            print("Side's length must be greater than zero!")
            return False
    side_a = sides[0]
    side_b = sides[1]
    side_c = sides[2]
    if (side_a >= side_b + side_c) or (side_b >= side_a + side_c) \
            or (side_c >= side_a + side_b):
        print("Such triangle does not exist! Any side's length cannot\n"
              + "exceed the sum of the two other sides!")
        return False
    return True


if __name__ == "__main__":
    main()
