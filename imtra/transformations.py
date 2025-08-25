from math import sin, cos, radians, floor, ceil

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


def scale_nearest(image_buffer:Image, factor:float=1.0) -> Image:
    image_buffer_pixels = image_buffer.load()
    modified_buffer = Image.new("RGBA", (floor(image_buffer.width*factor), floor(image_buffer.height*factor)))
    modified_buffer_pixels = modified_buffer.load()
    
    for row in range(modified_buffer.height):
        for column in range(modified_buffer.width):
            neighbor_column = floor(column/factor)
            neighbor_row = floor(row/factor)
            modified_buffer_pixels[column, row] = image_buffer_pixels[neighbor_column, neighbor_row]
            
    return modified_buffer

def scale_bilinear(image_buffer:Image, factor:float=1.0) -> Image:
    image_buffer_pixels = image_buffer.load()
    modified_buffer = Image.new("RGBA", (floor(image_buffer.width*factor), floor(image_buffer.height*factor)))
    modified_buffer_pixels = modified_buffer.load()

    for row in range(modified_buffer.height):
        for column in range(modified_buffer.width):
            projected_x = column/factor
            projected_y = row/factor
            
            previous_column = floor(projected_x)
            next_column = min(ceil(projected_x), image_buffer.width - 1)
            previous_row = floor(projected_y)
            next_row = min(ceil(projected_y), image_buffer.height - 1)
            
            x_total = (next_column-previous_column)
            y_total = (next_row-previous_row)            
            
            if x_total == 0 and y_total == 0: # pixel remapped to a grid corner
                modified_buffer_pixels[column,row] = image_buffer_pixels[previous_column,previous_row]
                
            elif x_total == 0: # collapsed x axis
                weights = [0,0]
                
                y_to_previous = projected_y - previous_row
                y_to_next = next_row - projected_y

                weights[0] = y_to_previous/y_total
                weights[1] = y_to_next/y_total

                bands = [0,0,0,0]
                for band in range(4):
                    bands[band] = int(weights[0]*image_buffer_pixels[previous_column, previous_row][band] + weights[1]*image_buffer_pixels[previous_column, next_row][band])
                
                modified_buffer_pixels[column, row] = (bands[0],bands[1],bands[2],bands[3])

            elif y_total == 0: # collapsed y axis
                weights = [0,0]
                
                x_to_previous = projected_x - previous_column
                x_to_next = next_column - projected_x

                weights[0] = x_to_previous/x_total
                weights[1] = x_to_next/x_total

                bands = [0,0,0,0]
                for band in range(4):
                    bands[band] = int(weights[0]*image_buffer_pixels[previous_column, previous_row][band] + weights[1]*image_buffer_pixels[next_column, previous_row][band])
                
                modified_buffer_pixels[column, row] = (bands[0],bands[1],bands[2],bands[3])

            else: # remapped inbtw 4 original pixels
                weights = [[0,0],[0,0]]

                x_to_previous = projected_x - previous_column
                x_to_next = next_column - projected_x
                y_to_previous = projected_y - previous_row
                y_to_next = next_row - projected_y

                square_size = (next_column - previous_column) * (next_row - previous_row)
    
                weights[0][0] = (x_to_previous*y_to_previous)/square_size
                weights[0][1] = (x_to_next*y_to_previous)/square_size
                weights[1][0] = (x_to_previous*y_to_next)/square_size
                weights[1][1] = (x_to_next*y_to_next)/square_size

                bands = [0,0,0,0]
                for band in range(4):
                    bands[band] = int(weights[0][0] * image_buffer_pixels[previous_column, previous_row][band] + weights[0][1] * image_buffer_pixels[next_column, previous_row][band] + weights[1][0] * image_buffer_pixels[previous_column, next_row][band] + weights[1][1]*image_buffer_pixels[next_column,next_row][band])

                modified_buffer_pixels[column, row] = (bands[0],bands[1],bands[2],bands[3])

    return modified_buffer

def scale_bicubic(image_buffer:Image, factor:float=1.0) -> Image:

    
    pass

