#SUMATORIA DE LOS NUMEROS PARES QUE HAY DESDE EL 1 AL 30 UTILIZANDO FOR
total = 0
for i in range(2, 31, 2):  # pares del 2 al 30
    total += i
print(f"Sumatoria de los números pares del 1 al 30: {total}")