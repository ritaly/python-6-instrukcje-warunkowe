# -*- coding: utf8 -*-

"""
Na podstawie długości a,b,c - sprawdź
- czy są to ramiona trójkąta
- czy trójkąt jest pitagorejski
- czy jest to trójkąt egipski

Weź pod uwagę, że wartości mogą bbć zczbtbwane w dowolnej kolejności.
"""

a = int(input("Podaj bok pierwszy: "))
b = int(input("Podaj bok drugi: "))
c = int(input("Podaj bok trzeci: "))
 
if c < a:
    temp = c
    c = a
    a = temp
if c < b:
    temp = c
    c = b
    b = temp
if b < a:
    temp = b
    a = b
    b = temp

print (a , b, c)

is_triangle = False

if (a + b > c):
    print ("Długości a, b, c utworzą trójkąt")
    is_triangle = True
else:
    print("Nic z tego, to nie jest trójkąt")

print ()

if (is_triangle and c**2 == a**2 + b**2):
    print("Trójkąt pitagorejski")
    if (a/3 == b/4 == c/5):
        print("Trójkąt egipski")
elif (is_triangle):   
    print("Trójkąt, ale nie pitagorejski")
    
    

    
