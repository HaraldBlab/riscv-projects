import opcode
from opcode import op_add, op_addi, op_bge, op_lui, op_jal

# RV32I instruction formats encoders
def register_register(opcode : int, rd : int, func3 : int, rs1 : int, rs2 : int, func7 : int):
    """Register/Register format"""
    return (opcode & 0x7f) + ((rd & 0x1F) << 7) + ((func3 & 0x07) << 12) + ((rs1 & 0x1F) << 15) + ((rs2 & 0x1F) << 20) + ((func7 & 0x7F) << 25)

def immediate(opcode : int, rd : int, func3 : int, rs1 : int, imm12 : int):
    """Immediate 12 format"""
    return (opcode & 0x7f) + ((rd & 0x1F) << 7) + ((func3 & 0x07) << 12) + ((rs1 & 0x1F) << 15) + ((imm12 & 0x7FF) << 20)

def upper_immediate(opcode : int, rd : int, imm20 : int):
    """Upper immediate 20 format """
    return (opcode & 0x7f) + ((rd & 0x1F) << 7) + ((imm20 & 0x7FF) << 12)

def branch(opcode : int, func3 : int, rs1 : int, rs2 : int, imm16 : int):
    """Branch format"""
    return (opcode & 0x7f) + ((imm16 & 0x1F) << 7) + ((func3 & 0x07) << 12) + ((rs1 & 0x1F) << 15) + ((rs2 & 0x1F) << 20) + (((imm16 >> 5) & 0xFFF) << 25)

def jump(opcode : int, rd : int, imm21 : int):
    """Jump format"""
    return (opcode & 0x7f) + ((rd & 0x1F) << 7) + (((imm21 >> 12) & 0xFF) << 12) + (((imm21 >> 11) & 0x01) << 20) + (((imm21 >> 1) & 0x3FF) << 25) + (((imm21 >> 20) & 0x01)  << 31); 

# RV32I instruction set encoder
def add(rd : int, rs1 : int, rs2 : int):
    """create an add immediate instruction"""
    return register_register(op_add, rd, 0x0, rs1, rs2, 0x00)

def addi(rd : int, rs1 : int, imm12 : int):
    """create an add immediate instruction"""
    return immediate(op_addi, rd, 0x0, rs1, imm12)

def bge(rs1 : int, rs2 : int, imm16 : int):
    """create a branch greater equal 0 instruction from register and address"""
    return branch(op_bge, 0x05, rs1, rs2, imm16)

def lui(rd : int, imm : int):
    """create a load upper immediate instruction from register and address"""
    return upper_immediate(op_lui, rd, imm)

def jal(rd : int, imm21 : int):
    """create a jump to address instruction and place return address in rd."""
    return jump(op_jal, rd, imm21)

# RV32I instruction formats tests
def register_register_tests():
    """Tests for the register-register format"""
    print(register_register(15, 0, 1, 2, 3, 27))
    print(register_register(15, 0+32, 1, 2, 3, 27))

def immediate_tests():
    """Tests for the register-register format"""
    print(immediate(16, 0, 3, 1, 1234))
    print(immediate(16, 0+32, 3, 1, 1234))

def format_tests():
    """all the tests for the instruction forats """
    register_register_tests()
    immediate_tests()

import register
from register import a0
from register import t0
from register import s4

# RV32I instruction set tests
def set_tests():
    """Instruction set tests"""
    print(addi(a0, a0, 0x0001000))
    print(bge(s4, t0, 1234))
    print(lui(a0, 0x0004000))

    print(jal(t0, 0) & 0x7f)
    print(jal(t0, 3*4) & 0x7f)
    print(jal(t0, 11*4) & 0x7f)

