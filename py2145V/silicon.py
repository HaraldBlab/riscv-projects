import opcode
from opcode import op_add, op_addi, op_bge, op_lui, op_jal

import register
from register import register_values

import decoder
from decoder import decode_register_register, decode_immediate, decode_branch, decode_jump, decode_upper_immediate

import memory
from memory import incpc, setpc

def execute_single(instruction : int, verbose : int = 0):
    """execute a instructions at pc. returns the new pc"""
    opcode = instruction & 0x7F
    if (opcode == op_add):
        decoded = decode_register_register(instruction)
        register_values[decoded["rd"]] = register_values[decoded["rs1"]] + register_values[decoded["rs2"]]
        if (verbose > 0):
            print(decoded, ":", register_values[decoded["rd"]])
        pc = incpc()
    elif opcode == op_addi:
        decoded = decode_immediate(instruction)
        register_values[decoded["rd"]] = register_values[decoded["rs1"]] + decoded["imm12"]
        if (verbose > 0):
            print(decoded, ":", register_values[decoded["rd"]])
        pc = incpc()
    elif opcode == op_bge:
        decoded = decode_branch(instruction)
        if register_values[decoded["rs1"]] >=  register_values[decoded["rs2"]]:
            pc = setpc(decoded["imm16"])
        else:
            pc = incpc()
        if (verbose > 0):
            print(decoded, "pc:", pc)
    elif opcode == op_jal:
        pc = 0
        decoded = decode_jump(instruction)
        register_values[decoded["rd"]] = pc
        pc = setpc(decoded["imm21"])    
        if (verbose > 0):
            print(decoded, "pc:", pc)
    elif opcode == op_lui:
        decoded = decode_upper_immediate(instruction)
        register_values[decoded["rd"]] =  decoded["imm20"]
        if (verbose > 0):
            print(decoded, ":", register_values[decoded["rd"]])
        pc = incpc()
    else:
        print("illegal instruction", format(opcode, "02x"))
    return pc
