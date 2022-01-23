from functools import reduce

#it is a vending machine
items = {'snickers': 3,  # 3 snickers are left in the vending machine
         'kitkat': 2,
         'twix': 3,
         'cola': 4,
         'fanta': 1,
         'sprite': 0,
         'lipton': 5,
         'juice': 4,
         'кумыс': 0}
money_inside = {'50rub': 40,   # 40 banknotes of 50 ruble are left in the vending machine
                '10rub': 40,
                '5rub': 34,
                '2rub': 44,
                '1rub': 28}
item_code =  {'snickers': 11,  # a code that you enter on a display to get snickers
              'kitkat': 12,
              'twix': 13,
              'cola': 14,
              'fanta': 15,
              'sprite': 16,
              'lipton': 17,
              'juice': 18,
              'кумыс': 19}
item_price = {'snickers': 60,  # snickers costs 60 rubles
               'kitkat': 50,
               'twix': 50,
               'cola': 70,
               'fanta': 60,
               'sprite': 60,
               'lipton': 65,
               'juice': 55,
               'кумыс': 100}


for k, v in item_code.items():
    print(f'product: "{k}" - code: {v}')

def filter_tovara(korzina: dict, code: int) -> str:
    def func(x):
        if korzina[x] == code:
            return True
        else:
            return False
    return list(filter(func, korzina))[0]
print()


while True:
    try:
        nomer = int(input("enter the code of the product: "))
        price = item_price[filter_tovara(item_code, nomer)]
        dengi = int(input(f'the price is {price} rub. '
                          f'how much money will you deposit into the vending machine: '))
    except IndexError:
        print('enter the code of the product correctly.')
        continue
    if items[filter_tovara(item_code, nomer)] == 0:
        print('the product is absent. please, choose another one.')
        continue
    elif dengi < price:
        print('there is not enough money to do the payment.')
        continue
    elif dengi > 100:
        print('100 rub is the maximum payment.')
        continue
    items[filter_tovara(item_code, nomer)] -= 1
    sdacha = dengi - price
    break


def inside_left(func):
    def wrapper(*args, **kwargs):
        global money_inside
        res = func(*args, **kwargs)
        k = -1
        for i in money_inside:
            k += 1
            money_inside[i] -= res[k]
        return f'{res[0]} banknotes of 50 руб, ' \
               f'{res[1]} coins of 10 руб, ' \
               f'{res[2]} coins of 5 руб, ' \
               f'{res[3]} coins of 2 руб, ' \
               f'{res[4]} coins of 1 руб.'
    return wrapper


@inside_left
def cash_back(arg):
    e = arg // 50
    a = (arg - e * 50) // 10
    b = (arg - e * 50 - a * 10) // 5
    c = (arg - e * 50 - a * 10 - b * 5) // 2
    d = (arg - e * 50 - a * 10 - b * 5 - c * 2) // 1
    return [e, a, b, c, d]


print(f'your change is {sdacha} rub: {cash_back(sdacha)}')

cash_inside = int(reduce(lambda x, y: x+y, [i * j for i, j in zip(list(money_inside.values()), [50, 10, 5, 2, 1])]))
items_inside = int(reduce(lambda x, y: x+y, items.values()))
print(f'{cash_inside} rub and {items_inside} products are left in the vending machine.')
