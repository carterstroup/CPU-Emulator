MEMORY_BUS_SIZE = 128

# This class implements the 'memory bus' which in real life communicates between the memory and other components.
#In this emulator, it serves as the memory itself for simplicity.
class Memory:
    def __init__(self):
        # The actual memory bus is implemented as a dictionary.
        self.memory_bus = {}
        self.init_memory_bus()

    # Method used to initialize memory bus, loops from 0 to Size of bus using ascending integer key with a default value "0".
    def init_memory_bus(self):
        for i in range(MEMORY_BUS_SIZE):
            self.memory_bus[str(i)] = 0

    def search_memory_bus(self, address):
        if self.memory_bus.get(address) is not None:
            return self.memory_bus.get(address)
        return None

    def write_memory_bus(self, address, value):
        if self.memory_bus.get(address) is not None:
            self.memory_bus[address] = value
            
            
            
#TO DO:
#Need to make default data input and instruction input more robust
#Need to make sure to fully understand alu and comment accordingly
#need to unit test
#Need to make subtraction skip if number is less than
#remove DS_Store and final checks 
#Publish