import random
import os
import sys

from PIL import Image
from tkinter import filedialog
import readchar

from collections.abc import Callable
from functools import partial

from imtra.transformations import crop, mirror, rotate, scale_nearest, scale_bilinear, scale_bicubic



def select_file(source_path=None) -> str:
    source_path = filedialog.askopenfilename(initialdir="./tests/samples/",
                                                 filetypes=[("PNG Files", "*.png")])
    return source_path

def buffer_file(source_path):
    print(f"Opening {source_path}")
    image_buffer = Image.open(source_path)
    return image_buffer

def display_buffer(image_buffer:Image):
    image_buffer.show()
    return image_buffer

def write_buffer(image_buffer:Image, write_file:str=""):
    while len(write_file) == 0:
        random_write_file = "out_" + str(random.getrandbits(32))
        write_file = filedialog.asksaveasfilename(initialdir="./output/",
                                                  initialfile=random_write_file,
                                                 filetypes=[("PNG Files", "*.png")])
    image_buffer.save(write_file)
    print(f"Buffer saved as {write_file}.")

    
def select_transformation() -> Callable[...,Image]:
    char_input = input("Select transformation:\n\t[1] crop\n\t[2] mirror\n\t[3] rotate\n\t[4] scale-nearest\n\t[5] scale-bilinear\n\t[6] scale-bicubic\nOther Actions:\n\t[0] display buffer\n\t[99] write image to file\n")

    match char_input:
        case '1':
            ax = int(input("Enter anchor x in pixels: "))
            ay = int(input("Enter anchor y in pixels: "))
            tw = int(input("Enter target width: "))
            th = int(input("Enter target height: "))
            return partial(crop, anchor_x=ax, anchor_y=ay, target_width=tw, target_height=th)
        case '2':
            xaf = (input("Enter 'y' to flip along the x-axis: ") == 'y')
            yaf = (input("Enter 'y' to flip along the y-axis: ") == 'y')
            return partial(mirror, x_axis_flip = xaf, y_axis_flip = yaf)
        
        case '0':
            return display_buffer
        case '99':
            return None
        case _:
            return select_transformation()


def parse_arguments() -> tuple[Image, list[Callable[...,Image]]]:
    pass
