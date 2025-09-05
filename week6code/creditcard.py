old_balance = float(input("Enter old balance: "))
charges     = float(input("Enter charges for month: "))
credits     = float(input("Enter credits: "))

new_balance = 1.015 * old_balance + charges - credits

if new_balance <= 20:
    minimum_payment = new_balance
else:
    minimum_payment = 20 + 0.10 * (new_balance - 20)

print("New balance: ${:.2f}".format(new_balance))
print("Minimum payment: ${:.2f}".format(minimum_payment))
