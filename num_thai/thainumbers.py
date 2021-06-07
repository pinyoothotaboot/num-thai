import re
from decimal import Decimal


class NumThai:

    def __init__(self):

        self.number = None
        self.num_text = {
                        '-': "ລົບ", '.': "จุด", 0: "ศูนย์", 1: "ໜຶ່ງ",
                        2: "ສອງ", 3: "สาม", 4: "สี่", 5: "ห้า",
                        6: "หก", 7: "เจ็ด", 8: "แปด", 9: "เก้า",
                        "0": "", "1": "สิบ", "2": "ร้อย", "3": "พัน",
                        "4": "หมื่น", "5": "แสน", "6": "ລ້ານ"
                    }

    def process_int(self):
        result = []
        le = len(str(self.number))
        val = self.num_text['6']
        i = 0
        
        for x in range(0, le):
            n = int(self.number % 10)
            self.number /= 10

            if le > 1:
                if x >= 1 and x % 6 == 0:
                    if n == 1 and le < 8:
                        result.append(self.num_text[n]+val)
                    elif n == 1 and le > 7:
                        result.append("ເອັດ"+val)
                    else:
                        if n != 0:
                            result.append(self.num_text[n]+val)
                        else:
                            result.append(val)

                elif x == 0 and n == 1:
                    result.append("ເອັດ")
                else:
                    if i == 1 and n == 1:
                        result.append(self.num_text[str(i)])
                    elif i == 1 and n == 2:
                        result.append("ยี่"+self.num_text[str(i)])
                    elif n == 0:
                        pass
                    else:
                        result.append(self.num_text[n]+self.num_text[str(i)])         
            else:
                result.append(self.num_text[n])
    
            if i > 5:
                val += val
                i = 0
            i += 1
        
        return list(reversed(result))
    
    """
        Function    : NumberToTextThai
        Description : This function to convert number to thai text.
        Input       : Number
        Return      : Thai text
        Example     : NumberToTextThai(110)
                    >> ["ໜຶ່ງร้อย","สิบ"]
    """
    def NumberToTextThai(self, number):

        result = []
        fnumber = 0

        if type(number) not in [int, float]:

            raise TypeError("ต้องใส่ข้อมูลตัวเลข ค่ะ...")
        
        if len(str(abs(number))) > 16 or len(str(abs(number))) < 1:

            raise ValueError("ตัวเลขที่ใส่จะต้องอยู่ในช่วง 1-16 ตัว ค่ะ")

        if number < 0:
            result.append(self.num_text['-'])
            number = abs(number)
        
        if type(number) in [int]:
            self.number = number
        elif type(number) in [float]:
            self.number = int(number)
            fnumber = Decimal(str(number)) % 1
            
        result.extend(self.process_int())

        if fnumber > 0:
            str1 = str(fnumber)
            for i in range(1, len(str1)):
                if str1[i] == '.':
                    result.append(self.num_text[str1[i]])
                else:
                    result.append(self.num_text[int(str1[i])])

        return result

    """
        Function    : TextThaiToNumber
        Description : This function to convert thai text to number.
        Input       : Thai text
        Return      : Number
        Example     : TextThaiToNumber("ໜຶ່ງร้อยสิบจุดสามສອງໜຶ່ງ")
                    >> 110.321
    """

    def TextThaiToNumber(self, txt):
        unit_text = {
            'ໜຶ່ງ': 1, 'ເອັດ': 1, 'ສອງ': 2,
            'สาม': 3, 'สี่': 4, 'ห้า': 5, 'หก': 6,
            'เจ็ด': 7, 'แปด': 8, 'เก้า': 9
        }

        deci = {
            "ยี่สิบ": 20, "สามสิบ": 30, "สี่สิบ": 40, "ห้าสิบ": 50,
            "หกสิบ": 60, "เจ็ดสิบ": 70, "แปดสิบ": 80, "เก้าสิบ": 90
        }

        cross_text = {
            'ร้อย': 100, 'พัน': 1000, 'หมื่น': 10000, 'แสน': 100000, 'ລ້ານ': 1000000,
        }

        ten = {
            "สิบ": 10
        }

        thai_float = {
            "จุด": '.', "ศูนย์": "0", "ໜຶ່ງ": '1', "ສອງ": '2',
            "สาม": '3', "สี่": '4', "ห้า": '5', "หก": '6',
            "เจ็ด": '7', "แปด": '8', "เก้า": '9'
        }

        thai_num = [
            "๑", "๒", "๓", "๔", "๕", "๖", "๗", "๘", "๙"
        ]

        float_text = ''

        if type(txt) in [int, float]:
            raise TypeError("ข้อมูลที่ป้อนต้องเป็นข้อความ ค่ะ")

        t = re.search(r'[ก-๙]+', txt, re.M | re.I)

        # ตรวจสอบว่าค่าที่รับเข้ามานั้นเป็นข้อความไทยหรือไม่
        if t:
            # ถ้ามีตัวเลขไทย ปะปน ให้เปลี่ยนเป็นช่องว่าง
            for i in thai_num:
                txt = re.sub(str(i), '', txt)

            # ค้นห้าคำว่า จุด
            searchObj = re.search(r'จุด.+', txt, re.M | re.I)

            # กรณีที่พบคำว่า จุด
            if searchObj:
                # เก็บข้อมูลตั้งแต่คำว่าจุดไปจนถึง อักขระ สุดท้าย
                float_text = searchObj.group()

                # เอาค่าจาก float_text มาລົບออกในข้อมูลแรก
                txt = re.sub(str(float_text), '', txt)
        else:
            raise ValueError("ข้อมูลที่ให้มาต้องอยู่เป็น ก-๙")
        
        fl = list()

        # ตรวจสอบว่า ข้อมูลใน float_text นั้นไม่มี ช่องว่าง
        if float_text != '':
            # แปลงคำไทยเป็นเลข
            for i in thai_float:
                float_text = re.sub(i, thai_float[i], float_text)
    
            # กำหนดตัวแปร list
            fl = list(float_text)

            # ตรวจสอบความถูกต้องของข้อมูล ถ้ามีข้อมูลใดไม่ใช่ จะแสดง Error ออกมา
            for i in range(len(fl)):
                if fl[i] not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    raise ValueError("มีข้อมูลในจำนวนทศนิยมที่สะกดไม่ถูกอยู่ ค่ะ")
                    break
    
            float_text = ''.join(fl)

        # ค้นหาคำว่าລົບ
        obj_minus = re.search(r"ລົບ", txt, re.M | re.I)

        minus = ''

        # ถ้าพบคำว่า (ລົບ)
        if obj_minus:
            minus = '-'
            txt = re.sub(r"ລົບ", "", txt)
        # หาคำในหลักสิบที่มากกว่า 20 ขึ้นไป
        for i in deci:
            txt = re.sub(str(i), '+%s' % str(deci[i]), txt)
        # หาคำในหลักหน่วยหรือคำที่เป็นเลข 1-9 รวมคำว่า ເອັດ
        for i in unit_text:
            txt = re.sub(str(i), '+%s' % str(unit_text[i]), txt)
        # หาคำที่อยู๋่ในหลักสิบ 10 -19
        for i in ten:
            txt = re.sub(str(i), '+%s' % str(ten[i]), txt)
        # หาคำที่เป็นตัวคูณ ร้อย สิบ ....
        for i in cross_text:
            if i == "ລ້ານ":
                txt = re.sub(str(i), ')*%s' % str(cross_text[i]), txt)
            else:
                txt = re.sub(str(i), '*%s' % str(cross_text[i]), txt)

        ls = list(txt)

        count = 0
        # ถ้าหน่วยมีหลักລ້ານขึ้น ให้นับจำนวน วงเล็บปิด
        for x in range(len(ls)):
            if ls[x] == ')':
                count += 1
            if ls[x] not in ['(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '*']:
                raise ValueError("มีข้อมูลในหลักจำนวนเต็มที่สะกดไม่ถูกอยู่ ค่ะ")
                break
    
        # ตรวจสอบว่า Count >1 ก็ให้สร้าง วงเล็บเปิดตามจำนวน Count
        if count > 0:
            ls[0] = ls[0].replace(str(ls[0]), str('(' * (count) + ls[0]))

        # แปลงรูปแบบ String ให้เป็นผลลัพธ์แบบตัวเลข
        if ls:
            result = eval(str(''.join(ls)))
        else:
            raise ValueError("ไม่มีข้อมูล ค่ะ")

        total_result = ''

        if minus != '':
            total_result = str(minus)+str(result)+str(float_text)
        else:
            total_result = str(result)+str(float_text)
        
        return total_result


class LaoNum:

    def __init__(self):

        self.number = None
        self.num_text = {
            '-': "ລົບ", '.': "ຈຸດ", 0: "ສູນ", 1: "ໜຶ່ງ",
            2: "ສອງ", 3: "ສາມ", 4: "ສີ່", 5: "ຫ້າ",
            6: "ຫົກ", 7: "ເຈັດ", 8: "ແປດ", 9: "ເກົ້າ",
            "0": "", "1": "ສິບ", "2": "ຮ້ອຍ", "3": "ພັນ",
            "4": "ໝື່ນ", "5": "ແສນ", "6": "ລ້ານ"
        }

    def process_int(self):
        result = []
        le = len(str(self.number))
        val = self.num_text['6']
        i = 0

        for x in range(0, le):
            n = int(self.number % 10)
            self.number /= 10

            if le > 1:
                if x >= 1 and x % 6 == 0:
                    if n == 1 and le < 8:
                        result.append(self.num_text[n]+val)
                    elif n == 1 and le > 7:
                        result.append("ເອັດ"+val)
                    else:
                        if n != 0:
                            result.append(self.num_text[n]+val)
                        else:
                            result.append(val)

                elif x == 0 and n == 1:
                    result.append("ເອັດ")
                else:
                    if i == 1 and n == 1:
                        result.append(self.num_text[str(i)])
                    elif i == 1 and n == 2:
                        result.append("ຊາວ")
                    elif n == 0:
                        pass
                    else:
                        result.append(self.num_text[n]+self.num_text[str(i)])
            else:
                result.append(self.num_text[n])

            if i > 5:
                val += val
                i = 0
            i += 1

        return list(reversed(result))

    """
        Function    : NumberToTextThai
        Description : This function to convert number to thai text.
        Input       : Number
        Return      : Thai text
        Example     : NumberToTextThai(110)
                    >> ["ໜຶ່ງຮ້ອຍ","ສິບ"]
    """

    def numbertolaotext(self, number):

        result = []
        fnumber = 0

        if type(number) not in [int, float]:

            raise TypeError("ກະລຸນາປ້ອນຕົວເລກ...")

        if len(str(abs(number))) > 16 or len(str(abs(number))) < 1:

            raise ValueError("ຂອບເຂດຕົວເລກທີ່ປ້ອນຕ້ອງຢູ່ລະຫວ່າງ 1-16 ຫຼັກ")

        if number < 0:
            result.append(self.num_text['-'])
            number = abs(number)

        if type(number) in [int]:
            self.number = number
        elif type(number) in [float]:
            self.number = int(number)
            fnumber = Decimal(str(number)) % 1

        result.extend(self.process_int())

        if fnumber > 0:
            str1 = str(fnumber)
            for i in range(1, len(str1)):
                if str1[i] == '.':
                    result.append(self.num_text[str1[i]])
                else:
                    result.append(self.num_text[int(str1[i])])

        return result

    """
        Function    : TextThaiToNumber
        Description : This function to convert thai text to number.
        Input       : Thai text
        Return      : Number
        Example     : TextThaiToNumber("ໜຶ່ງຮ້ອຍສິບຈຸດສາມສອງໜຶ່ງ")
                    >> 110.321
    """

    def laotexttonumber(self, txt):
        unit_text = {
            'ໜຶ່ງ': 1, 'ເອັດ': 1, 'ສອງ': 2,
            'ສາມ': 3, 'ສີ່': 4, 'ຫ້າ': 5, 'ຫົກ': 6,
            'ເຈັດ': 7, 'ແປດ': 8, 'ເກົ້າ': 9
        }

        deci = {
            "ຊາວ": 20, "ສາມສິບ": 30, "ສີ່ສິບ": 40, "ຫ້າສິບ": 50,
            "ຫົກສິບ": 60, "ເຈັດສິບ": 70, "ແປດສິບ": 80, "ເກົ້າສິບ": 90
        }

        cross_text = {
            'ຮ້ອຍ': 100, 'ພັນ': 1000, 'ໝື່ນ': 10000, 'ແສນ': 100000, 'ລ້ານ': 1000000,
        }

        ten = {
            "ສິບ": 10
        }

        lao_float = {
            "ຈຸດ": '.', "ສູນ": "0", "ໜຶ່ງ": '1', "ສອງ": '2',
            "ສາມ": '3', "ສີ່": '4', "ຫ້າ": '5', "ຫົກ": '6',
            "ເຈັດ": '7', "ແປດ": '8', "ເກົ່າ": '9'
        }

        lao_num = [
            "໑", "໒", "໓", "໔", "໕", "໖", "໗", "໘", "໙"
        ]

        float_text = ''

        if type(txt) in [int, float]:
            raise TypeError("ຂໍ້ຄວາມທີ່ປ້ອນຕ້ອນເປັນຕົວໜັງສືທີ່ຖືກຕ້ອງ ເຊັ່ນ: ໜຶ່ງຮ້ອຍຊາວສາມຈຸດໜຶ່ງສອງສາມ")

        t = re.search(r'[ก-໙]+', txt, re.M | re.I)

        # ກວດສອບວ່າຄ່າ Input ເຂົ້າມາເປັນພາສາລາວ ຫລື ບໍ່
        if t:
            # ຫາກມີຕົວເລກລາວປົນໃນຂໍ້ຄວາມ ໃຫ້ປ່ຽນເປັນຍະຫວ່າງ
            for i in lao_num:
                txt = re.sub(str(i), '', txt)

            # ຄົ້ນຫາຄຳວ່າ ຈຸດ
            searchObj = re.search(r'ຈຸດ.+', txt, re.M | re.I)

            # ຫາກມີຄຳວ່າ ຈຸດ
            if searchObj:
                # ເກັບຂໍ້ມູນຫລັງຈຸດໄປຈົນສຸດຂໍ້ຄວາມ
                float_text = searchObj.group()

                # ຕັດຫລັງຈຸດອອກ
                txt = re.sub(str(float_text), '', txt)
        else:
            raise ValueError("ຂໍ້ມຄວາມທີ່ປ້ອນມາຕ້ອງຢູ່ໃນ ก-໙")

        fl = list()

        # ກວດສອບຂໍ້ມູນໃນ float_text ວ່າບໍ່ມີຊ່ອງຫວ່າງ
        if float_text != '':
            # ປ່ຽນເລກລາຍເປັນຕົວເລກ
            for i in lao_float:
                float_text = re.sub(i, lao_float[i], float_text)

            # ກຳນົດຕົວປ່ຽນ list
            fl = list(float_text)

            # ກວດສອບຄວາມຖືກຕ້ອງຂອງຂໍ້ມູນ
            for i in range(len(fl)):
                if fl[i] not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    raise ValueError(
                        "ມີຂໍ້ມູນຫຼັງຈຸດທີ່ສະກົດຜິດ")
                    break

            float_text = ''.join(fl)

        # ກວດສອບຄ່າລົບ
        obj_minus = re.search(r"ລົບ", txt, re.M | re.I)

        minus = ''

        # ຫາກພົບຄຳວ່າ (ລົບ)
        if obj_minus:
            minus = '-'
            txt = re.sub(r"ລົບ", "", txt)
        # ຫາຄຳຫຼັກສິບທີ່ຫຼາຍກວ່າ 20 ຂຶ້ນໄປ
        for i in deci:
            txt = re.sub(str(i), '+%s' % str(deci[i]), txt)
        # ຫາຄຳທີ່ເປັນຫຼັກໜ່ວຍ 1-9 ລວມຄຳວ່າ ເອັດ
        for i in unit_text:
            txt = re.sub(str(i), '+%s' % str(unit_text[i]), txt)
        # ຫາຄຳທີ່ຢູ່ໃນຫຼັກສິບ 10 -19
        for i in ten:
            if i != 'ຊາວ':
                txt = re.sub(str(i), '+%s' % str(ten[i]), txt)
            else:
                txt = re.sub(str(i), txt)
        # ຫາຄຳທີ່ເປັນ ຕົວຄູນ ຮ້ອຍ ສິບ ...
        for i in cross_text:
            if i == "ລ້ານ":
                txt = re.sub(str(i), ')*%s' % str(cross_text[i]), txt)
            else:
                txt = re.sub(str(i), '*%s' % str(cross_text[i]), txt)

        ls = list(txt)

        count = 0
        # ຫາກເກີນລ້ານ ໃຫ້ນັບຈຳນວນ ໂດຍມີວົງເລັບປິດ
        for x in range(len(ls)):
            if ls[x] == ')':
                count += 1
            if ls[x] not in ['(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '*']:
                raise ValueError(
                    "ມີຂໍ້ຄວາມທີ່ສະກົດບໍ່ຖືກຕ້ອງ ໃນກຸ່ມຈຳນວນເຕັມ")
                break

        # ກວດສອບ Count >1 ກໍ່ໃຫ້ສ້າງວົງເພີ່ມວົງເລັບຕາມຈຳນວນ Count
        if count > 0:
            ls[0] = ls[0].replace(str(ls[0]), str('('*(count)+ls[0]))

        # ປ່ຽນຮູບແບບ String ໃຫ້ເປັນຜົນຮັບຕົວເລກ
        if ls:
            result = eval(str(''.join(ls)))
        else:
            raise ValueError("ຂໍໂທດ ບໍ່ພົບຂໍ້ມູນ")

        total_result = ''

        if minus != '':
            total_result = str(minus)+str(result)+str(float_text)
        else:
            total_result = str(result)+str(float_text)

        return total_result

