def main():
    # 1) Get inputs from the user (as numbers).
    old_balance, charges, credits = input_data()

    # 2) Do the math to compute new balance and minimum payment.
    new_balance, minimum_payment = calculate_new_values(old_balance, charges, credits)

    # 3) Show the results nicely formatted (two decimals, with $).
    display_new_data(new_balance, minimum_payment)


def input_data():
    """
    This function is a little 'machine' that ONLY asks for input.
    It returns three numbers that other functions will use.
    - old balance: what you owed before this month
    - charges: what you spent this month
    - credits: what you paid back (or refunds)
    """
    # input(...) shows a message and waits for the user to type something.
    # float(...) converts the typed text into a decimal number like 123.45
    old_balance = float(input("Enter old balance: "))
    charges     = float(input("Enter charges for month: "))
    credits     = float(input("Enter credits: "))

    # Return all three results at once as a "tuple".
    return old_balance, charges, credits


def calculate_new_values(old_balance, charges, credits):
    """
    This function ONLY does the math.
    Step by step idea (paper version):
      1) Start from OLD balance and add 1.5% interest -> multiply old balance by 1.015
      2) Add this month's charges
      3) Subtract credits (payments/refunds)
      4) Use the minimum payment rule
    """
    # 1.5% interest on the OLD balance means multiplying by 1.015
    new_balance = 1.015 * old_balance + charges - credits

    # Minimum payment rule:
    # - If new_balance is small (<= 20), pay it all.
    # - Otherwise, pay $20 + 10% of the amount above $20.
    if new_balance <= 20:
        minimum_payment = new_balance
    else:
        minimum_payment = 20 + 0.10 * (new_balance - 20)

    # Give both numbers back to whoever called this function.
    return new_balance, minimum_payment


def display_new_data(new_balance, minimum_payment):
    """
    This function ONLY displays the final answers.
    {:.2f} means 'format with 2 decimal places', e.g., 253.0 -> 253.00
    """
    print("New balance: ${:.2f}.".format(new_balance))
    print("Minimum payment: ${:.2f}.".format(minimum_payment))


# This actually starts the program.
main()
