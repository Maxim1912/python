a = 33
b = [12, "ok", "567"]
# print(b[:2])



shop = ["cheese", "chips", "juice", "water", "onion", "apple", "banana", "lemon", "lime", "carrot", "bacon", "paprika"]

new_element = input("Что ещё купить?\n")
if new_element not in shop:
    shop.append(new_element)

print('We need to buy:')
for element in shop:
    print(" - ", element)

