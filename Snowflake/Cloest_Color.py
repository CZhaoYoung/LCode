# https://stackoverflow.com/questions/54242194/python-find-the-closest-color-to-a-color-from-giving-list-of-colors

# Easy

from math import sqrt

COLORS = (
    (181, 230, 99),
    (23, 186, 241),
    (99, 23, 153),
    (231, 99, 29),
)


def closest_color (rgb):
    r, g, b = rgb(rgb)
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diffs = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diffs, color))
    return min(color_diffs)[1]

