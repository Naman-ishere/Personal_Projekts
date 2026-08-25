print("Welcome to the Mini Shopping Cart.")
print("Your best friend if you are Dori(ifykyk) or from a minor dementia known as clumsiness.")
print("Due to ChatGPT, this thing can only take 5 items (cart is short gng)")

item1 = int(input("Enter the price of first item: "))
item2 = int(input("Enter the price of second item: "))
item3 = int(input("Enter the price of third item: "))
item4 = int(input("Enter the fourth of item: "))
item5 = int(input("Enter the fifth of item: "))

itemPrices = [item1, item2, item3, item4, item5]
print("Total price:", sum(itemPrices))
print("Average price", sum(itemPrices) / len(itemPrices))
print("Most expensive:", max(itemPrices))
print("Cheapest:", min(itemPrices))
