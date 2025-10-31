import encoder
from encoder import jal, lui, add, addi, bge

import register
from register import register_index
from register import zero

# parser
def parse(statement : str):
    """Parse a statemnt ad return a list of token"""
    token = statement.split()
    return token

# gnu assembler

def print_line(label : str, parts = []):
    """Build a single line from a label and the list of parts"""
    b1 = 0 # column mnemonic (1st part)
    b2 = 6 # column 1st operand (2nd part)
    line = ""
    if (len(label) > 0):
        line = label
    else:
        line = " " *b1
    n = 0
    for part in parts:
        if n == 0:
            line = line + " "*b1 + part
        elif n == 1:
            line = line + " "*(b2-l) + part
        else:
            line = line + " " + part
        n = n + 1
        l = len(part)
    #print(line)
    return line

def prepocess(statements = [], verbose = 0):
    """Preprocess a gnu assembly listing to a RISC-V assembly listing file"""
    line = 0
    pc = 0
    symbol_map = { "start" : pc}
    out_statements = []
    for statement in statements:
        line += 1
        token = parse(statement)
        if (len(token) == 0):
            out_statements.append('')
            continue
        if (len(token) == 1):
            out_statements.append( print_line(token[0], []))
            if (verbose > 0):
                print(line, ":", token[0])
        elif (len(token) == 2):
            if (token[0] == "j"):
                out_token = ["ja1", token[1]]
                out_statements.append(print_line("", out_token))
                if (verbose > 0):
                    print(line, ":", out_token[0], out_token[1])
        elif (len(token) == 3):
            if (token[0] == "li"):
                out_token = ["lui", token[1], token[2]]
                out_statements.append(print_line("", out_token))
                if (verbose > 0):
                    print(line, ":", out_token[0], out_token[1], out_token[2])
            if (token[0] == "mv"):
                out_token = ["add", token[1], "zero,", token[2]]
                out_statements.append(print_line("", out_token))
                if (verbose > 0):
                    print(line, ":", out_token[0], out_token[1], out_token[2], out_token[2])
        elif (len(token) == 4):
            if (token[0] == "add"):
                out_token = ["add", token[1], token[2], token[3]]
                out_statements.append(print_line("", out_token))
                if (verbose > 0):
                    print(line, ":", out_token[0], out_token[1], out_token[2], out_token[2])
            if (token[0] == "addi"):
                out_token = ["addi", token[1], token[2], token[3]]
                out_statements.append(print_line("", out_token))
                if (verbose > 0):
                    print(line, ":", out_token[0], out_token[1], out_token[2], out_token[2])
            if (token[0] == "bge"):
                out_token = token
                out_statements.append(print_line("", out_token))
                if (verbose > 0):
                    print(line, ":", out_token[0], out_token[1], out_token[2], out_token[2])
        else:
            if (verbose > 0):
                print("***", line, ":", token)
        pc += 4
    return out_statements

# risc-v assembler
def build_symbol_map(statements = [], verbose = 1):
    """Process a RISC-V assembly listing to a list of symbols"""
    line = 0
    pc = 0
    symbol_map = { "start" : pc}
    for statement in statements:
        line += 1
        token = parse(statement)
        if (len(token) == 0):
            continue
        if (len(token) == 1):
            label = token[0].replace(':','')
            symbol = { label : pc }
            symbol_map.update(symbol)
            if (verbose > 0):
                print(line, ":", label, symbol_map)
            continue
        pc += 4
    return symbol_map

def trim(token : str):
    """Remove extra characters from a token"""
    return token.replace(',', '')

def index(token : str):
    """convert a register token to a register index"""
    return register_index(trim(token))

def process(statements = [], verbose = 0):
    """Process a RISC-V assembly listing to a list of RISC_V statements"""
    symbol_map = build_symbol_map(statements, verbose)

    instructions = []
    line = 0
    for statement in statements:
        line += 1
        token = parse(statement)
        if (len(token) == 0):
            continue
        if (len(token) == 1):
            continue
        if (len(token) == 2):
            if (token[0] == "jal"):
                label = token[1]
                address = symbol_map[label] 
                instruction = jal(index("t0"), address)
                instructions.append(instruction)
                if (verbose > 0):
                    print(line, ":", "jal", symbol_map[token[1]])
        elif (len(token) == 3):
            if (token[0] == "lui"):
                instruction = lui(index(token[1]), int(token[2]))
                instructions.append(instruction)
                if (verbose > 0):
                    print(line, ":", "lui", token[1], token[2])
        elif (len(token) == 4):
            if (token[0] == "add"):
                instruction = add(index(token[1]),index(token[2]),index(token[3]))
                instructions.append(instruction)
                if (verbose > 0):
                    print(line, ":", "add", token[1], token[2], token[3])
            if (token[0] == "addi"):
                instruction = addi(index(token[1]),index(token[2]),int(token[3]))
                instructions.append(instruction)
                if (verbose > 9):
                    print(line, ":", "addi", token[1], token[2], token[3])
            if (token[0] == "bge"):
                label = token[3]
                address = symbol_map[label] 
                instruction = bge(index(token[1]),index(token[2]),address)
                instructions.append(instruction)
                if (verbose > 0):
                    print(line, ":", "bge", token[1], token[2], address)
    return instructions
        
