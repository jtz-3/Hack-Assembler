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
    if fname[-4:] != '.asm':
        print('Error: File is not a .asm file.')
        return None
    try:
        return open(fname, 'r')
    except FileNotFoundError:
        print("Error: File '%s' not found." % fname)
        return None

# next_inst: Takes a a list consisting of lines read in from a .asm file
#            and returns:
#   - The next line, if it exists
#   - None, if the next line is a comment or whitespace
#   - False, if the end of file is reached
# Note: modifies inst_list in place by removing inst_list[0].
def next_inst(inst_list):
    try:
        next_line = inst_list.pop(0)
        stripped_line = next_line.strip(' \n')
        if stripped_line.startswith('//') or not stripped_line:
            return None
    except IndexError:
        return False

# inst_fields: Takes a string representing a well-written C- or A-instruction, and
# returns a tuple containing the instruction type and field(s).
def inst_fields(inst: str):

    if inst[0] == '@':
        inst_type = 'A'
        fields = inst
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