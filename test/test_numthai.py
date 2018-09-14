import unittest
import sys
sys.path.append('..')

from num_thai.thainumbers import NumThai

class TestNumThai(unittest.TestCase):

    def test_numthai(self):
        self.assertAlmostEqual(NumThai().NumberToTextThai(0),["ศูนย์"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(1),["หนึ่ง"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(-1),["ลบ","หนึ่ง"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(10),["สิบ"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(-10),["ลบ","สิบ"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(11),["สิบ","เอ็ด"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(-11),["ลบ","สิบ","เอ็ด"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(20),["ยี่สิบ"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(-20),["ลบ","ยี่สิบ"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(21),["ยี่สิบ","เอ็ด"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(-21),["ลบ","ยี่สิบ","เอ็ด"])
        self.assertAlmostEqual(NumThai().NumberToTextThai(30),["สามสิบ"])

        self.assertAlmostEqual(NumThai().NumberToTextThai(200),["สองร้อย"])
    
    def test_numthaiValue(self):
        self.assertRaises(ValueError,NumThai().NumberToTextThai,111111111111111111)
        self.assertRaises(ValueError,NumThai().NumberToTextThai,-111111111111111111)

    def test_numthaiType(self):
        self.assertRaises(TypeError,NumThai().NumberToTextThai,1+2j)
        self.assertRaises(TypeError,NumThai().NumberToTextThai,True)
        self.assertRaises(TypeError,NumThai().NumberToTextThai,"number")


