

from encoder import add, addi, bge, lui, jal

from memory import load

from silicon import execute_single

from register import register_values

from register import a0, a1
from register import s2, s3, s4, s5
from register import t0
from register import zero

def execute(instructions=[]):
    """execute a sequence of instructions"""
    pc = 0
    for instruction in instructions:
        # fetch instruction at pc
        pc = execute_single(instruction)
        print("pc =", pc)

def execute_single_test():
    register_values[a0] = 0
    register_values[a1] = 1
    instruction = addi(a0, a1, 2)
    print("a0 =", register_values[a0])
    print("a1 =", register_values[a1])
    print("execute addi(a0, a1, 2)")
    execute_single(instruction)
    print("a0 =", register_values[a0])

def execute_test():
    register_values[s2] = 7
    register_values[s3] = 7
    instructions = [lui(s2, 0), lui(s3, 1)]
    print("s2 =", register_values[s2])
    print("s3 =", register_values[s3])
    print("execute [lui(s2, 0), lui(s3, 1)]")
    execute(instructions)
    print("s2 =", register_values[s2])
    print("s3 =", register_values[s3])

# sample fibonacci10
fibonacci10 = [
    lui(s2, 0),
    lui(s3, 1),
    lui(s4, 2),
    # loop = 3*4
    add(s5, zero, s3),
    add(s3, s3, s2),
    add(s2, zero, s5),
    # 6*4   
    lui(t0, 10),
    bge(s4, t0, 10*4),
    addi(s4, s4, 1),    #add(s4,zero,1)
    jal(t0, 3*4),
    # end: 10*4
    jal(t0, 10*4)
]

def execute_fibonacci10():
    print("running fib(10)")
    execute(fibonacci10)

# assembler
import assembler

riscv = [
    "lui   s2, 0",
    "lui   s3, 1",
    "lui   s4, 2",
    "",
    "loop:",
    "add   s5, zero, s3",
    "add   s3, s3, s2",
    "add   s2, zero, s5",
    "",
    "lui   t0, 10",
    "bge   s4, t0, end",
    "addi  s4, s4, 1",
    "jal   loop",
    "",
    "end:",
    "jal   end",
    ]

def process_riscv():
    print("asm fib(10)", assembler.process(riscv))
    print("fibonacci10", fibonacci10)

#process_riscv()

asm = [
    "li   s2, 0",
    "li   s3, 1",
    "li   s4, 2",
    "",
    "loop:",
    "mv   s5, s3",
    "add  s3, s3, s2",
    "mv   s2, s5",
    "",
    "li   t0, 10",
    "bge  s4, t0, end",
    "addi s4, s4, 1",
    "j    loop",
    "",
    "end:",
    "j    end",
]

def prepocess_asm():
    print("gnu asm fib(10):", assembler.prepocess(asm))
    print("riscv   fib(10):", riscv)

prepocess_asm()


# debugger
from debugger import debug

def debug_fibonacci10():
    print("debug fib(10)")
    eop = load(fibonacci10)
    debug(eop)

#debug_fibonacci10()
