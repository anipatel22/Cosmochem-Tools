# Cosmochem-Tools
This repository contains python tools relevant to research at the cross section of cosmochemistry and nuclear astrophysics.

To use any of these codes, download the relevant file and place it in the same folder as your working python file or notebook. Then import into your file or notebook using ' from file.name import * ' to import all the functions. For data_processor.py, the line would be ' from data_processor import * '

data_processor.py contains functions that are useful in processing isotopic data. Cosmochemists often work with isotopic data normalized to some standard (delta, epsilon, and mu notation). Astrophysicits and astronmers generally work with mass fraction ratios (not normalized to a standard). This module contains functions that convert between the two data formats (taking lists as inputs). It also contains functions to get absolute mass fractions from mass fraction ratios and vice versa. Will be updated with additional relevant functions in the future.
