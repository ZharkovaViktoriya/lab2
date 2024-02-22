a=input("Введите пароль: ")
b=input("Подтвердите: ")
if a.isdigit()==True and b.isdigit()==True and len(a)==len(b):
    if a==b:
        print("Пароль принят")
    else:
        print("Пароль не принят")
else:
    print("Пароль не принят")
