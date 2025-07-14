import sys
import logging
import PIL.Image as Image
import os
from tkinter import filedialog

logging.basicConfig(
    level = logging.DEBUG,
    stream = sys.stdout,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

Prompts = {
    'filepath' : "Write the absolute path of an image, or press enter to open explorer:\n",
    'action' : "Input 1 to transform, 2 to preview, 3 to output image:\n",
    'continue_editing' : "Input 'a' to edit another image, anything else to exit:\n",
}

def main():
    match len(sys.argv):
        case 1:
            logging.info("NO ARGUMENTS PROVIDED") # launch interactive mode
            interactive_mode()
        case _:
            logging.info("SOME ARGUMENTS PROVIDED") # parse and handle input
            for argument in sys.argv:
                continue

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
    edited_image = selected_image.copy()

    match action := input(Prompts['action']):
        case '1':
            print("Transform selection: 1:rotate 2:mirror 3:scale ...:")
            input()
        case '2':
            edited_image.show()
        case '3':
            print("Outfile: out.png, enter to confirm, m to modify name, c to continue editing:")
            input()
        case _:
            print("Command not recognized.")

    if input(Prompts['continue_editing']) == 'a':
        interactive_mode()

if __name__ == "__main__":
    main()
