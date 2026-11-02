a = float(input("Первое число: "))
op = input("Операция (+, -, *, /, **, %): ")
b = float(input("Второе число: "))

if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
elif op == "*":
    print("Результат:", a * b)
elif op == "/":
    if b == 0:
        print("Ошибка: на ноль делить нельзя")
    else:
        print("Результат:", a / b)
elif op == "**":
    print("Результат:", a ** b)
elif op == "%":
    if b == 0:
        print("Ошибка: на ноль делить нельзя")
    else:
        print("Результат:", a % b)
else:
    print("Неизвестная операция")