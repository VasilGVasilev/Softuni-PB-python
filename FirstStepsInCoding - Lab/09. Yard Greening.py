meter = float(input())
price = meter * 7.61
discount = (price * 18)/100
last_price = price - discount
print(f'The final price is: {last_price} lv.')
print(f'The discount is: {discount} lv.')