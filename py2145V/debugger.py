from memory import pc, fetch
from register import register_index, register_value
from silicon import execute_single

# print helper
def led_display(rd : int):
    """Convert int value as 32 bit led string"""
    s = format(rd, "032b")
    leds = s.replace('0', ".").replace('1', '*')
    return leds

def info_reg(reg : str):
    """Display value of a register"""
    rd = register_index(reg)
    val = register_value(rd)
    print(format(reg, '4s'), led_display(val), format(val, '08x'), val)

def info_reg_tests():
    info_reg("s4")
    info_reg("zero")

def info_pc(pc : int):
    """Display value of the program instruction counter"""
    val = pc
    print(format("pc", '4s'), led_display(val), format(val, '08x'), val)

def info(regs = []):
    """Display values of a list of registers"""
    for reg in regs:
        info_reg(reg)

def info_tests():
    info(["s2", "s3", "s4"])

def debug(eop : int):
    """Debug program loaded into memory"""
    global pc
    print("debug start")
    #script break at 0 and continue
    while pc != eop: 
        pc_last = pc
        instruction = fetch()
        pc = execute_single(instruction)
        if (pc == pc_last):
            break
        #script break at 20, info reg s3, s4, continue
        if pc == 20:
            #info_pc(pc)
            #info_reg("s2")
            info_reg("s3")
            #info_reg("s5")
            info_reg("s4")
        #script break at eop
        if (pc > eop):
            break
    print("debug done")
