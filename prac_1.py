name=input("Input Customer name: ")
product=input("Input Product name: ")
price=float(input("Input Price per unit in KZT: "))
quantity=int(input("Input Quantity: "))
subtotal=price*quantity
if subtotal>5000:
    discount=subtotal*0.10
else:
    discount=0
total=subtotal-discount
line="="*30
divider="-"*30
print(
    f"{line}\n"
    f"        SHOP RECEIPT\n"
    f"{line}\n"
    f"Customer : {name}\n"
    f"Product : {product}\n"
    f"Price : {price} KZT\n"
    f"Quantity : {quantity}\n"
    f"{divider}\n"
    f"Subtotal : {subtotal} KZT\n"
    f"Discount : {discount} KZT\n"
    f"Total : {total} KZT\n"
    f"{line}"
    )
print("Discount applied: ", subtotal>5000)
print("Paid more than 3000: ", total>3000)
