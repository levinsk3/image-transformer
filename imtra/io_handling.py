import random
import os
import sys

from PIL import Image
from tkinter import filedialog

from collections.abc import Callable
from functools import partial

from imtra.transformations import crop, mirror, shift, rotate, scale_nearest, scale_bilinear, scale_bicubic



def select_file(source_path=None) -> str:
    source_path = filedialog.askopenfilename(initialdir="./sample_images/",
                                                 filetypes=[("PNG Files", "*.png")])
    return source_path

def buffer_file(source_path):
    print(f"Opening {source_path}")
    image_buffer = Image.open(source_path).convert("RGBA")
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
    char_input = input("Select transformation:\n\t[1] crop\n\t[2] mirror\n\t[3] rotate\n\t[4] shift\n\t[5] scale-nearest\n\t[6] scale-bilinear\n\t[7] scale-bicubic\nOther Actions:\n\t[0] display buffer\n\t[99] write image to file\n")

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
        case '3':
            cc = (input("Enter 'y' to rotate counter-clokwise (default clokwise): ") == 'y')
            return partial(rotate, counter_clokwise=cc)
        case '4':
            sx = int(input("Enter shift ammount along the x axis: "))
            sy = int(input("Enter shift ammount along the y axis: "))
            return partial(shift, shift_x=sx, shift_y=sy)

        case '5':
            f = float(input("Enter the scaling factor: "))
            print("Working...")
            return partial(scale_nearest, factor=f)

        case '6':
            f = float(input("Enter the scaling factor: "))
            print("Working...")
            return partial(scale_bilinear, factor=f)

        case '7':
            f = float(input("Enter the scaling factor: "))
            print("Working...")
            return partial(scale_bicubic, factor=f)

        case '0':
            return partial(display_buffer)
        case '99':
            return None
        case _:
            return select_transformation()


def parse_arguments() -> tuple[str, list[Callable[...,Image]],str]:
    input_file = sys.argv[1]
    transformation_chain = sys.argv[2].split('+')
    write_file = sys.argv[3]

    transformation_stack = []
    for transformation in transformation_chain:
        action, parameters = transformation.split(':')
        
        match action:
            case "cr":
                ax, ay, tw, th = parameters.split(',')
                transformation_stack.append(partial(crop, anchor_x=int(ax), anchor_y=int(ay), target_width=int(tw), target_height=int(th)))
            case "mr":
                xaf = 'x' in parameters
                yaf = 'y' in parameters
                transformation_stack.append(partial(mirror, x_axis_flip = xaf, y_axis_flip = yaf))
            case "ro":
                cc = (parameters=="cc")
                transformation_stack.append(partial(rotate, counter_clokwise=cc))
            case "sh":
                sx, sy = parameters.split(',')
                transformation_stack.append(partial(shift, shift_x=int(sx), shift_y=int(sy)))
            case "sn":
                f = float(parameters)
                transformation_stack.append(partial(scale_nearest, factor=f))
            case "sl":
                f = float(parameters)
                transformation_stack.append(partial(scale_bilinear, factor=f))
            case "sc":
                f = float(parameters)
                transformation_stack.append(partial(scale_bicubic, factor=f))

    return (input_file, transformation_stack, write_file)
