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

        self.assertAlmostEqual(NumThai().TextThaiToNumber("หนึ่ง"),"1")
        self.assertAlmostEqual(NumThai().TextThaiToNumber("ลบหนึ่ง"),"-1")
        self.assertAlmostEqual(NumThai().TextThaiToNumber("สิบ"),"10")
        self.assertAlmostEqual(NumThai().TextThaiToNumber("สิบเอ็ด"),"11")
        self.assertAlmostEqual(NumThai().TextThaiToNumber("ยี่สิบ"),"20")
        self.assertAlmostEqual(NumThai().TextThaiToNumber("หนึ่งร้อย"),"100")
        self.assertAlmostEqual(NumThai().TextThaiToNumber("หนึ่งล้านจุดสามสองหนึ่ง"),"1000000.321")
        self.assertAlmostEqual(NumThai().TextThaiToNumber("ลบหนึ่งล้านจุดสามสองหนึ่ง"),"-1000000.321")

    
    def test_numthaiValue(self):
        self.assertRaises(ValueError,NumThai().NumberToTextThai,111111111111111111)
        self.assertRaises(ValueError,NumThai().NumberToTextThai,-111111111111111111)

        self.assertRaises(ValueError,NumThai().TextThaiToNumber,"11")
        self.assertRaises(ValueError,NumThai().TextThaiToNumber,"-22")

    def test_numthaiType(self):
        self.assertRaises(TypeError,NumThai().NumberToTextThai,1+2j)
        self.assertRaises(TypeError,NumThai().NumberToTextThai,True)
        self.assertRaises(TypeError,NumThai().NumberToTextThai,"number")

        self.assertRaises(TypeError,NumThai().TextThaiToNumber,1+2j)
        self.assertRaises(TypeError,NumThai().TextThaiToNumber,True)
        self.assertRaises(TypeError,NumThai().TextThaiToNumber,10)
        self.assertRaises(TypeError,NumThai().TextThaiToNumber,-10)
        self.assertRaises(TypeError,NumThai().TextThaiToNumber,10.5432)



