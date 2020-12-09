from struct import pack
from math import sin, cos, pi

width = 600
height = 600
t = 0
STEP = 0.005
pixels = []
x_min = float("inf")
y_min = float("inf")

while t <= 10 * pi:
    x = round(2 * (sin(2 * t) - cos(t)/2), 2)
    if x < x_min:
        x_min = x
    y = round(2 * (cos(2 * t) - sin(t)/2), 2)
    if y < y_min:
        y_min = y
    pixels.append((x, y))
    t += STEP

pixels.reverse()


def create_bitmap_header(wigth, height):
    filetype = 19778
    reserved_1 = 0
    reserved_2 = 0
    offset = 62
    filesize = offset + 1 * wigth * height
    return pack("<HL2HL", filetype, filesize, reserved_1, reserved_2, offset)

def create_info_header(wigth, height):
    header_size = 40
    planes = 1
    bits_per_pixel = 8
    compression = 0
    image_size = 0
    total_colors = 2
    return pack("<3L2H3L", header_size, wigth, height, planes, bits_per_pixel, compression, image_size, total_colors)

def create_color_pallete():
    color_1 = (0, 0, 0, 0)
    color_2 = (255, 255, 255, 0)
    return pack("<8B", *color_1, *color_2)


with open ("img.bmp", "wb") as f:
    f.write(create_bitmap_header(width, height))
    f.write(create_info_header(width, height))
    f.write(create_color_pallete())

    y_pix = y_min
    for y_val in range(height):
        x_pix = x_min
        for x_val in range(width):
            if (x_pix, y_pix) in pixels:
                f.write(pack("<B", 0))
            else:
                f.write(pack("<B", 1))
            x_pix = round(x_pix + STEP, 2)
        y_pix = round(y_pix + STEP, 2)
