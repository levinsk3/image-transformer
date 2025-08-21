import sys

from imtra.io_handling import select_file, buffer_file, select_transformation, write_buffer, parse_arguments

def main():
#    logging.basicConfig(
#        level = logging.DEBUG,
#        stream = sys.stdout,
#        format = '%(asctime)s - %(levelname)s - %(message)s'
#    )

    if len(sys.argv) == 1:
#        logging.info("NO ARGUMENTS PROVIDED") # launch interactive mode
        
        input("Interactive Mode Initialized. Press Enter to select a file.")
        
        while source_path := select_file():
            image_buffer = buffer_file(source_path)
            
            while transformation := select_transformation():
                image_buffer = transformation(image_buffer)
            
            write_buffer(image_buffer)
            
            input("Press Enter to select another file. (Cancel the selection to exit.)")

        return 0

    else:
#        logging.info("SOME ARGUMENTS PROVIDED") # parse and handle input

        try:
            source_path, transformation_stack, write_path = parse_arguments()
        except:
            print("Invalid arguments, exiting.")
            return 1

        image_buffer = buffer_file(source_path)
        
        for transformation, parameters in transformation_stack:
            apply_transformation(image_buffer, transformation)
        write_buffer(image_buffer, write_file)

        return 0

if __name__ == "__main__":
    main()
