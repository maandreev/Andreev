import os
from dotenv import load_dotenv

load_dotenv()
# ITEMS(Количесто в заказе) = 3
# SUM(Сумма заказа) = 100.00
# ORDER_NUM(Номер в очереди) 265
items = int(os.getenv('ITEMS'))
sum = float(os.getenv('SUM'))
order_num = int(os.getenv('ORDER_NUM'))

# 1. Касса перепутала номер в очереди с суммой. Надо поменять эти переменные местами
order_num, sum = sum, order_num
print('ORDER_NUM:', order_num, 'SUM:', sum)
...

# 2. Для отчёта боссу, нужно посчитать среднюю стоимость каждой пиццы в заказе
print('Средняя стоимоть пиццы: ', sum/order_num)

...

# 3. Если в сумме заказа нету дробей (.00), нужно, чтобы нули не отрисовывались
order_num = int(100.11)
print(order_num)
...

# 4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%
...

# 5. Если кол-во пицц в заказе меньше 2, от номер в очереди нужно сократить на 5