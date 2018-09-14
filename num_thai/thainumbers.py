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






