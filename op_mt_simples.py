n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
op = input("Digite a operação que deseja (+,-,*,/): ")
if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print("Operação invalida")
