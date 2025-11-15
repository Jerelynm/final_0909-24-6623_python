#REALIZACIÓN DE LA TABLA DEL 5 PERO CON LOS NÚMEROS IMPARES UTILIZANDO WHILE

m = int(input("Cantidad de números impares a mostrar: "))
i = 1
count = 0
while count < m:
    print(f"5 x {i} = {5 * i}")
    i += 2
    count += 1

