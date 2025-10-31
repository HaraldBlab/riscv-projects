# the program counter
pc = 0x0000
# the end of program
eop = 0x0000
# the program in memory
program = [0 for x in range(64)]

def incpc():
    """Move the program counter to the next instruction position"""
    global pc
    pc = pc + 4
    return pc

def setpc(addr: int):
    """Set the proram counter to an address"""
    global pc
    pc = addr
    return pc

def fetch():
    """Fetch the next instruction from program memory"""
    global program, pc
    return  program[pc // 4]

def load(instructions = []):
    """Load the list of insturctions into program memory and returns the end of program"""
    global program, eop
    program = [x for x in instructions]
    eop = 4 * (len(program)-1)
    return eop
