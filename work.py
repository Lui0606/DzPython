# задача 1

def rate(rub, dollar):
    dollar = 0.011
    return rub * dollar

print(rate(rub=300, dollar=0.011))

# задача 2

def age(years):
    if years < 18:
        print('False')
    elif years >= 18:
        print('True')

age(20)