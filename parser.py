"""
Module to parse Hack assembly code into its components by
reading in xxx.asm files and breaking down each line into its
constituent parts for further processing. See the nand2Tetris
specification below:

https://www.nand2tetris.org/_files/ugd/44046b_7ef1c00a714c46768f08c459a6cab45a.pdf
"""
import re

# read_asm: Attempts to read in a given .asm file, throwing an error
# if the file doesn't exist or is in the incorrect format
def read_asm(fname: str):
    if fname[-4:] is not '.asm':
        print('Error: File is not a .asm file.')
        return None
    try:
        return open(fname, 'r')
    except FileNotFoundError:
        print("Error: File '%s' not found." % fname)
        return None

# next_inst: Takes a file-like object representing a .asm script and 
# returns the next instruction (stripped of whitespace), or returns None
# if the line is a comment, or returns False if end of file is reached.
def next_inst(file):
    try:
        new_line = next(file)
        stripped_line = new_line.strip(' \n')
        if stripped_line.startswith('//') or not stripped_line:
            return None
        return stripped_line
    except StopIteration:
        return False

# inst_fields: Takes a string representing a well-written C- or A-instruction, and
# returns a tuple containing the instruction type and field(s).
def inst_fields(inst: str):

    if inst[0] == '@':
        inst_type = 'A'
        fields = inst[1:] 
    else:
        inst_type = 'C'

        # Note:
        # 1. Instructions must be one of: comp, dest=comp, comp;jump, or dest=comp;jump.
        # 2. This logic only works if we assume that all Hack Assembly
        #    scripts being translated are error-free (as the project requires).
        fields = re.split(r'=', inst)  
        
        if len(fields) == 2:
            d = fields[0]
            inst = fields[1]
        else:
            d = ''
            inst = fields[0]

        fields = re.split(r';', inst)

        if len(fields) == 2:
            j = fields[1]
        else:
            j = ''
        
        c = fields[0]

        fields = [d,c,j]

    return (inst_type, fields)