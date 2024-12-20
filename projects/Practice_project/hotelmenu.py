menu = {
    'pizza': 90,
    'burger': 70,
    'cocacola': 40,
    'coldcofee': 50,
}
print("Wellcome to our Resturant")
print("pizza:Rs90\nburger:Rs70\ncocacola:Rs40\ncoldcoffee:Rs50")
order_total = 0
item1 = input("Enter the name of the item you want:")
if item1 in menu:
    order_total += menu[item1]
    print(f"your item{item1}has been added to your order")
else:
    print(f"Ordered item{item1}is not available")
another_order = input("Do you want order something else?(Yes/No)")
if another_order == "Yes":
    item2 = input("Enter the other item:")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Item{item2} has been added to order")
    else:
        print(f"Ordered item{item2} is not available!!!")
print(f" The amount of items  to pay is{order_total} ")
