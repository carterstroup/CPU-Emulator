# Syntax Instructions

## Assembly Information

Below you will find a list of function supported by the emulator and their Assembly syntax.

#### Add

This function will add two registers together and store the result in a seperate register.

`ADD,STORAGE REGISTER,ADDENED1,ADDEND2`

Working Example:

`ADD,R5,R1,R2`

This will add register 1 to register 2 and store the result at register 5. (Please Note: There are only registers 1-7, you will need to save any more results to memory.)

#### Add With Constant

`ADDI,STORAGE REGISTER,REGISTER TO BE ADDED, CONSTANT`

Working Example:

`ADDI,R5,R1,10011`

This will add register 1 to the binary constant and store the result at register 5. (Please Note: The constant must be binary. There are only registers 1-7, you will need to save any more results to memory.)

#### Subtract

`SUB,STORAGE REGISTER,MINUEND,SUBTRAHEND`

Working Example:

`SUB,R5,R1,R2`

This will subtract register 2 from register 1 and store the result at register 5. (Please Note: The first input MUST be larger than the second for an accurate calculation. There are only registers 1-7, you will need to save any more results to memory.)

#### Multiply

`MULT,STORAGE REGISTER,FACTOR1,FACTOR2`

Working Example:

`MULT,R5,R1,R2`

This will multiply register 1 with register 2 and store the result at register 5. (Please Note: There are only registers 1-7, you will need to save any more results to memory.)

#### Flush Cache

`CACHE,1`

This will completely flush the cache.

#### Skip

`J,LINE TO SKIP TO`

Working Example:

`J,5`

This will skip all instructions and go straight to line five.

#### Load From Memory

`LW,MEMORY LOCATION,REGISTER TO STORE IN`

Working Example:

`LW,15,R5`

This will load whatever is in memory slot 15 (0 by default) to register 5. (Please Note: There are only registers 1-7, and memory slots 0-125.)

#### Save To Memory

`SW,MEMORY LOCATION,REGISTER TO SAVE`

Working Example:

`SW,65,R3`

This will save whatever binary information is in register 3 to memory slot 65. (Please Note: There are only registers 1-7, and memory slots 0-125.)

#### Print

`PNT,REGISTER TO PRINT`

Working Example:

`PNT,R6`

This will print the data in register six to the console. This is not a standard MIPS function, but helpful for the emulator. (Please Note: There are only registers 1-7.)

## Memory Information

This CPU emulator allows you to load binary data into the memory bus during initialization. You can do this by using the data_input.txt file. Simply use the following syntax:

`INT(MEMORY LOCATION),BINARY`

Working Example:

`67,1001011101`

This syntax would store 605 in binary into the memory location 67. You can create up to 125 base memory entries, each on their own line.

#### Limitations

The built in memory only runs 0-127, therefore MEMORY LOCATION >= 0 but <= 127.