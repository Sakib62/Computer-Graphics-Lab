from pyGameInitialize import pygameSetup
from bresenham_line import bresenham_line_all_condition

def main():
    pixels = []

    # inner rectangle
    pixels.append(bresenham_line_all_condition([-10, -10], [-10, 10]))
    pixels.append(bresenham_line_all_condition([-10, 10], [10, 10]))
    pixels.append(bresenham_line_all_condition([10, 10], [10, -10]))
    pixels.append(bresenham_line_all_condition([-10, -10], [10, -10]))

    # outer rectangle
    pixels.append(bresenham_line_all_condition([-25, -23], [-25, 23]))
    pixels.append(bresenham_line_all_condition([-25, 23], [25, 23]))
    pixels.append(bresenham_line_all_condition([25, 23], [25, -23]))
    pixels.append(bresenham_line_all_condition([-25, -23], [25, -23]))

    #connection between them, keep line straight
    pixels.append(bresenham_line_all_condition([-10, 10], [-24, 22]))
    pixels.append(bresenham_line_all_condition([-10, -10], [-24, -22]))
    pixels.append(bresenham_line_all_condition([10, 10], [24, 22]))
    pixels.append(bresenham_line_all_condition([10, -10], [24, -22]))

    pygameSetup(pixels)

if __name__ == '__main__':
    main()