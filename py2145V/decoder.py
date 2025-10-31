import opcode
from opcode import op_add, op_addi, op_bge, op_lui, op_jal

import register
from register import register_values

# RV32I instruction format decoder
def decode_register_register(instruction : int):
    """Decode instruction in register register format"""
    #return (opcode & 0x7f) + ((rd & 0x1F) << 7) + ((func3 & 0x07) << 12) + ((rs1 & 0x1F) << 15) + ((rs2 & 0x1F) << 20) + ((func7 & 0x7F) << 25)
    opcode = instruction & 0x7F
    rd = (instruction >> 7) & 0x1F
    func3 = (instruction >> 12) & 0x07
    rs1 = (instruction >> 15) & 0x1F
    rs2 = (instruction >> 20) & 0x1F
    func7 = (instruction >> 25) & 0x7F
    return { "opcode" : opcode, "rd" : rd, "func3" : func3, "rs1" : rs1, "rs2" : rs2, "func7" : func7}

def decode_immediate(instruction : int):
    """Decode instruction in immediate format"""
    #return (opcode & 0x7f) + ((rd & 0x1F) << 7) + ((func3 & 0x07) << 12) + ((rs1 & 0x1F) << 15) + ((imm12 & 0x7FF) << 20)
    opcode = instruction & 0x7F
    rd = (instruction >> 7) & 0x1F
    func3 = (instruction >> 12) & 0x07
    rs1 = (instruction >> 15) & 0x1F
    imm12 = (instruction >> 20) & 0x7FF
    return { "opcode" : opcode, "rd" : rd, "func3" : func3, "rs1" : rs1, "imm12" : imm12}

def decode_upper_immediate(instruction : int):
    """Decode instruction in upper immediate 20 format """
    #return (opcode & 0x7f) + ((rd & 0x1F) << 7) + ((imm20 & 0x7FF) << 12)
    opcode = instruction & 0x7F
    rd = (instruction >> 7) & 0x1F
    imm20 = (instruction >> 12) & 0x7FF
    return { "opcode" : opcode, "rd" : rd, "imm20" : imm20}

def decode_branch(instruction : int):
    """Decode instruction in branch format"""
    #return (opcode & 0x7f) + ((imm16 & 0x1F) << 7) + ((func3 & 0x07) << 12) + ((rs1 & 0x1F) << 15) + ((rs1 & 0x1F) << 20) + (((imm16 >> 5) & 0xFFF) << 25)
    opcode = instruction & 0x7F
    imm16_lo = (instruction >> 7) & 0x1F
    func3 = (instruction >> 12) & 0x07
    rs1 = (instruction >> 15) & 0x1F
    rs2 = (instruction >> 20) & 0x1F
    imm16_hi = (instruction >> 25) & 0x7FF
    imm16 = (imm16_hi << 5) + imm16_lo
    return { "opcode" : opcode, "func3" : func3, "rs1" : rs1, "rs2" : rs2, "imm16" : imm16}

def decode_jump(instruction : int):
    """Decode instruction in jump format"""
    # return (opcode & 0x7f) + ((rd & 0x1F) << 7) + (((imm21 >> 12) & 0xFF) << 12) + (((imm21 >> 11) & 0x01) << 20) + (((imm21 >> 1) & 0x3FF) << 25) + (((imm21 >> 20) & 0x01)  << 31); 
    opcode = instruction & 0x7F
    rd = (instruction >> 7) & 0x1F
    imm21_lo = (instruction >> 12) & 0xFF
    imm21_11 = (instruction >> 20) & 0x01
    imm21_1 = (instruction >> 25) & 0x3FF
    imm21_20 = (instruction >> 31) & 0x01
    imm21 = (imm21_lo << 12) + (imm21_11 << 1) + (imm21_1 << 1) + (imm21_20 << 20)
    return { "opcode" : opcode, "rd" : rd, "imm21" : imm21}
