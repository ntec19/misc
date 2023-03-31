#!/usr/bin/env python3

import sys

try:
    import openpyxl
except ImportError:
    print("Bibliothèque 'openpyxl' introuvable !")
    exit(1)

if len(sys.argv) != 2:
    print(f"Usage : {sys.argv[0]} <fichierExcelADéprotéger>")
    exit(2)

fichier = sys.argv[1]

# retirer la protection du classeur
wb = openpyxl.load_workbook(fichier)
wb.security.lockStructure = False
wb.save(fichier)
wb.close()

# retirer la protection de toutes les feuilles
wb = openpyxl.load_workbook(fichier)
liste_feuilles = wb.sheetnames
for feuille in liste_feuilles:
    print(feuille)
    ws = wb[feuille]
    ws.protection.disable()
wb.save(fichier)
wb.close()

print("terminé !\n")
