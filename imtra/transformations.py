from collections.abc import Callable

from PIL import Image


def crop(image_buffer:Image, anchor_x, anchor_y, target_width, target_height) -> Image:
    final_width = min(image_buffer.width - anchor_x, target_width)
    final_height = min(image_buffer.height - anchor_y, target_height)
    
    image_buffer_pixels = image_buffer.load() # create a PixelAccess object
    modified_buffer = Image.new("RGBA", (final_width, final_height))
    modified_buffer_pixels = modified_buffer.load()
    
    for row in range(final_width):
        for column in range(final_height):
            modified_buffer_pixels[row, column] = image_buffer_pixels[anchor_x+row, anchor_y+column]
            
    return modified_buffer


def mirror(image_buffer:Image, x_axis_flip:bool, y_axis_flip:bool) -> Image:
    if not x_axis_flip and not y_axis_flip:
        return image_buffer
    
    image_buffer_pixels = image_buffer.load()

    modified_buffer = Image.new("RGBA", (image_buffer.width, image_buffer.height))
    modified_buffer_pixels = modified_buffer.load()

    for row in range(image_buffer.width):
        for column in range(image_buffer.height):
            if x_axis_flip and y_axis_flip:
                target_row = image_buffer.width - row -1
                target_column = image_buffer.height - column -1
            elif x_axis_flip:
                target_row = image_buffer.width - row -1
                target_column = column
            elif y_axis_flip:
                target_row = row
                target_column = image_buffer.height - column -1
            modified_buffer_pixels[target_row, target_column] = image_buffer_pixels[row, column]

    return modified_buffer


def rotate(image_buffer:Image, degree) -> Image:
    pass

def scale_nearest(image_buffer:Image) -> Image:
    pass

def scale_bilinear(image_buffer:Image) -> Image:
    pass

def scale_bicubic(image_buffer:Image) -> Image:
    pass

