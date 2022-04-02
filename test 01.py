# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:16:23 2022

@author: Admin
"""

#converting into uppercase using map  fncnt question.9
input=map(lambda x:x.upper(), ['True','FALse','tRUe','FalSe','faLse'])
output= list(input)
print(output)

#fruits 3rd question
names_of_fruits = (('Lemon','sour'),('DragonFruit', 'Sweet'),('Grapes','soUr'),('Kiwi','Sour'),('Apples', 'sweet'),('Orange', 'sour'),('Blueberries','sweet'),('Limes','Sour'))
sour_taste_fruits=[]

for j in names_of_fruits:
    if(j[1].lower()=='sour'):
        sour_taste_fruits.append(j[0])
 
print("Sour Fruits:", sour_taste_fruits)

#2nd question
def solve(n):
    dict = { 'Square': lambda a : a**2, 
         'Cube': lambda a : a**3, 
         'Squareroot': lambda a : a**(1/2)}
    result = 0
    for k in dict.keys():
        result += dict[k](n)
    return result    
print(round(solve(6),2))  

#4th question:
list_of_words= ['hello' , 'Dear' , 'hOw' , 'You' , 'ARe']
result = []
for i in list_of_words:
    if i[1].isupper():
        result.append(i)
print(result)

#6th question
names = ["santa Maria" , "Hello World" , " Merry christmas", "tHank You"]


result = []
for i in names:
    a ,b = i.split()
    if a[0].isupper(): 
        result.append(a)
    if b[0].isupper():result.append(b)
print(result)

#10th question
dates=['17-12-1997','22-04-2011','01-05-1993','19-06-2020']
result=[]
for s in dates:
    d=s.split("-")
    result.append(d[2])
    print("your result is:",result)
    
    
