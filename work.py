# задача 1

def rate(rub, dollar):
    dollar = 0.011
    return rub * dollar

print(rate(rub=300, dollar=0.011))

# задача 2

def age(years):
    if years < 18:
        print('Доступно только лицам 18+')
    elif years >= 18:
        print('Доступ разрешён')

age(20)