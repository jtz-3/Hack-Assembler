"""
Module to parse Hack assembly code into its components by
reading in xxx.asm files and breaking down each line into its
constituent parts for further processing. See the nand2Tetris
specification below:

https://www.nand2tetris.org/_files/ugd/44046b_7ef1c00a714c46768f08c459a6cab45a.pdf
"""
import re

# Necessary? just use file open method in main loop?
def read_asm(fname: str):
    return

# next_cmd: Takes a file-like object representing a .asm script and 
# returns the next instruction, or returns False if the end is reached.
def next_cmd(file):
    return

# cmd_fields: Takes a string representing a well-written C- or A-instruction, and
# returns a tuple containing the instruction type and field(s).
def cmd_fields(cmd: str):

    if cmd[0] == '@':
        cmd_type = 'A'
        fields = cmd[1:] 
    else:
        cmd_type = 'C'

        # Note:
        # 1. Instructions must be one of: comp, dest=comp, comp;jump, or dest=comp;jump.
        # 2. This logic only works if we assume that all Hack Assembly
        #    scripts being translated are error-free (as the project requires).
        fields = re.split(r'=', cmd)  
        
        if len(fields) == 2:
            d = fields[0]
            cmd = fields[1]
        else:
            d = ''
            cmd = fields[0]

        fields = re.split(r';', cmd)

        if len(fields) == 2:
            j = fields[1]
        else:
            j = ''
        
        c = fields[0]

        fields = [d,c,j]

    return (cmd_type, fields)