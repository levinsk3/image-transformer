import sys
import logging
from PIL import Image
import os
from tkinter import filedialog
import random


Prompts = {
    'filepath' : "Write the absolute path of an image, or press enter to open file explorer:\n",
    'action' : "ACTION LIST\n\t1 -> transform\n\t2 -> preview\n\t3 -> output image\n\t99 -> cancel without saving\nSelect action:\n",
    'edit_another' : "Input 'a' to edit another image, anything else to exit:\n",
    'transform_type' : "AVAILABLE TRANSFORMS\n\t1 -> rotate\n\t2 -> mirror\n\t3 -> crop\n\t4 -> scale\n\t0 -> cancel transform\nSelect transform:\n",
}



def output_image(image:Image):
    randompostfix = random.getrandbits(32)
    outfile = "./output/out_" + str(randompostfix) + ".png"
    os.makedirs(os.path.dirname("./output/"), exist_ok=True) #make output folder if nonexistent
    #TODO check for filename collision
    image.save(outfile, 'png')
    print(f"Image saved as {outfile}")
    return


def action_loop(image:Image):
    action = input(Prompts['action'])
    match action:
        case '1':
            transform_type = input(Prompts['transform_type'])
            match transform_type:
                case '1':
                    pass
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case '0':
                    pass
        case '2':
            image.show()
        case '3':
            output_image(image)
            return
        case '99':
            return
        case _:
            print("Command not recognized.")
    action_loop(image)

def interactive_mode():
    print("IMAGE TRANSFORMER INITIALIZED")

    match file_path := input(Prompts['filepath']):
        case '':
            file_path = filedialog.askopenfilename(
                title="Select an image to edit",
                initialdir=os.path.realpath('./tests/samples/'),
                filetypes=[("Image files", ("*.png", "*.jpg", "*.jpeg", "*.gif"))]
            )
        case _:
            pass

    # TODO check if file at file_path is valid
    print(f"Selected image: {file_path}")
    selected_image = Image.open(file_path)

    action_loop(selected_image.copy())

    if input(Prompts['edit_another']) == 'a':
        interactive_mode()
    else:
        return


def main():
    #TODO logging configuration based on flags?
    logging.basicConfig(
        level = logging.DEBUG,
        stream = sys.stdout,
        format = '%(asctime)s - %(levelname)s - %(message)s'
    )

    match len(sys.argv):
        case 1:
            logging.info("NO ARGUMENTS PROVIDED") # launch interactive mode
            interactive_mode()
        case _:
            logging.info("SOME ARGUMENTS PROVIDED") # parse and handle input
            for argument in sys.argv:
                continue

if __name__ == "__main__":
    main()
