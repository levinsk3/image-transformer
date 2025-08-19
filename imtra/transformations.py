def crop(image_buffer:Image, anchor_x, anchor_y, dimension_x, dimension_y) -> Image:
    pass

def mirror(image_buffer:Image, x_axis:bool, y_axis:bool) -> Image:
    pass

def rotate(image_buffer:Image, degree) -> Image:
    pass

def shift(image_buffer:Image, shift_x, shift_y) -> Image:
    pass

def scale_nearest(image_buffer:Image) -> Image:
    pass

def scale_bilinear(image_buffer:Image) -> Image:
    pass

def scale_bicubic(image_buffer:Image) -> Image:
    pass
