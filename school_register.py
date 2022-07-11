import numpy as np
import matplotlib.pyplot as plt

class Student:
    def __init__(self, name):
        self.name = name
        
        for i in range(1,len(name)):
            if (name[i] == " "):
                self.fst_name = name[:i]
                self.lst_name = name[i+1:]


        print(self.stdnt_info())
        
    def stdnt_info(self):
        
        """
        Creating and Saving Student Information

        Returns
        -------
        Dict. of Student Info.

        """
        
        fst_name = self.fst_name
        lst_name = self.lst_name
        self.age = int(input('Enter Student age: '))
        age = self.age

        
        info = {"First Name": fst_name, "Last Name": lst_name, "Age": age}
        
        return info
        
if __name__ == '__main__':
    Student("Bobby Esema")
    Student("James Etokebe")
