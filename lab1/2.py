mesto=int(input())
if mesto in range(1,55):
    if mesto in range(2,37) and mesto%2==0:
        print("Верхнее купе")
    elif mesto in range(1,36) and mesto%2!=0:
        print("Нижнее купе")
    elif mesto in range(37,55):
        if mesto%2==0:
            print("Верхнее боковое")
        elif mesto%2!=0:
            print("Нижнее боковое")
else:
    print("Неверный ввод данных")

