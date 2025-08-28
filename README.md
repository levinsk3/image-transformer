# Image Transformer: NMIN112 Credit Project

## Overview
Image Transformer (imtra) is a python project for editing png images. It serves as a proof of concept for the implementation of multiple transformations, with focus on functional approach within the boundaries of python, and self-documenting code.

## Project Setup

1. Clone this repository:

```bash
git clone https://github.com/levinsk3/image-transformer.git
cd ./image_transformer
```
2. Install Dependencies

```bash
pip install -r requirements.txt
```
Note that this project requires a tkinter-compatible version of python.

## Usage

### Interactive Mode
This is the primary way to use this project. To launch interactive mode, from the repository root, run:
```bash
python -m imtra.main
```
and follow the instructions.

### Streamlined Mode
To edit images directly, run:
```bash
python -m imtra.main ARGUMENT1 ARGUMENT2 ARGUMENT3
```
Where:

ARGUMENT1 is the path to the image to be sourced.

ARGUMENT3 is the file path to be writen to after applying all transformations.

ARGUMENT2 is a string of transformations and parameters, with the following syntax:

"TRANSFORMATION:FIRSTPARAMETER,SECONDPARAMETER,...+"

Chained together, one for each desired transformation, in the order of execution (see example below the table).

Viable transformations and their correspoding parameters are:
| Transformation             | Shortcut to use | Parameters                     | Specification                                  |
|----------------------------|-----------------|--------------------------------|------------------------------------------------|
| Crop                       | cr              | x-anchor,y-anchor,width,height | mandatory, replace with positive integers      |
| Mirror                     | mr              | x \| y \| xy                   | pick one, to flip along the corresponding axis |
| Rotate                     | ro              | cw \| cc                       | pick one, clockwise or counter-clokwise        |
| Shift                      | sh              | distance-x, distance-y         | mandatory, replace with integers               |
| Scale (nearest-neightbour) | sn              | factor                         | mandatory, replace with a positive float       |
| Scale (bilinear)           | sl              | factor                         | mandatory, replace with a positive float       |
| Scale (bicubic)            | sc              | factor                         | mandatory, replace with a positive float       |


For example, running:

```bash
python -m imtra.main ./sample_images/tree.png sn:1.3+sh:200,300+ro:cc ./output/scaled_shifted_rotated_tree.png
```

Scales the image by the factor of 1.3, shifts it by 200x300 pixels, and rotates it counter-clokwise.

## Technical Documentation

### Architecture

There are three modules that constitute this project. The main module provides the wiring and the interaction loops for both modes as described above. The io_handling module contains all functions dealing with input and output, both from the user, as well as the system. The transformations module contains all implemented transformations.

### Design Approach

This project focuses on applying functional programming principles, within some reasonable boundaries. This has proven most useful within transformation selection functions in the io_handling module, and, subjectively, in the overall legibility of the program, which skips the need to consider internal state. The only exception to the latter is the main image buffer. No object oriented constructions were used, except for the PIL Image class and the related PixelAccess class. All custom functions have no interrim effect on the rest of the program, with which they are in relation only through their inputs and outputs. The main function does effect the rest of the system through the writing of images, which is obviously desirable.
There is an emphasis on full-word, descriptive naming of functions and variables, to minimize the need for comments and provide self-documenting code. This greatly improves orientation when reading, especially within more complex functions, since it unloads the reader's working memory.

### Existing Code Use

The core external library allowing this project to function is the PIL library. The primary goal of this project was the implementation of several transformations and their wrapper, which contradicts the fact, that this library already implements most of the functionality via predefined functions. Using those predefined functions would make writing the project redundant, therefore PIL has only been utilized for the Image class for buffering the image, and pixel-level access to buffered images for the implementation of the transformations.
