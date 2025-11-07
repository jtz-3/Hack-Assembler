"""
A SymbolTable data structure for the nand2tetris Hack assembler. When implemented, this
will allow the user to use label definitions in their .asm files.

https://www.nand2tetris.org/_files/ugd/44046b_89a8e226476741a3b7c5204575b8a0b2.pdf
"""

class SymbolTable:
    def __init__(self):
        # Add predefined symbols.
        self.sym_table = {'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3,
                          'THAT': 4, 'R0': 0, 'R1': 1, 'R2': 2,
                          'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 
                          'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10,
                          'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14,
                          'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
        
        self.current_var_addr = 16

    def __setitem__(self, key, value):
        self.sym_table[key] = value

    def __getitem__(self, key):
        return self.sym_table[key]

    # add_variable: Adds the variable sym to the next available memory address
    # (beginning with the address 16)
    # (Possibly redundant)
    def add_variable(self, sym: str):
        self.sym_table[sym] =  self.current_var_addr
        self.current_var_addr += 1

    # check_table: Returns False if sym not found; or the address corresponding to sym
    # if it is in the table.
    def check_table(self, sym: str):
        try:
            return self.sym_table[sym]
        except KeyError:
            return False