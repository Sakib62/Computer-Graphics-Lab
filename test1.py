from pyGameInitialize import pygameSetup
from bresenham_line import bresenham_line_all_condition
from midpoint_circle import midpoint_circle

def main():
    pixels = []
    # pixels.append(midpoint_circle(-10, 0, 10))
    # pixels.append(midpoint_circle(-2, 10, 10))
    # pixels.append(midpoint_circle(5, 5, 10))
    # pixels.append(midpoint_circle(5, -5, 10))
    # pixels.append(midpoint_circle(-2, -10, 10))

    pixels.append(midpoint_circle(-35, 0, 10))
    pixels.append(midpoint_circle(-27, 10, 10))
    pixels.append(midpoint_circle(-20, 5, 10))
    pixels.append(midpoint_circle(-15, -2, 10))
    pixels.append(midpoint_circle(-23, -10, 10))

    pixels.append(bresenham_line_all_condition([5, -15], [-3, 15]))
    pixels.append(bresenham_line_all_condition([5, -15], [13, 15]))
    pixels.append(bresenham_line_all_condition([13, 15], [21, -15]))
    pixels.append(bresenham_line_all_condition([21, -15], [29, 15]))

    pixels.append(bresenham_line_all_condition([35, 15], [35, -15]))
    pixels.append(bresenham_line_all_condition([35, -15], [48, -15]))

    pygameSetup(pixels)


if __name__ == '__main__':
    main()