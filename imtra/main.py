




from imtra.io_handling import Prompts write_image



def main():
#    logging.basicConfig(
#        level = logging.DEBUG,
#        stream = sys.stdout,
#        format = '%(asctime)s - %(levelname)s - %(message)s'
#    )

    if len(sys.argv) == 1:
#        logging.info("NO ARGUMENTS PROVIDED") # launch interactive mode
        print("Interactive Mode Initialized")
        while image_buffer := select_file():
            while transformation := select_transformation():
                apply_transformation(image_buffer, transformation)
            buffer_write(image_buffer)

    else:
#        logging.info("SOME ARGUMENTS PROVIDED") # parse and handle input
        if arguments_are_valid() == False:
            return
        source_file, transformation_stack, write_file = parse_arguments()
        image_buffer = select_file(source_file)
        for transformation in transformation_stack:
            apply_transformation(image_buffer, transformation)
        buffer_write(image_buffer, write_file)

if __name__ == "__main__":
    main()
