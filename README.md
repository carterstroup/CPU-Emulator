# CPU Emulator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/carterstroup/Netflix-Recommendation/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

## Features

- Emulates essential CPU and computer functions including Cache, Memory Busses, Control Unit, and a Arithmetic Logic Unit.
- Performs multiple types of binary calculations using nothing more than emulated logic gates in the ALU.
- Uses a modified MIPS Assembly language ([see Syntax Instructions](https://github.com/carterstroup/cpu/blob/main/Syntax%20Instructions.md)).
- Provides nine essential CPU opcodes/functions.
- Simulates a realistic memory storage structure using a FIFO cache replacement policy and a write-through memory policy.

## Getting Started

To run the program, simply follow the steps below in your terminal.

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/carterstroup/cpu.git
    cd CPU
    ```

2. **Run the Application:**
    ```bash
    cd Emulator
    python main.py
    ```

## Technical Details

The CPU Emulator is written in completely organic Python with no additional dependencies. The purpose of this project is to demonstrate a comprehensive knowledge of computer architecture and the relationship between high-level and low-level programming. 

At the heart of this program is the CPU, which is composed of eight registers, an arithmetic logic unit, and a control unit. The registers are simulated using a list, while the control unit utilizes simple if-then logic with many helper functions. The ALU is housed in a separate file because it uses only emulated logic gates to perform its binary operations. It can add, subtract, multiply, and divide without using native Python arithmetic operators. 

In addition to the CPU, the program also uses a simulated cache and memory bus. The cache (16 blocks) uses a FIFO replacement policy and a write-through memory storage policy. The cache is simulated using a dequeue while the memory is replicated via a dictionary. 

These processes can be utilized with a modified version of MIPS assembly via a text file ([See Syntax Instructions](https://github.com/carterstroup/cpu/blob/main/Syntax%20Instructions.md) for valid functions and syntax). You can also load in data using a text file with another simple syntax, which you can find in the same file. The total operations that can be completed are load word, save word, flush cache, multiply, subtract, add, add with constant, skip, and print. In all, the program runs in linear time across five scripts and shows strong proficiency in the knowledge of computer architecture and object-oriented programming. 

**First Functional Date:** January 16, 2024

**Education Level at The Time of Development:** Junior in High School

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/carterstroup/Netflix-Recommendation/blob/main/LICENSE) file for details.