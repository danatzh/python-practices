name=input("Enter your name: ")
count=0
subtotal=0.0
product=input("Enter product name (or 'done' to finish): ")
while product!='done':
    price=int(input("Enter price: "))
    subtotal+=price
    count+=1
    product=input("Enter product name (or 'done' to finish): ")
print()
print("Customer : ", name.upper())
print("Items : ", count)
print("Subtotal: ", subtotal, "KZT")
print("-"*30)
discount=0.0
if 3000<=subtotal<7000:
    discount=subtotal*0.05
    discount_tier="5% discount"
elif subtotal>+7000:
    discount=subtotal*0.05
    discount_tier="15% discount"
else:
    discount_tier="No discount"
total=subtotal-discount
print("Discount tier : ", discount_tier)
print("Discount : ", discount, "KZT")
print("Total : ", total, "KZT")
print("-"*30)
print("Name uppercase : ", name.upper())
print("Name lowercase : ", name.lower())
print("Name length : ", len(name))
if len(name)>5:
    print("Long name")
else:
    print("Short name")
