# -*- coding: utf8 -*-

"""
Utwórz listę imion męskich / żeńskich.
Użytkownik podaje imię.
Jeśli imię istnieje na liście wyświetl czy jest to imię męskie czy żeńskie
Jeżeli nie dodaj imię do zbioru wraz z oznaczeniem płci.
"""

dict_names = {
    "Anna" : "zenskie",
    "Julia" : "zenskie",
    "Zofia" : "zenskie",
    "Maja" : "zenskie",
    "Hania" : "zenskie",
    "Maria" : "zenskie",
    "Stanisława" : "zenskie",
    "Michał" : "meskie",
    "Antoni" : "meskie",
    "Jan" : "meskie",
    "Franciszek" : "meskie",
    "Piotr" : "meskie",
    "Wiktor" : "meskie",
    "Wawrzyniec" : "meskie"
    }

name = input("Podaj imię: ")

if (name in list(dict_names.keys())):
    print(name, "to imię", dict_names[name])
else:
    print("Nie mamy tego imienia! Dodaj je do zbioru")
    gender = input("To imię męskie czy żeńskie? wpisz m / z: ")
    if (gender == "m"):
        dict_names[name] = "meskie"
    else:
        dict_names[name] = "zenskie"
    print (list(dict_names.keys()))

