import random
import os

from PIL import Image
from tkinter import filedialog

from collections.abc import Callable

from imtra.transformations import crop, mirror, rotate, shift, scale_nearest, scale_bilinear, scale_bicubic


Prompts = {
    'filepath' : "Write the absolute path of an image to edit [default is ...]:\n",
    'action' : "ACTION LIST\n\t1 -> transform\n\t2 -> preview\n\t3 -> output image\n\t99 -> cancel without saving\nSelect action:\n",
    'edit_another' : "Input 'a' to edit another image, anything else to exit:\n",
    'transform_type' : "AVAILABLE TRANSFORMS\n\t1 -> rotate\n\t2 -> mirror\n\t3 -> crop\n\t4 -> scale\n\t0 -> cancel transform\nSelect transform:\n",
}

def select_file(source_path=None) -> str:
    source_path = filedialog.askopenfilename(initialdir="./tests/samples/",
                                                 filetypes=[("PNG Files", "*.png")])
    return source_path

def buffer_file(source_path):
    print(f"Opening {source_path}")
    image_buffer = Image.open(source_path)
    return image_buffer

def select_transformation() -> Callable[...,Image]:
    pass

def buffer_write(image_buffer:Image, write_file:str=None):
    if write_file is None:
        random_write_file = "out_" + str(random.getrandbits(32))
        write_file = filedialog.asksaveasfilename(initialdir="./output/",
                                                  initialfile=random_write_file,
                                                 filetypes=[("PNG Files", "*.png")])
    image_buffer.save(write_file)

def parse_arguments() -> tuple[Image, list[Callable[...,Image]]]:
    pass
