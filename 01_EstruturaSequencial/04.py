# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Nota Bimestre I: "))
nota2 = float(input("Nota Bimestre II: "))
nota3 = float(input("Nota Bimestre III: "))
nota4 = float(input("Nota Bimestre IV: "))

total = nota1 + nota2 + nota3 + nota4
media = total / 4

print("A média dos bimestres foi: ", media, "pontos.")
