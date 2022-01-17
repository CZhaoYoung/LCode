# https://stackoverflow.com/questions/54242194/python-find-the-closest-color-to-a-color-from-giving-list-of-colors

# Easy

from math import sqrt

# COLORS = (
#     (181, 230, 99),
#     (23, 186, 241),
#     (99, 23, 153),
#     (231, 99, 29),
# )
#
#
# def closest_color (rgb):
#     r, g, b = rgb(rgb)
#     color_diffs = []
#     for color in COLORS:
#         cr, cg, cb = color
#         color_diffs = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
#         color_diffs.append((color_diffs, color))
#     return min(color_diffs)[1]

from math import sqrt

#
# Complete the 'closestColor' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY pixels as parameter.
#


COLORS = (
    (0, 0, 0),
    (255, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
)


def closestColor(pixels):
    # Write your code here
    for pixel in pixels:
        r = int(pixel[0:8])
        g = int(pixel[8:16])
        b = int(pixel[16:24])
        color_diff = []
        cnames = []
        for color in COLORS:
            cr, cg, cb = color
            print (type(cr))
            color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
            # color_diff = abs(r - int(cr)) ** 2 + abs(g - int(cg)) ** 2 + abs(b - int(cb)) ** 2
            # color_diff.append((color_diff, color))
            # min_index = color_diff.index(min(color_diff))
            # return  cnames[min_index]

if __name__ == '__main__':
    pixels = ["000000001111111100000110"]
    closestColor(pixels)