n = int(input("Digite um número:"))
if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 and n != 2 and n != 3 and n != 5:
    print("Não é primo")
    x = ""
    for i in range(1, n + 1):
        if n % i == 0:
            i = str(i)
            x += i + " "
    print(x)
else:
    x = ""
    for i in range(1, n + 1):
        if n % i == 0:
            i = str(i)
            x += i + " "
    print(x)
    print("É primo")