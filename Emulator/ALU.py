#If both inputs match, return 1.
class ANDGate:
    @staticmethod
    def execute(a, b):
        result = ""
        for bit_a, bit_b in zip(a, b):
            result += '1' if bit_a == '1' and bit_b == '1' else '0'
        return result

#If either or both of the inputs are 1, return 1.
class ORGate:
    @staticmethod
    def execute(a, b):
        result = ""
        for bit_a, bit_b in zip(a, b):
            result += '1' if bit_a == '1' or bit_b == '1' else '0'
        return result

#If one of the inputs is 1, return 1. If both inputs are 1, return 0.
class XORGate:
    @staticmethod
    def execute(a, b):
        result = ""
        for bit_a, bit_b in zip(a, b):
            result += '1' if (bit_a == '1' and bit_b == '0') or (bit_a == '0' and bit_b == '1') else '0'
        return result

#Inverts the input. 1 is 0 and 0 is 1.
class NOTGate:
    @staticmethod
    def execute(a):
        result = ""
        for bit_a in a:
            result += '0' if bit_a == '1' else '1'
        return result
      
class ALU:
    @staticmethod
    def add(a, b):
        result = ""
        carry = '0'
        max_len = max(len(a), len(b))

        # Zero-pad the shorter operand
        # Zfill fills with 0s up to the desired length
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        #loops for each value in the zipped tuple.
        for bit_a, bit_b in zip(reversed(a), reversed(b)):
            #If 1 + 0 without carry in this step, it returns 1
            #If 1 + 1 without carry it returns 0, plus a carry
            #If it is 1+0 with a carry, it returns 0 because it would essentially be 1+1
            #If 1+1 with carry it will return 1 plus a carry.
            sum_bit = XORGate.execute(XORGate.execute(bit_a, bit_b), carry)
            #If 1+0, returns 0.
            #If 1+1, return 1
            #If 1+1 with carry, return 1 for extra carry
            carry = ORGate.execute(ANDGate.execute(bit_a, bit_b), ANDGate.execute(XORGate.execute(bit_a, bit_b), carry))
            #Adds to the result to the beginning of the result.
            result = sum_bit + result

        #If carry is left over after loop is done, add the extra 1
        if carry == '1':
            result = carry + result

        #removes the leading 0s for cleanliness and multiplication function.
        return ALU.remove_leading_zeros(result)
    
    @staticmethod
    def subtract(a, b):
        result = ""
        borrow = '0'
        check_a = []
        check_b = []
        max_len = max(len(a), len(b))
        
        #Ensures the minuend is larger than the subtrahend.
        #The logic in this emulator only handles non-negative values.
        if len(ALU.remove_leading_zeros(a)) < len(ALU.remove_leading_zeros(b)):
            return "0"
        
        for i in a:
            check_a.append(int(i))
            
        for i in b:
            check_b.append(int(i))
            
        if sum(check_a) < sum(check_b):
            return "0"

        # Zero-pad the shorter operand
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        #loop in the zipped tuple
        for bit_a, bit_b in zip(reversed(a), reversed(b)):
            
            #If 1-0 without borrow return 1
            #If 1-1 without borrow return 0
            #If 0-1 return 1 and will borrow another
            #If 1-1 with borrow it will return 1
            diff = XORGate.execute(XORGate.execute(bit_a, bit_b), borrow)
            #If 0-1, return borrow 1
            #If 1-1, return no borrow
            #If 0-1 with borrow return 1
            borrow= ORGate.execute(ORGate.execute(ANDGate.execute(NOTGate.execute(bit_a), bit_b),
                                                    ANDGate.execute(NOTGate.execute(bit_a), borrow)),
                                        ANDGate.execute(bit_b, borrow))
            #Adds to the beginning of the result
            result = diff + result

        # Trim leading zeros
        result = result.lstrip('0') or '0'

        return result
    
    @staticmethod
    def multiply(a, b):
        result = '0'
        max_len = max(len(a), len(b))

        # Zero-pad the shorter operand
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        #loop through each element in the 2nd product
        for bit_b in reversed(b):
            #if the bit is 1, add the entire a input to the result
            if bit_b == '1':
                result = ALU.add(result, a)

            a = a + '0'  # Shift 'a' to the left for each step

        return ALU.remove_leading_zeros(result)
    
    #trims all leading 0s
    @staticmethod
    def remove_leading_zeros(binary_str):
        return binary_str.lstrip('0')