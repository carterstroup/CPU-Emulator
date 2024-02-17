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

CACHE_FLUSH_VALUE = 1


# Helper function to convert register string to index. I.e. register labelled 'R2' should correspond to int index 2
def convert_register_to_index(value):
    return int(value[1:])


# CPU class to implement the bulk of CPU Simulator requirements. Member properties include:
# CPU Counter - Int representing the number of the instruction being parsed
# Registers - List used to represent internal registers used by the CPU
# Cache - instance of Cache object instantiated for CPU
# Memory Bus - instance of Memory Bus object instantiated for CPU
class CPU:

    def __init__(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE
        self.registers = [0] * NUMBER_OF_REGISTERS
        self.cache = Cache()
        self.memory_bus = Memory()

    #The CPU counter counts which instruction we are on.
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

    def flush_cache(self):
        self.cache.flush_cache()

    def search_cache(self, memory_address):
        return self.cache.search_cache(memory_address)

    def write_cache(self, memory_address, value):
        self.cache.write_cache(memory_address, value)

    def search_memory_bus(self, address):
        return self.memory_bus.search_memory_bus(address)

    #The key in the dict representing the memory bus is an integer, which is why int() is used.
    def write_memory_bus(self, address, value):
        self.memory_bus.write_memory_bus(address, value)

    #Jumps to the line of instructions provided.
    def jump_instruction(self, target):
        try:
            self.cpu_counter = int(target)
        except:
            return
    
    #Validation Functions
    
    #Ensures input is binary.
    def check_for_binary(self, bin_str):
        if len(set(bin_str)) < 3:
            return True
        
    #Ensures the requested register is valid.
    def check_register(self, reg):
        if reg[0] == "R" or reg[0] == "r":
            if int(reg[1:]) > 0 and int(reg[1:]) <= 7:
                return True
    
    #Ensures the memory address is valid.
    def validate_memory_location(self, loc):
        try:
            if int(loc) <= 127 and int(loc) >= 0:
                return True
            else:
                print("Instruction Error: Invalid Memory Location. Jumping to Next Instruction")
                self.jump_instruction(self.cpu_counter + 1)
                return
        except:
            return
    
    #Adds two registers together.
    def add_instruction(self, destination, ad1, ad2):
        if self.check_register(ad1) == True and self.check_register(ad2) == True:
            self.registers[convert_register_to_index(destination)] = alu.add(str(self.registers[convert_register_to_index(ad1)]), str(self.registers[convert_register_to_index(ad2)]))
    
    #Multiplies two registers together.
    def mult_instruction(self, destination, fctr1, fctr2):
        if self.check_register(fctr1) == True and self.check_register(fctr2) == True:
            self.registers[convert_register_to_index(destination)] = alu.multiply(str(self.registers[convert_register_to_index(fctr1)]), str(self.registers[convert_register_to_index(fctr2)]))
    
    #Subtracts two registers. It subtracts the second number from the first. AKA sub1 - sub2 = answer
    def subt_instruction(self, destination, sub1, sub2):
        if self.check_register(sub1) == True and self.check_register(sub2) == True:
            self.registers[convert_register_to_index(destination)] = alu.subtract(str(self.registers[convert_register_to_index(sub1)]), str(self.registers[convert_register_to_index(sub2)]))

    #Adds to a constant.
    def add_i_instruction(self, destination, ad1, const):
        if self.check_for_binary(const) == True and self.check_register(ad1) == True:
            self.registers[convert_register_to_index(destination)] = alu.add(str(self.registers[convert_register_to_index(ad1)]), str(int(const)))

    # Method to implement cache flush if called.
    def cache_instruction(self, value):
        try:
            if value == CACHE_FLUSH_VALUE:
                self.flush_cache()
        except:
            return
    
    #Prints a current register's data.   
    def print_instruction(self,reg):
            print(self.registers[convert_register_to_index(reg)])
      
    #Checks to see if the wanted data is in the cache. 
    #If so, it returns the value from the cache. 
    #If not, it gets the value from the memory bus.
    #It then stores it in the cache, and then returns the value from the memory bus.
    def get_memory(self, m_address):
        value = None
        if self.cache.search_cache(m_address) != None:
            value = self.cache.search_cache(m_address)
        elif self.memory_bus.search_memory_bus(m_address) != None:
            value = self.memory_bus.search_memory_bus(m_address)
            self.cache.write_cache(m_address, value)
        else:
            return "0"
        return value
    
    #Loads values from the memory bus.
    def load_word(self, m_address, r_address):
        try:
            value = self.get_memory(m_address)
            self.registers[convert_register_to_index(r_address)] = value
        except:
            return
    
    #Saves a register's data to memory.
    def save_word(self, m_address, r_address):
        if self.check_register(r_address) == True and self.validate_memory_location(m_address) == True:
            self.cache.write_cache(m_address, self.registers[convert_register_to_index(r_address)])
            self.memory_bus.write_memory_bus(m_address, self.registers[convert_register_to_index(r_address)])



    # Main parser method used to interpret instructions from input file.
    # Check value of operator and call subsequent helper function
    def parse_instruction(self, instruction):
        instruction_parsed = instruction.split(",")
        print("Reading instruction: " + instruction)
        self.increment_cpu_counter()
        if instruction_parsed[0] == PRINT_INSTRUCTION_OPERATOR:
            if self.check_register(instruction_parsed[1]) == True:
                self.print_instruction(instruction_parsed[1])
        if instruction_parsed[0] == JUMP_INSTRUCTION_OPERATOR:
            self.jump_instruction(instruction_parsed[1])
        if instruction_parsed[0] == CACHE_INSTRUCTION_OPERATOR:
            self.cache_instruction(instruction_parsed[1])
        if instruction_parsed[0] == LOAD_WORD_INSTRUCTION_OPERATOR:
            try:
                self.load_word(instruction_parsed[1], instruction_parsed[2])
            except:
                return
        if instruction_parsed[0] == SAVE_WORD_INSTRUCTION_OPERATOR:
            try:
                self.save_word(instruction_parsed[1], instruction_parsed[2])
            except:
                return
        if instruction_parsed[0] == SUBTRACT_INSTRUCTION_OPERATOR:
            try:
                self.subt_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
            except:
                return
        if instruction_parsed[0] == MULTIPLY_INSTRUCTION_OPERATOR:
            try:
                self.mult_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
            except:
                return
        if instruction_parsed[0] == ADD_INSTRUCTION_OPERATOR:
            try:
                self.add_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
            except:
                return
        if instruction_parsed[0] == ADD_I_INSTRUCTION_OPERATOR:
            try:
                self.add_i_instruction(instruction_parsed[1], instruction_parsed[2], instruction_parsed[3])
            except:
                return