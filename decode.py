"""
Module to handle translating Hack assembly code into its 
binary equivalent, according to tables 4.3, 4.4, and 4.5 in the 
nand2Tetris specification below:

https://www.nand2tetris.org/_files/ugd/44046b_7ef1c00a714c46768f08c459a6cab45a.pdf

Each function takes a string input of the dest, comp, and jump fields and
return the corresponding binary bits.
"""

comp_table = {'0': '0101010', '1': '0111111', 
              '-1': '0111010', 'D': '0001100',
              'A': '0110000', 'M': '1110000',
              '!D': '0001101', '!A': '0110001', 
              '!M': '1110001','-D': '0001111',
              '-A': '0110011', '-M': '1110011',
              'D+1': '0011111', 'A+1': '0110111', 
              'M+1': '1110111', 'D-1': '0001110', 
              'A-1': '0110010', 'M-1': '1110010',
              'D+A': '0000010', 'D+M': '1000010', 
              'D-A': '0010011', 'D-M': '1010011',
              'A-D': '0000111', 'M-D': '1000111',
              'D&M': '1000000', 'D&A': '0000000',
              'D|A': '0010101', 'D|M': '1010101'}

dest_table = {'': '000', 'M': '001', 
            'D': '010', 'MD': '011',
            'A': '100', 'AM': '101', 
            'AD': '110', 'AMD': '111'}
        
jump_table = {'': '000', 'JGT': '001', 
              'JEQ': '010', 'JGE': '011',
              'JLT': '100', 'JNE': '101', 
              'JLE': '110', 'JMP': '111'}

# comp: Return the binary translation of the 'comp' part of a C-instruction.
def comp(comp_str: str):
    return comp_table[comp_str]

# dest: Return the binary translation of the 'dest' part of a C-instruction.
def dest(dest_str: str):
    return dest_table[dest_str]

# jump: Return the binary translation of the 'jump' part of a C-instruction.
def jump(jump_str: str):
    return jump_table[jump_str]

# a_instruction: Translate a string representing an A-instruction.
def a_instruction(inst: str):
    inst = inst[1:]
    bin_addr = bin(int(inst))[2:]
    return '0' + bin_addr.rjust(15, '0')