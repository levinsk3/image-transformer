import sys

from imtra.io_handling import select_file, buffer_file, select_transformation, write_buffer, parse_arguments

def main():

    if len(sys.argv) == 1:
        
        input("Interactive Mode Initialized. Press Enter to select a file.")
        
        while source_path := select_file():
            image_buffer = buffer_file(source_path)
            
            while transformation := select_transformation():
                image_buffer = transformation(image_buffer)
            
            write_buffer(image_buffer)
            
            input("Press Enter to select another file. (Cancel the selection to exit.)")

        return 0

    else:

        try:
            source_path, transformation_stack, write_file = parse_arguments()
        except:
            print("Invalid arguments, exiting.")
            return 1

        image_buffer = buffer_file(source_path)
        
        for transformation in transformation_stack:
            image_buffer = transformation(image_buffer)
        write_buffer(image_buffer, write_file)

        return 0

if __name__ == "__main__":
    main()
