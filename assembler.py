"""
Assembler for the Hack machine language specification in nand2tetris. Uses the previously-developed
decoder and parser modules to take a xxx.asm file and output the corresponding xxx.hack binary.

Note: Any assembly files supplied are presumed to be correctly written according to the Hack machine language
      specification.

https://www.nand2tetris.org/_files/ugd/44046b_7ef1c00a714c46768f08c459a6cab45a.pdf

"""

import parser
import decode
import sys

if len(sys.argv) != 2:
    print('Error: Must specify a .asm file to assemble.')
else:
    file_name = sys.argv[1]
    asm_file = parser.read_asm(sys.argv[1])

    instructions = asm_file.readlines()
    num_insts = len(instructions)

    hack_file = open(file_name[:-4] + '.hack', 'w')

    for i in range(num_insts):
        current_inst = instructions[i].strip(' \n')

        # Skip comments and whitespace
        if current_inst.startswith('//') or not current_inst:
            next
        else:
            current_inst = parser.inst_fields(current_inst)

            if current_inst[0] == 'A':
                next_out = decode.a_instruction(current_inst[1])
            else:
                dest = current_inst[1][0]
                comp = current_inst[1][1]
                jump = current_inst[1][2]

                c = decode.comp(comp)
                d = decode.dest(dest)
                j = decode.jump(jump)

                next_out = '111' + c + d + j

            if i < num_insts - 1:
                next_out += '\n'

            hack_file.write(next_out)

    hack_file.close()