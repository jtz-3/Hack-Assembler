"""
Assembler for the Hack machine language specification in nand2tetris. Uses the previously-developed
decoder and parser modules to take a xxx.asm file and output the corresponding xxx.hack binary.

Note: Any assembly files supplied are presumed to be correctly written according to the Hack machine language
      specification.

https://www.nand2tetris.org/_files/ugd/44046b_7ef1c00a714c46768f08c459a6cab45a.pdf

"""

import parser
import decode
from symboltable import *
import sys

if len(sys.argv) != 2:
    print('Error: Must specify a .asm file to assemble.')
else:
    file_name = sys.argv[1]
    asm_file = parser.read_asm(sys.argv[1])

    instructions = asm_file.readlines()
    num_lines = len(instructions)   # Should be num_lines
    inst_num = 0

    hack_file = open(file_name[:-4] + '.hack', 'w')
    symtab = SymbolTable()

    # First pass, to add undefined label symbols to the SymbolTable:
    # - Strip the current line of whitespace.
    # - If it starts with (, it is a label declaration -- check/update SymbolTable accordingly.
    # - If it is not a comment (i.e. an A- or C-instruction), update the number of *instructions*
    #   (to assign any labels appropriately)
    for i in range(num_lines):
        current_line = instructions[i].strip(' \n')

        if current_line.startswith('('):
            sym = current_line.strip('()')

            if not symtab.check_table(sym):
                symtab[sym] = inst_num
        elif not current_line.startswith('//') and current_line:
            inst_num += 1

    # Second pass, to add variable symbols to the table and assemble the code
    for i in range(num_lines):
        current_inst = instructions[i].strip(' \n')

        # Skip comments, whitespace, and label declarations
        if current_inst.startswith(('//', '(')) or not current_inst:
            next
        else:
            current_inst = parser.inst_fields(current_inst)

            if current_inst[0] == 'A':
                addr = current_inst[1][1:]

                # If a variable was mentioned, substitute it (defining it if necessary)
                if not addr.isdigit():
                    var = symtab.check_table(addr)
                    if var is False:
                        symtab.add_variable(addr)
                    next_out = decode.a_instruction('@' + str(symtab[addr]))
                else:
                    next_out = decode.a_instruction(current_inst[1])
            else:
                dest = current_inst[1][0]
                comp = current_inst[1][1]
                jump = current_inst[1][2]

                c = decode.comp(comp)
                d = decode.dest(dest)
                j = decode.jump(jump)

                next_out = '111' + c + d + j

            if i < num_lines - 1:
                next_out += '\n'

            hack_file.write(next_out)
    
    hack_file.close()