# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 01:35:15 2020

@author: Sourabh
"""
#Create .csv file using DataFrame,csv file auto create using this code

import pandas as pd

dict1 = {"Name":['Neha', 'Deepak','Jyoti','Mohini','Deepak'],
        "Gender":['F','M','F','F','M'],
        "Location":['Burhanpur','Pune','Bhopal','Pune','Pune'],
        "Salary":[80000,15000,25000,25000,50000]}
df = pd.DataFrame(dict1)
df.to_csv('Data.csv',index=False)#For Save,here Data.csv is a file_name
print(df)

#Find Male Employee
