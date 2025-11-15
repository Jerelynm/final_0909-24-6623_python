#REALIZACIÓN DE LA TABLA DEL 5 CON NÚMEROS PARES UTILIZANDO FOR

n = int(input("Número para la tabla: "))
for i in range(2, n*1, 2):
    print(f"{n} x {i} = {n * i}")