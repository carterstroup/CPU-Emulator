import unittest
from ALU import *

class TestALU(unittest.TestCase):
    def test_add(self):
        self.assertEqual(ALU.add("00000001", "00000001"), "10")
        self.assertEqual(ALU.add("00000001", "00000010"), "11")
        self.assertEqual(ALU.add("00000001", "00000011"), "100")
        self.assertEqual(ALU.add("00000001", "00000100"), "101")
        
    def test_subtract(self):
        self.assertEqual(ALU.subtract("00000001", "00000001"), "0")
        self.assertEqual(ALU.subtract("00000010", "00000001"), "1")
        self.assertEqual(ALU.subtract("00000011", "00000010"), "1")
        self.assertEqual(ALU.subtract("00000100", "00000001"), "11")
    
    def test_mult(self):
        self.assertEqual(ALU.multiply("00000001", "00000001"), "1")
        self.assertEqual(ALU.multiply("00000001", "00000010"), "10")
        self.assertEqual(ALU.multiply("00000001", "00000011"), "11")
        self.assertEqual(ALU.multiply("00000001", "00000100"), "100")
    
    def test_remove_leading_zeros(self):
        self.assertEqual(ALU.remove_leading_zeros("00000001"), "1")
        self.assertEqual(ALU.remove_leading_zeros("00000010"), "10")
        self.assertEqual(ALU.remove_leading_zeros("00000100"), "100")
        
class TestANDGate(unittest.TestCase):
    def test_execute(self):
        self.assertEqual(ANDGate.execute("1", "1"), "1")
        self.assertEqual(ANDGate.execute("1", "0"), "0")
        self.assertEqual(ANDGate.execute("0", "0"), "0")
        
class TestORGate(unittest.TestCase):
    def test_execute(self):
        self.assertEqual(ORGate.execute("1", "0"), "1")
        self.assertEqual(ORGate.execute("1", "1"), "1")
        self.assertEqual(ORGate.execute("0", "0"), "0")

class TestXORGate(unittest.TestCase):
    def test_execute(self):
        self.assertEqual(XORGate.execute("1", "0"), "1")
        self.assertEqual(XORGate.execute("1", "1"), "0")
        self.assertEqual(XORGate.execute("0", "0"), "0")
        
class TestNOTGate(unittest.TestCase):
    def test_execute(self):
        self.assertEqual(NOTGate.execute("1"), "0")
        self.assertEqual(NOTGate.execute("0"), "1")

if __name__ == '__main__':
    unittest.main()