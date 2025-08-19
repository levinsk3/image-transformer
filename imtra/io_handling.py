import random
import os

from PIL import Image

Prompts = {
    'filepath' : "Write the absolute path of an image to edit [default is ...]:\n",
    'action' : "ACTION LIST\n\t1 -> transform\n\t2 -> preview\n\t3 -> output image\n\t99 -> cancel without saving\nSelect action:\n",
    'edit_another' : "Input 'a' to edit another image, anything else to exit:\n",
    'transform_type' : "AVAILABLE TRANSFORMS\n\t1 -> rotate\n\t2 -> mirror\n\t3 -> crop\n\t4 -> scale\n\t0 -> cancel transform\nSelect transform:\n",
}

def select_filepath() -> str:
    pass

def buffer_image(image_buffer:str) -> Image:
    pass

def write_image(image_buffer:Image, file_name:str=".", output_directory:str="./output/"):
    os.makedirs(os.path.dirname(output_directory), exist_ok=True) #make output folder if nonexistent
    output_filename = "out_" + str(random.getrandbits(32)) + ".png"
    #TODO check for filename collision
    image.save(outfile, "png")
    print(f"Image saved as {output_filename} in {output_directory}.")
    return

def kill_buffer(image_buffer:Image):
    pass

def oneline_sanity_check() -> bool:
    pass
