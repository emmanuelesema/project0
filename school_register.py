import numpy as np
import matplotlib.pyplot as plt
import datetime


class Student:
    def __init__(self):
        self.name = input("Name of Student: ")
        name = self.name
        self.dt = datetime.datetime.now()   #date today
        
        for i in range(1,len(name)):
            if (name[i] == " "):
                self.fst_name = name[:i]
                self.lst_name = name[i+1:]
                
        self.stdnt_info()
        self.stdnt_grades()

        
    def stdnt_info(self):
        
        """
        Creating and Saving Student Information in dictionaries

        Returns
        -------
        Dict. of Student Info.

        """
        
        fst_name = self.fst_name
        lst_name = self.lst_name
        dt = self.dt #date today
        
        self.DOB = input("Enter Date of Birth (dd.mm.yyyy): ")
        DOB = self.DOB
        
        for i in range(len(DOB)):
           if (DOB[i] == "."):
               self.birth_day = (DOB[:i-3])
               self.birth_month = (DOB[3:i])
               self.birth_year = (DOB[i+1:])
               

        birth_day = int(self.birth_day)
        birth_month = int(self.birth_month)
        birth_year = int(self.birth_year)
        
        #print("dd", birth_day, "mm", birth_month, "yyyy", birth_year)
        
        if birth_day < 1 or birth_day > 31:
            raise ValueError ("Invalid Input! Birth month is " 
                              "less/greater than 1 or 31 respectively")
            
        if birth_month < 1 or birth_month > 12:
            raise ValueError ("Invalid Input! Birth month is " 
                              "less/greater than 1 or 12 respectively")
            
        if birth_year > dt.year:
            raise ValueError ("Invalid Input! Birth Year is greater than current year", dt.year)
        
        
        if birth_month < 10:
            #self.DOB = int("%s%s%s"  %(birth_day, birth_month, birth_year ))
            self.DOB = int(f"{birth_day}0{birth_month}{birth_year}")
        else:
            self.DOB = int(f"{birth_day}{birth_month}{birth_year}")

        DOB = self.DOB
        
        
        self.age = dt.year - birth_year
        
        if dt.month < birth_month or dt.month == birth_month and dt.day < birth_day:
            self.age -= 1
            
        age = self.age

        
    
        self.info = {"First Name": fst_name, 
                "Last Name": lst_name, 
                "Age": age,  
                "D.O.B.": DOB}

        info = self.info
        
        print()
        print("Today's date: %s/%s/%s"  %(dt.day, dt.month, dt.year ))
        print()
        
        print(info)
        
    
    def stdnt_grades(self):
        """
        Inserting student grades

        Returns
        -------
        Updated dict. with grades 

        """
        
        #A – 92 %

        #B – 77%

        #C - 58%

        #D - 46%

        #E - 40%
        
        info = self.info
                
        self.eng = int(input("Enter English grade (%): "))        
        self.phy = int(input("Enter Physics grade (%): "))
        self.math = int(input("Enter Mathematics grade (%): "))
    
        print()

        eng = self.eng
        phy = self.phy
        math = self.math
        
        #if eng or phy or math > 100:
        if eng > 100 or eng < 0:
          raise ValueError ("Invalid Input! Value must be between 0 - 100")
          
        if phy > 100 or phy < 0:
          raise ValueError ("Invalid Input! Value must be between 0 - 100")
          
        if math > 100 or math < 0:
          raise ValueError ("Invalid Input! Value must be between 0 - 100")
        
        self.avg_grd = (eng + phy + math) / 3
        avg_grd = self.avg_grd
        
        if eng >= 92 and eng < 101:
            eng = "A"
        elif eng >= 77 and eng < 92:
            eng = "B"
        elif eng >= 58 and eng < 77:
            eng = "C"
        elif eng >= 46 and eng < 58:
            eng = "D"
        else:
            eng = "F"
            
            
        if phy >= 92 and phy < 101:
            phy = "A"
        elif phy >= 77 and phy < 92:
            phy = "B"
        elif phy >= 58 and phy < 77:
            phy = "C"
        elif phy >= 46 and phy < 58:
            phy = "D"
        else:
            phy = "F"
            
            
        if math >= 92 and math < 101:
            math = "A"
        elif math >= 77 and math < 92:
            math = "B"
        elif math >= 58 and math < 77:
            math = "C"
        elif math >= 46 and math < 58:
            math = "D"
        else:
            math = "F"


        info["English"] = eng
        info["Physics"] = phy
        info["Mathematics"] = math
        
        info["Average Grade"] = avg_grd
        
        print(info)
        
    
        
if __name__ == '__main__':
    #Student("Bobby Esema")
    #Student("James Etokebe")
    Student()
    

