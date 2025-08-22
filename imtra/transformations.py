from math import sin, cos, radians

from collections.abc import Callable

from PIL import Image


def crop(image_buffer:Image, anchor_x, anchor_y, target_width, target_height) -> Image:
    final_width = min(image_buffer.width - anchor_x, target_width)
    final_height = min(image_buffer.height - anchor_y, target_height)
    
    image_buffer_pixels = image_buffer.load() # create a PixelAccess object
    modified_buffer = Image.new("RGBA", (final_width, final_height))
    modified_buffer_pixels = modified_buffer.load()
    
    for row in range(final_height):
        for column in range(final_width):
            modified_buffer_pixels[column,row] = image_buffer_pixels[anchor_x+column, anchor_y+row]
            
    return modified_buffer


def mirror(image_buffer:Image, x_axis_flip:bool, y_axis_flip:bool) -> Image:
    if not x_axis_flip and not y_axis_flip:
        return image_buffer
    
    image_buffer_pixels = image_buffer.load()

    modified_buffer = Image.new("RGBA", (image_buffer.width, image_buffer.height))
    modified_buffer_pixels = modified_buffer.load()

    for row in range(image_buffer.height):
        for column in range(image_buffer.width):
            if x_axis_flip and y_axis_flip:
                target_column = image_buffer.width - column - 1
                target_row = image_buffer.height - row - 1
            elif y_axis_flip:
                target_column = column
                target_row = image_buffer.height - row - 1
            elif x_axis_flip:
                target_column = image_buffer.width - column - 1
                target_row = row
            modified_buffer_pixels[target_column, target_row] = image_buffer_pixels[column, row]

    return modified_buffer


def rotate(image_buffer:Image, counter_clokwise:bool=False) -> Image:
    image_buffer_pixels = image_buffer.load()
    modified_buffer = Image.new("RGBA", (image_buffer.height, image_buffer.width))
    modified_buffer_pixels = modified_buffer.load()

    for row in range(image_buffer.height):
        for column in range(image_buffer.width):
            if counter_clokwise:
                modified_buffer_pixels[row,image_buffer.width-column-1] = image_buffer_pixels[column,row]
            else:
                modified_buffer_pixels[image_buffer.height-row-1,column] = image_buffer_pixels[column,row]

    return modified_buffer


def shift(image_buffer:Image, shift_x, shift_y) -> Image:
    modified_buffer = Image.new("RGBA", (image_buffer.width, image_buffer.height), (0,0,0,0))
    
    if abs(shift_x) > image_buffer.width or abs(shift_y) > image_buffer.height:
        return modified_buffer

    image_buffer_pixels = image_buffer.load()
    modified_buffer_pixels = modified_buffer.load()
    
    starting_scan_x = 0
    starting_scan_y = 0
    starting_print_x = 0
    starting_print_y = 0
    
    if shift_x > 0:
        starting_print_x += shift_x
    elif shift_x < 0:
        starting_scan_x -= shift_x
    if shift_y > 0:
        starting_print_y += shift_y
    elif shift_y < 0:
        starting_scan_y -= shift_y
        
    for row in range(starting_scan_y, image_buffer.height-starting_print_y):
        for column in range(starting_scan_x, image_buffer.width-starting_print_x):
            print_x = starting_print_x + column - starting_scan_x
            print_y = starting_print_y + row - starting_scan_y
            modified_buffer_pixels[print_x,print_y] = image_buffer_pixels[column, row]

    return modified_buffer


def scale_nearest(image_buffer:Image) -> Image:
    pass

def scale_bilinear(image_buffer:Image) -> Image:
    pass

def scale_bicubic(image_buffer:Image) -> Image:
    pass

