# py2145 - a python RISC-V simulator

Implements a simulator of a RISC-V core. The core is used to calculate Fibonacci numbers. Only things needed are implemented. 

## Runtime modules
Modules to simulate (run) a RISC-V program in memory
### register.py
<li>Defines the 32 RV32I register.</li>
<li>Provides RV32I register definition.</li>

### opcode.py
<li>Supported operation codes for RV32I instructions.</li>

### decoder.py
<li>implements RV32I instruction decoder.</li>
<li>RV32I instruction format decoder to decode supported instructions.</li>

### silicon.py
<li>Execute a single RV32I instruction.</li>
<li>Decode the instruction.</li> 
<li>Process the op code detected.</li>

### memory.py
<li>Defines the program memory and the program counter.</li>
<li>Provides loading a list of instructions into memory.</li>

### debugger.py
<li>Loads a list of instructions into memory.</li>
<li>Performs a step by step execution of instructions in memory.</li>
<li>Displays information on program counter and registers.</li>

## Build modules
Modules to create a list of instructions to load into memory and execute at runtime.
### encoder.py
<li>RV32I instruction encoder.</li>
<li>Provides RV32I instruction format encoder to encode instructions.</li>

### assembler.py
<li>Translates RISC-V assembler lines to a list of instructions.</li>
<li>Translates gnu alike assembler lines to RISC-V assembler lines.</li>

## Playground
Modul to define samples and verify build and runtime modules.
### py2145.py
<li>Definition of fibonacci10 as list of instructions.</li>
<li>Definition of fibonacci10 RISC-V assembler listing.</li>
<li>Definition of fibonacci10 gnu (alike) assembler listing.</li>
<li>Debugging of fibonacci10 instructions.</li>

End.
