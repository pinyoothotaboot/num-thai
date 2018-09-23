import re
from decimal import Decimal

class NumThai:

    def __init__(self):

        self.number = None
        self.num_text = {
                        '-': "ลบ",'.': "จุด",0  : "ศูนย์",1  : "หนึ่ง",
                        2  : "สอง",3  : "สาม",4  : "สี่",5  : "ห้า",
                        6  : "หก",7  : "เจ็ด",8  : "แปด",9  : "เก้า",
                        "0": "","1"  : "สิบ","2" : "ร้อย","3": "พัน",
                        "4": "หมื่น","5": "แสน","6": "ล้าน"
                    }

    def process_int(self):
        result = []
        le = len(str(self.number))
        val = self.num_text['6']
        i=0
        
        for x in range(0,le):
            n = int(self.number%10)
            self.number /=10

            if le >1:
                if x >=1 and x%6==0:
                    if n==1 and le<8:
                        result.append(self.num_text[n]+val)
                    elif n==1 and le>7:
                        result.append("เอ็ด"+val)
                    else:
                        if n !=0:
                            result.append(self.num_text[n]+val)
                        else:
                            result.append(val)

                elif x==0 and n==1:
                    result.append("เอ็ด")
                else:
                    if i==1 and n==1:
                        result.append(self.num_text[str(i)])
                    elif i==1 and n==2:
                        result.append("ยี่"+self.num_text[str(i)])
                    elif n==0:
                        pass
                    else:
                        result.append(self.num_text[n]+self.num_text[str(i)])         
            else:
                result.append(self.num_text[n])
    
            if i>5:
                val+=val
                i=0
            i+=1
        
        return list(reversed(result))
    
    """
        Function    : NumberToTextThai
        Description : This function to convert number to thai text.
        Input       : Number
        Return      : Thai text
        Example     : NumberToTextThai(110)
                    >> ["หนึ่งร้อย","สิบ"]
    """
    def NumberToTextThai(self,number):

        result =[]
        fnumber = 0

        if type(number) not in [int,float]:

            raise TypeError("ต้องใส่ข้อมูลตัวเลข ค่ะ...")
        
        if len(str(abs(number)))>16 or len(str(abs(number)))<1:

            raise ValueError("ตัวเลขที่ใส่จะต้องอยู่ในช่วง 1-16 ตัว ค่ะ")

        if number < 0:
            result.append(self.num_text['-'])
            number = abs(number)
        
        if type(number) in [int]:
            self.number = number
        elif type(number) in [float]:
            self.number = int(number)
            fnumber = Decimal(str(number))%1
            
        result.extend(self.process_int())

        if fnumber >0:
            str1 = str(fnumber)
            for i in range(1,len(str1)):
                if str1[i] =='.':
                    result.append(self.num_text[str1[i]])
                else:
                    result.append(self.num_text[int(str1[i])])

        return result
    

    """
        Function    : TextThaiToNumber
        Description : This function to convert thai text to number.
        Input       : Thai text
        Return      : Number
        Example     : TextThaiToNumber("หนึ่งร้อยสิบจุดสามสองหนึ่ง")
                    >> 110.321
    """

    def TextThaiToNumber(self,txt):
        unit_text = {
            'หนึ่ง':1,'เอ็ด':1,'สอง':2,
            'สาม':3,'สี่':4,'ห้า':5,'หก':6,
            'เจ็ด':7,'แปด':8,'เก้า':9
        }

        deci = {
            "ยี่สิบ":20,"สามสิบ":30,"สี่สิบ":40,"ห้าสิบ":50,
            "หกสิบ":60,"เจ็ดสิบ":70,"แปดสิบ":80,"เก้าสิบ":90
        }

        cross_text = {
            'ร้อย':100,'พัน':1000,'หมื่น':10000,'แสน':100000,'ล้าน':1000000,
        }

        ten = {
            "สิบ":10
        }

        thai_float = {
            "จุด":'.', "ศูนย์":"0","หนึ่ง":'1',"สอง":'2',
            "สาม":'3',"สี่":'4',"ห้า":'5',"หก":'6',
            "เจ็ด":'7',"แปด":'8',"เก้า":'9'
        }

        thai_num = [
            "๑","๒","๓","๔","๕","๖","๗","๘","๙"
        ]

        float_text = ''

        if type(txt) in [int,float]:
            raise TypeError("ข้อมูลที่ป้อนต้องเป็นข้อความ ค่ะ")

        t = re.search(r'[ก-๙]+',txt,re.M|re.I)

        # ตรวจสอบว่าค่าที่รับเข้ามานั้นเป็นข้อความไทยหรือไม่
        if t:
        # ถ้ามีตัวเลขไทย ปะปน ให้เปลี่ยนเป็นช่องว่าง
            for i in thai_num:
                txt = re.sub(str(i),'',txt)

            # ค้นห้าคำว่า จุด
            searchObj = re.search( r'จุด.+', txt, re.M|re.I)

            # กรณีที่พบคำว่า จุด
            if searchObj:
                # เก็บข้อมูลตั้งแต่คำว่าจุดไปจนถึง อักขระ สุดท้าย
                float_text = searchObj.group()

                # เอาค่าจาก float_text มาลบออกในข้อมูลแรก
                txt = re.sub(str(float_text),'',txt)
        else:
            raise ValueError("ข้อมูลที่ให้มาต้องอยู่เป็น ก-๙")
        
        fl = list()

        # ตรวจสอบว่า ข้อมูลใน float_text นั้นไม่มี ช่องว่าง
        if float_text !='':
            # แปลงคำไทยเป็นเลข
            for i in thai_float:
                float_text = re.sub(i,thai_float[i],float_text)
    
            # กำหนดตัวแปร list
            fl = list(float_text)

            # ตรวจสอบความถูกต้องของข้อมูล ถ้ามีข้อมูลใดไม่ใช่ จะแสดง Error ออกมา
            for i in range(len(fl)):
                if fl[i] not in ['.','0','1','2','3','4','5','6','7','8','9']:
                    raise ValueError("มีข้อมูลในจำนวนทศนิยมที่สะกดไม่ถูกอยู่ ค่ะ")
                    break
    
            float_text = ''.join(fl)

        # ค้นหาคำว่าลบ
        obj_minus = re.search(r"ลบ",txt,re.M|re.I)

        minus = ''

        # ถ้าพบคำว่า (ลบ)
        if obj_minus:
            minus = '-'
            txt = re.sub(r"ลบ","",txt)
        # หาคำในหลักสิบที่มากกว่า 20 ขึ้นไป
        for i in deci:
            txt = re.sub(str(i),'+%s'%str(deci[i]),txt)
        # หาคำในหลักหน่วยหรือคำที่เป็นเลข 1-9 รวมคำว่า เอ็ด
        for i in unit_text:
            txt = re.sub(str(i),'+%s'%str(unit_text[i]),txt)
        # หาคำที่อยู๋่ในหลักสิบ 10 -19
        for i in ten:
            txt = re.sub(str(i),'+%s'%str(ten[i]),txt)
        # หาคำที่เป็นตัวคูณ ร้อย สิบ ....
        for i in cross_text:
            if i == "ล้าน":
                txt = re.sub(str(i),')*%s'%str(cross_text[i]),txt)
            else:
                txt = re.sub(str(i),'*%s'%str(cross_text[i]),txt)

        ls = list(txt)

        count=0
        # ถ้าหน่วยมีหลักล้านขึ้น ให้นับจำนวน วงเล็บปิด
        for x in  range(len(ls)):
            if ls[x]==')':
                count+=1
            if ls[x] not in ['(',')','0','1','2','3','4','5','6','7','8','9','+','*']:
                raise ValueError("มีข้อมูลในหลักจำนวนเต็มที่สะกดไม่ถูกอยู่ ค่ะ")
                break
    
        # ตรวจสอบว่า Count >1 ก็ให้สร้าง วงเล็บเปิดตามจำนวน Count
        if count>0:
            ls[0] = ls[0].replace(str(ls[0]),str('('*(count)+ls[0]))

        # แปลงรูปแบบ String ให้เป็นผลลัพธ์แบบตัวเลข
        if ls:
            result = eval(str(''.join(ls)))
        else:
            raise ValueError("ไม่มีข้อมูล ค่ะ")

        total_result = ''

        if minus !='':
            total_result = str(minus)+str(result)+str(float_text)
        else:
            total_result = str(result)+str(float_text)
        
        return total_result






