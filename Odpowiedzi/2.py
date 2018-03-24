# -*- coding: utf8 -*-

"""
Do kalkulatora BMI z lekcji "Python 1 zabawy w konsoli"
dodaj sprawdzanie czy BMI jest prawidłowe

Niedowaga       |   < 18,5
Waga normaln    |   18,5 – 24
Lekka nadwaga	|   24 – 26,5
Nadwaga	        |   > 26,5

W przypadku nadwagi sprawdź czy występuje otyłość:

Otyłość I stopnia   |	30 – 35
Otyłość II stopnia  |	30 – 40
Otyłość III stopnia |	> 40
"""

print("Podaj wagę w kg: ")
weight = float(input())
print("Podaj wzrost w cm: ")
height = float(input())/100
BMI = weight / (height ** 2)

print("Twoje bmi wynosi:", round(BMI, 2))

if (BMI < 18.5):
    print("Niedowaga")
elif (18.5 <= BMI < 24):
    print("Waga prawidłowa")
elif (24 <= BMI < 26.5):
    print("Lekka nadwaga")
else:
    print("Nadwaga")
    if (30 >= BMI > 35):
        print("Otyłość I stopnia")
    elif (35 >= BMI > 40):
        print("Otyłość II stopnia")
    else:
        print("Otyłość III stopnia")
    
