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
        
        #DOB = Date of Birth
        self.DOB = input("Enter Date of Birth (dd.mm.yyyy): ")
        DOB = self.DOB
        
        for i in range(len(DOB)):
           if (DOB[i] == "."):
               self.dd   = (DOB[:i-3])
               self.mm   = (DOB[3:i])
               self.yy   = (DOB[i+3:])
               self.yyyy = (DOB[i+1:])
               

        dd   = int(self.dd) #birth day
        mm   = int(self.mm) #birth month
        yy   = self.yy #birth year (last 2 digits)
        yyyy = int(self.yyyy) #birth year
        
        
        if dd < 1 or dd > 31:
            raise ValueError ("Invalid Input! Birth month is " 
                              "less/greater than 1 or 31 respectively")
            
        if mm < 1 or mm > 12:
            raise ValueError ("Invalid Input! Birth month is " 
                              "less/greater than 1 or 12 respectively")
            
        if yyyy > dt.year:
            raise ValueError ("Invalid Input! Birth Year is greater than current year", dt.year)
        
        
        if mm < 10:
            #self.DOB = int("%s%s%s"  %(birth_day, birth_month, birth_year ))
            self.DOB = int(f"{dd}0{mm}{yyyy}")
            self.birth_no = int(f"{dd}0{mm}{yy}")
        else:
            self.DOB = int(f"{dd}{mm}{yyyy}")
            self.birth_no = int(f"{dd}0{mm}{yy}")


        DOB      = self.DOB
        birth_no = self.birth_no
        
        self.age = dt.year - yyyy
        
        if dt.month < mm or dt.month == mm and dt.day < dd:
            self.age -= 1
            
        age = self.age

        
    
        self.info = {"First Name": fst_name, 
                "Last Name": lst_name, 
                "Age": age,  
                "D.O.B.": DOB,
                "birth_no": birth_no}

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
        
        sbj = [eng, phy, math] #subject grades in numbers
        #if eng or phy or math > 100:
        for i in sbj:
            if i >100 or i <0:
                raise ValueError ("Invalid Input! Value must be between 0 - 100")
                
        
        self.avg_grd = sum(sbj) / len(sbj)
        avg_grd = self.avg_grd
        

        sbj_grades = [] #Subject grades in letters i.e A,B,C...

        #"""
        for i in sbj:
            if i >= 92 and i < 101:
                sbj_grades.append("A")
            elif i >= 77 and i < 92:
                sbj_grades.append("B")
            elif i >= 58 and i < 77:
                sbj_grades.append("C")
            elif i >= 46 and i < 58:
                sbj_grades.append("D")
            else:
                sbj_grades.append("F")
                #"""
                
            
        info["English"] = sbj_grades[0]
        info["Physics"] = sbj_grades[1]
        info["Mathematics"] = sbj_grades[2]
        
        info["Average Grade"] = avg_grd
        
        #print(info)
        ans = input("Would like to overwrite this data? (y/n) \n") 
        if ans == "y":
            self.overwrite()
        else:
            pass

    def overwrite(self):

        keys = [i for i in self.info.keys()]
        values = [i for i in self.info.values()]

        python_file = open("school_register.txt", "w")
        
        for i in range(len(keys)):
            python_file.write("{: <15} {: <20} \n".format (keys[i],values[i]))
        
        python_file.close()
        print("school_register.txt overwrited!")
        
if __name__ == '__main__':

    x = Student()
    #print(x.math)

    
