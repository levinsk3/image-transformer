import random
import os
import sys

from PIL import Image
from tkinter import filedialog
import readchar

from collections.abc import Callable
from functools import partial

from imtra.transformations import crop, mirror, rotate, shift, scale_nearest, scale_bilinear, scale_bicubic


Prompts = {
    "select-transformation" : "Select transformation:\n\t[1] crop\n\t[2] mirror\n\t[3] rotate\n\t[4] shift\n\t[5] scale-nearest\n\t[6] scale-bilinear\n\t[7] scale-bicubic\n\n\t[0] display buffer\n\t[99] write image to file\n",
}

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

def write_buffer(image_buffer:Image, write_file:str=None):
    if write_file is None:
        random_write_file = "out_" + str(random.getrandbits(32))
        write_file = filedialog.asksaveasfilename(initialdir="./output/",
                                                  initialfile=random_write_file,
                                                 filetypes=[("PNG Files", "*.png")])
    image_buffer.save(write_file)
    print(f"Buffer saved as {write_file}.")

    
def select_transformation() -> Callable[...,Image]:
    char_input = input(Prompts["select-transformation"])

    match char_input:
        case '1':
            ax = int(input("Enter anchor x: "))
            ay = int(input("Enter anchor y: "))
            w = int(input("Enter target width: "))
            h = int(input("Enter target height: "))
            return partial(crop, anchor_x=ax, anchor_y=ay, width=w, height=h)
        
        case '0':
            return display_buffer
        case '99':
            return None

    
    return None


def parse_arguments() -> tuple[Image, list[Callable[...,Image]]]:
    pass
