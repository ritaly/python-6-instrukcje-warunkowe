# -*- coding: utf8 -*-

"""
Wskaż najwyższą wartość z 3 liczb
i posortuj je od największej do najmniejszej.
"""
x = 34
y = 107
z = 7

if (x > y) and (x > z):
 maximum = x
elif (y > x) and (y > z):
 maximum = y
else:
 maximum = z

print(maximum)


if x < y:
    temp = x
    x = y
    y = temp
if x < z:
    temp = x
    x = z
    z = temp
if y < z:
    temp = y
    y = z
    z =temp
print (x , y, z)


