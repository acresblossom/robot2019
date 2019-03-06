# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 22:14:30 2019

@author: ASUS
"""

import csv
fn = r'bank ranking.csv'
with open(fn, encoding='UTF-8-sig') as csvFile:
    csvReader=csv.reader(csvFile)
    listReport=list(csvReader)
    
    x=[]
    y=[]
    y1=[]
    print(listReport[0])
    col=len(listReport[0])
    print(col)
    col1=len(listReport)
    print(col1)
    for i in range(1,col):
        x+=[listReport[i][3]]
        y+=[listReport[i][7]]
        y1+=[eval(listReport[i][7])]

print("{:2s}{:6s}{:3s}{:14s}{:3s}".format(listReport[0][0],listReport[0][1],listReport[0][2],listReport[0][7],listReport[0][3]))


for row in listReport[1:11]: 
    print("{:5s}{:3s}{:^8s}{:^15s}{:8s}".format(row[0],row[1],row[2],row[7],row[3]))
    
import matplotlib.pyplot as plt
width=0.5


plt.figure(dpi=50,figsize=(15,5))
plt.title("銀行總額",fontsize=15)
plt.xlabel("銀行別",fontsize=15)
plt.ylabel("資產總額-新臺幣百萬元",fontsize=15)
plt.bar(x,y1,width,facecolor='blue',edgecolor='yellow',alpha=0.5)
plt.grid()
plt.show()