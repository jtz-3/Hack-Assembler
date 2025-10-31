import parser
import decode
import sys

if len(sys.argv) != 2:
    print('Error: Must specify a .asm file to assemble.')
else:
    # Throw an error in read_asm or return false or smth to check if file name is correct.
    asm_file = parser.read_asm(sys.argv[1])
    next_line = parser.next_inst(asm_file)

    while True:
        if not next_line:
            break
        else:
            if next_line == None:
                pass
            else:
                pass