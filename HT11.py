import keyword
my_str = input('Задайте переменную :')
a = 0
for i in keyword.kwlist:
    if i == my_str:
        a = 1
if my_str != '_':
    z = list(my_str)
    x = 0
    while x != len(z):
        if z[x] != '_':
            x += 1
        else:
            del (z[x])
            x += -1
    z = "".join(z)
    if my_str[0].isdigit():
        print('Переменная не может начинаться с цифры')
    elif not my_str.islower() and not z.isdigit():
        print('Переменная не может содержать заглавные буквы')
    elif not z.isalnum():
        print('Переменная не может содержать знаки пунктуации и символы')
    elif a == 1:
        print("Такая переменная уже существует")
    else:
        print('Такая переменная возможна')
else:
    print('Такая переменная возможна')
print('END')
