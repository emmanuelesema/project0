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


        print(self.stdnt_info())
        
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

        
    
        info = {"First Name": fst_name, 
                "Last Name": lst_name, 
                "Age": age,  
                "D.O.B.": DOB}
        
        print()
        print("Today's date: %s/%s/%s"  %(dt.day, dt.month, dt.year ))
        print()
        
        return info
        
if __name__ == '__main__':
    #Student("Bobby Esema")
    #Student("James Etokebe")
    Student()


