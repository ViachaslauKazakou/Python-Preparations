import dis
from bytecode import Instr, Bytecode

bytecode = Bytecode([Instr("LOAD_NAME", 'print'),
                     Instr("LOAD_CONST", 'Hello World!'),
                     Instr("CALL_FUNCTION", 1),
                     Instr("POP_TOP"),
                     Instr("LOAD_CONST", None),
                     Instr("RETURN_VALUE")])
code = bytecode.to_code()
exec(code)


def sum_2(x,y):
    return x+y


dis.dis(sum_2)


def print_word(name):
    print(name)


dis.dis(print_word)