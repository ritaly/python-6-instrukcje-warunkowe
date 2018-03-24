# -*- coding: utf8 -*-

"""
Zapytaj użytkownika o wiek.
W zależności od wieku zwróć czy użytkownik jest już pełnoletni
lub ile lat zostało mu do pełnoletności,
Użytkownikom powyżej 100lat życz 200 ;)
"""

print("Ile masz lat?")
age = int( input() )
if ( age >= 18 ):
    print("Użytkownik pełnoletni")
if ( age > 100 ):
    print("♫ 200 lat ♫")
else:
    print("Użytkownik niepełnoletni")
    print("Do 18. urodzin zostało", 18 - age, "lat")
