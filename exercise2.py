from collections import deque

def carculator(prices):
    n = len(prices)
    deque_list = deque()
    result = []

    for i in range(n):
        deque_list.append(0)
        for j in range(i + 1, n):
            if prices[i] <= prices[j]:
                deque_list[i] += 1
    for k in deque_list:
        result.append(k)

    return result

print('Enter prices in the size(1 <= price <= 10000)')
print('Enter (2 <= price <= 100000) of the prices')
while True:
    try:
        enter_list = input("Enter prices for making list: ")
        split_list = enter_list.split()
        price_check = 0
        if enter_list == 'done':
            print('End')
            break
        for price in split_list:
            price = int(price)
            if price < 1 or price > 10000:
                price_check += 1
        if price_check != 0:
            print('Please enter prices in the size(1 <= price <= 10000)')
        elif len(split_list) < 2 or len(split_list) > 100000:
            print('Please enter (2 <= price <= 100000) of the prices')
        else:
            print("prices\n", split_list)
            print("result\n", carculator(split_list))
    except:
        print('Please, enter a number for price')
        continue