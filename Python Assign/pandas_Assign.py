# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 01:52:14 2020

@author: Sourabh
"""

import pandas as pd

file=r'C:\Users\mahesh\Desktop\Python Assign\Data.csv'
df=pd.read_csv(file)
print(df)
print("----------------------------------------------------")

#Find Male Employee
print("MALE EMPLOYEE")

male = df.loc[(df['Gender']=='M')].Name
print(male)

print("----------------------------------------------------")

#Find Female Employee
print("FEMALE EMPLOYEE")

female = df.loc[(df['Gender']=='F')].Name
print(female)
print("----------------------------------------------------")

# find Male emp with miminum sal
print("Male emp with miminum sal")
print(df.loc[(df.Salary==min(df.Salary))&(df['Gender']=='M')])
print("----------------------------------------------------")

# find Female emp with Maximum sal
print("Female emp with Maximum sal")
print(df.loc[(df.Salary==max(df.Salary))&(df['Gender']=='F')])

print("----------------------------------------------------")

# find emp with Same location 
print("Same Loaction")
print(df[df.duplicated('Location')]) 

print("-----------------------------------------------------")
# find emp with same salary
print("Same Salary")
print(df[df.duplicated('Salary')]) 

print("----------------------------------------------------")
# find emp with same name
print("Same Name")
print(df[df.duplicated('Name')]) 