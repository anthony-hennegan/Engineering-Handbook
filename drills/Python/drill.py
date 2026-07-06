book_count = input("How many books would you like to check out? ")
book_count = int(book_count)

if book_count > 3:
    print("You can only check out 3 books.")
else:
    print("Checkout amount is approved.")

late_fee_amount = input("How much is the late fee?" )
late_fee_amount = float(late_fee_amount)
print(late_fee_amount)

num = 20
num = str(num)
print(num)
print(type(book_count))
print(type(late_fee_amount))
print(type(num))

