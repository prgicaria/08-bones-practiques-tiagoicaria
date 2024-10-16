#!/usr/bin/env python
'''
Divisio, Calcular la divisio entre dos nombres enters
Institut Icària
Programació - 1r Batxillerat - Curs 2023-24
Dona el resultat de la divisio, el quocient y el residu
'''
__author__ = "Tiago"
__contact__ = "tquispe@instituticaria.cat"
__date__ = "2024/10/16"

dividend = int(input("introduïu el dividend:"))
divisor = int(input("introduïu el divisor:"))
divisio = dividend/divisor
quocient = dividend//divisor
residu = dividend % divisor
print(f"Divisió: {dividend}/{divisor}")
print("Quocient:", quocient)
print("Residu:", residu)
