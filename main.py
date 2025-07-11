import sys
import logging

logging.basicConfig(
    level = logging.DEBUG,
    stream = sys.stdout,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    match len(sys.argv):
        case 1:
            logging.info("NO ARGUMENTS PROVIDED")
            # launch interactive mode
            interactive_mode()
        case _:
            logging.info("SOME ARGUMENTS PROVIDED")
            # parse and handle input
            for argument in sys.argv:
                continue

def interactive_mode():
    print("Image Transformer Initialized")

    print("Select image file:")
    input()

    print("Select action: 1:transform 2:preview 3:output")

    match input():
        case '1':
            print("Transform selection: 1:rotate 2:mirror 3:scale ...:")
            input()
        case '2':
            print("[Display image preview ?in console? if possible]")
            input()
        case '3':
            print("Outfile: out.png, enter to confirm, m to modify name, c to continue editing:")
            input()
        case _:
            print("Command not recognized.")

    if go_again := input("Enter 'y' to edit another image, anything else to exit:\n")\
        == 'y':
        interactive_mode()

if __name__ == "__main__":
    main()
