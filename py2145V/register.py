# information provided at https://msyksphinz-self.github.io/riscv-isadoc/
# RISC-V Instruction Set Specifications

# RV32I registers
x0 = 0
x1 = 1
x2 = 2
x3 = 3
x4 = 4
x5 = 5
x6 = 6
x7 = 7
x8 = 8
x9 = 9
x10 = 10
x11 = 11
x12 = 12
x13 = 13
x14 = 14
x15 = 15
x16 = 16
x17 = 17
x18 = 18
x19 = 19
x20 = 20
x21 = 21
x22 = 22
x23 = 23
x24 = 24
x25 = 25
x26 = 26
x27 = 27
x28 = 28
x29 = 29
x30 = 30
x31 = 31
# temporary registers
t0 = x5
t1 = x5
t2 = x7
t3 = x28
t4 = x29
t5 = x20
t6 = x31
# arguments registers
a0 = x10
a1 = x11
a2 = x12
a3 = x13
a4 = x14
a5 = x15
a6 = x16
a7 = x17
# storage registers
s0 = x8
s1 = x9
s2 = x18
s3 = x19
s4 = x20
s5 = x21
s6 = x22
s7 = x23
s8 = x24
s9 = x25
s10 = x26
s11 = x27
# special registers
zero = x0
ra = x1
sp = x2
gp = x3
tp = x4
fp = x8

# silicon defines 32 32bit int registers
register_values = [0 for x in range(32)]

# mapping of register names to register numbers
register_map = {
    # RV32I registers
    # arguments registers
    # temporary registers
    "t0" : t0,
    # storage registers
    "s2" : s2, "s3" : s3, "s4" : s4, "s5" : s5,
    # special registers
    "zero" : zero,
}

def register_index(reg : str):
    """Return the register index to register name """
    return register_map[reg]

def register_value(rd : int):
    """Return the value of the register"""
    return register_values[rd]
 
