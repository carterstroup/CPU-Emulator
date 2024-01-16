from cache import Cache
from memory import Memory
from ALU import ALU as alu

CPU_COUNTER_INIT_VALUE = 0
NUMBER_OF_REGISTERS = 9

ADD_INSTRUCTION_OPERATOR = "ADD"
ADD_I_INSTRUCTION_OPERATOR = "ADDI"
JUMP_INSTRUCTION_OPERATOR = "J"
CACHE_INSTRUCTION_OPERATOR = "CACHE"
LOAD_WORD_INSTRUCTION_OPERATOR = "LW"
SAVE_WORD_INSTRUCTION_OPERATOR = "SW"
MULTIPLY_INSTRUCTION_OPERATOR = "MULT"
SUBTRACT_INSTRUCTION_OPERATOR = "SUB"
PRINT_INSTRUCTION_OPERATOR = "PNT"

CACHE_OFF_VALUE = 0
CACHE_FLUSH_VALUE = 1


# Helper function to convert register string to index. I.e. register labelled 'R2' should correspond to int index 2
def convert_register_to_index(value):
    return int(value[1:])


# CPU class to implement the bulk of CPU Simulator requirements. Member properties include:
# CPU Counter - Int representing the number of the instruction being parsed
# Registers - List used to represent internal registers used by the CPU
# Cache Flag - boolean representing whether or not the cache is to be used
# Cache - instance of Cache object instantiated for CPU
# Memory Bus - instance of Memory Bus object instantiated for CPU
class CPU:

    def __init__(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE
        self.registers = [0] * NUMBER_OF_REGISTERS
        self.cache = Cache()
        self.memory_bus = Memory()

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def reset_cpu_counter(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE

    def set_cpu_counter(self, value):
        self.cpu_counter = value

    def get_cpu_counter(self):
        return self.cpu_counter

    def reset_registers(self):
        for i in range(len(self.registers)):
            self.registers[i] = 0

    def set_cache_flag(self, value):
        self.cache_flag = value

    def flush_cache(self):
        self.cache.flush_cache()

    def search_cache(self, address):
        return self.cache.search_cache(address)

    def write_cache(self, address, value):
        self.cache.write_cache(address, value)

    def search_memory_bus(self, address):
        return self.memory_bus.search_memory_bus(address)

    def write_memory_bus(self, address, value):
        self.memory_bus.write_memory_bus(int(address), value)

    # --- Sample implementations for ADD, ADDI, J, and Cache instructions ---

    def jump_instruction(self, target):
        self.cpu_counter = int(target)

    def add_instruction(self, destination, source, target):
        self.registers[convert_register_to_index(destination)] = alu.add(str(self.registers[convert_register_to_index(source)]), str(self.registers[convert_register_to_index(target)]))
    
    def mult_instruction(self, destination, source, target):
        self.registers[convert_register_to_index(destination)] = alu.multiply(str(self.registers[convert_register_to_index(source)]), str(self.registers[convert_register_to_index(target)]))
        
    def subt_instruction(self, destination, source, target):
        self.registers[convert_register_to_index(destination)] = alu.subtract(str(self.registers[convert_register_to_index(source)]), str(self.registers[convert_register_to_index(target)]))

    def add_i_instruction(self, destination, source, immediate):
        self.registers[convert_register_to_index(destination)] = alu.add(str(self.registers[convert_register_to_index(source)]), str(int(immediate)))

    # Method to implement cache instruction. 0 = OFF, 1 = ON, 2 = Flush Cache
    def cache_instruction(self, value):
        if value == CACHE_FLUSH_VALUE:
            self.flush_cache()
            
    def print_instruction(self,idx):
        print(self.registers[convert_register_to_index(idx)])
      
    #checks to see if data in cache, if so it returns the value from the cache, if not, it gets the memory from the bus, stores it in the cache, and then returns from the bus
    def get_memory(self, m_address):
        value = None
        if self.cache.search_cache(int(m_address)) != None:
            value = self.cache.search_cache(int(m_address))
        elif self.memory_bus.search_memory_bus(int(m_address)) != None:
            value = self.memory_bus.search_memory_bus(int(m_address))
            self.cache.write_cache(int(m_address), value)
        else:
            return None
        return value
    
    #helper function LW, gets the value from get_memory then assigns it to the register
    def load_word(self, m_address, r_address):
        value = self.get_memory(int(m_address))
        self.registers[convert_register_to_index(r_address)] = value
    
    def save_word(self, m_address, r_address):
        self.cache.write_cache(m_address, self.registers[convert_register_to_index(r_address)])
        self.memory_bus.write_memory_bus(int(m_address), self.registers[convert_register_to_index(r_address)])
     

    #test a bunch -> comment all the code and understand it
    #publish

    # --- Add implementations for further instructions below ---

    # --------------------------------------------------------- #

    # Main parser method used to interpret instructions from input file.
    # Check value of operator and call subsequent helper function
    def parse_instruction(self, instruction):
        instruction_parsed = instruction.split(",")
        print("Reading instruction: " + instruction)
        self.increment_cpu_counter()
        if instruction_parsed[0] == ADD_INSTRUCTION_OPERATOR:
            self.add_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == ADD_I_INSTRUCTION_OPERATOR:
            self.add_i_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == JUMP_INSTRUCTION_OPERATOR:
            self.jump_instruction(instruction_parsed[1])
        if instruction_parsed[0] == CACHE_INSTRUCTION_OPERATOR:
            self.cache_instruction(instruction_parsed[1])
        if instruction_parsed[0] == LOAD_WORD_INSTRUCTION_OPERATOR:
            self.load_word(instruction_parsed[1], instruction_parsed[2])
        if instruction_parsed[0] == SAVE_WORD_INSTRUCTION_OPERATOR:
            self.save_word(instruction_parsed[1], instruction_parsed[2])
        if instruction_parsed[0] == SUBTRACT_INSTRUCTION_OPERATOR:
            self.subt_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == MULTIPLY_INSTRUCTION_OPERATOR:
            self.mult_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
        if instruction_parsed[0] == PRINT_INSTRUCTION_OPERATOR:
            self.print_instruction(instruction_parsed[1])