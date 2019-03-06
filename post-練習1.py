# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 23:03:49 2019

@author: ASUS
"""
import csv
fn=r'Post_All.csv'
with open(fn,encoding='UTF-8-sig') as csvFile:
    csvReader=csv.reader(csvFile)
    listReport=list(csvReader)
    col=listReport[0]
    print(col)
    col1=len(listReport)
    print(col1-1)
    x=[]
    y=[]
    post=[]
    sat=[]
    sun=[]
    taipost=[]
    otherpost=[]
    taisat=[]
    othersat=[]

    
    for i in range(1,col1):
        if listReport[i][14]!='':
            post+=[listReport[i]]
        if listReport[i][15]!='':
            sat+=[listReport[i]]
        if listReport[i][16]!='':
            sun+=[listReport[i]]
    
    postnum=len(post)
    satnum=len(sat)
    sunnum=len(sun)
    
    print('全台郵局總數:{},平日延時提供服務家數:{},周六提供服務家數:{},周日提供服務家數:{}'.format(col1-1,postnum,satnum,sunnum))

    
    for i in range(0,postnum):
        if post[i][8]=='臺北市':
            taipost+=[post[i]]
        else:
            otherpost+=[post[i]]
    
    for i in range(0,satnum):
        if sat[i][8]=='臺北市':
            taisat+=[sat[i]]
        else:
            othersat+=[sat[i]]
            
    taipostnum=len(taipost)
    otherpostnum=len(otherpost)
    taisatnum=len(taisat)
    othersatnum=len(othersat)
    
    print("臺北市平日延時服務家數:{},其它地區平日延時服務家數:{}".format(taipostnum,otherpostnum))
    print("台北市周六營業家數:{},其它地區周六營業家數:{}".format(taisatnum,othersatnum))


import matplotlib.pyplot as plt
   
act=['全台家數','平日延時家數']
pienum=[col1-postnum,postnum]
colors=['lightgreen','lightblue']
plt.pie(pienum,labels=act,colors=colors,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
plt.axis('equal')
plt.show()

act=['全台家數','周六營業家數']
pienum=[col1-satnum,satnum]
colors=['purple','grey']
plt.pie(pienum,labels=act,colors=colors,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
plt.axis('equal')
plt.show()


act=['台北平日平日延時營業家數','其它地區平日延時營業家數']
pienum=[taipostnum,otherpostnum]
colors=['pink','brown']
plt.pie(pienum,labels=act,colors=colors,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
plt.axis('equal')
plt.show()

act=['台北周六營業家數','其它周六營業家數']
pienum=[taisatnum,othersatnum]
colors=['red','yellow']
plt.pie(pienum,labels=act,colors=colors,shadow=True,explode=(0,0.1),autopct='%1.1f%%')
plt.axis('equal')
plt.show()

   
    
            
        
        
        
        
    