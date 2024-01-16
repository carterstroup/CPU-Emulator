class ANDGate:
    def execute(a, b):
        result = ""
        for bit_a, bit_b in zip(a, b):
            result += '1' if bit_a == '1' and bit_b == '1' else '0'
        return result


class ORGate:
    def execute(a, b):
        result = ""
        for bit_a, bit_b in zip(a, b):
            result += '1' if bit_a == '1' or bit_b == '1' else '0'
        return result


class XORGate:
    def execute(a, b):
        result = ""
        for bit_a, bit_b in zip(a, b):
            result += '1' if (bit_a == '1' and bit_b == '0') or (bit_a == '0' and bit_b == '1') else '0'
        return result


class NOTGate:
    def execute(a):
        result = ""
        for bit_a in a:
            result += '0' if bit_a == '1' else '1'
        return result
    
    
class ALU:
    def add(a, b):
        result = ""
        carry = '0'
        max_len = max(len(a), len(b))

        # Zero-pad the shorter operand
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for bit_a, bit_b in zip(reversed(a), reversed(b)):
            sum_bit = XORGate.execute(XORGate.execute(bit_a, bit_b), carry)
            carry = ORGate.execute(ANDGate.execute(bit_a, bit_b), ORGate.execute(ANDGate.execute(XORGate.execute(bit_a, bit_b), carry), ANDGate.execute(bit_a, carry)))
            result = sum_bit + result

        if carry == '1':
            result = carry + result

        return ALU.remove_leading_zeros(result)

    def subtract(a, b):
        # Ensure both binary strings have the same length
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        result = ""
        borrow = 0

        for bit_a, bit_b in zip(reversed(a), reversed(b)):
            # Convert bits to integers
            int_a = int(bit_a)
            int_b = int(bit_b)

            # Perform subtraction with borrow
            diff = (int_a - int_b - borrow) % 2

            # Update borrow for the next iteration
            borrow = (int_a - int_b - borrow < 0)

            # Convert the result bit back to a string
            result = str(diff) + result

        # Trim leading zeros
        result = result.lstrip('0') or '0'

        return result

    def multiply(a, b):
        result = '0'
        max_len = max(len(a), len(b))

        # Zero-pad the shorter operand
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        for bit_b in reversed(b):
            if bit_b == '1':
                result = ALU.add(result, a)

            a = a + '0'  # Shift 'a' to the left

        return ALU.remove_leading_zeros(result)
    
    def remove_leading_zeros(binary_str):
        return binary_str.lstrip('0')
    
operand1 = "101010"
operand2 = "1100"

result_addition = ALU.add(operand1, operand2)
result_subtraction = ALU.subtract(operand1, operand2)
result_multiplication = ALU.multiply(operand1, operand2)

print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)