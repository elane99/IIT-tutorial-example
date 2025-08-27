movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0,
}

purchases = []  # (title, qty)

print("Available movies:")
for title, price in movies.items():
    print(f"{title:14s} ${price:.2f}")

while True:
    title = input("Movie title you choose(or 'done'): ").lower().title()
    if title.lower() == "done":
        break
    if title not in movies:
        print("Unknown title. Available:", ", ".join(movies.keys()))
        continue
    try:
        qty = int(input("Quantity: "))
        if qty <= 0:
            print("Enter a positive quantity.")
            continue
    except ValueError:
        print("Please enter a whole number.")
        continue
    purchases.append((title, qty))

# --- Receipt ---

def apply_group_discount(qty, price):
    """
    Apply 10% discount if quantity >= 4.
    Returns the final line total and a flag indicating if discount was applied.
    """
    total = qty * price
    if qty >= 4:
        total *= 0.90
        return total, True
    return total, False


def apply_member_discount(subtotal, is_member):
    """
    Apply 5% discount if user is a member.
    Returns the final total.
    """
    if is_member:
        return subtotal * 0.95
    return subtotal


# --- Main Logic ---
subtotal = 0.0

print("\nPurchase Summary")
print("{:<14} {:>5} {:>10} {:>12}".format("Movie", "Qty", "Price", "Line Total"))
print("-" * 45)

for title, qty in purchases:
    price = movies[title]
    lt = qty * price
    if qty >= 4:
        lt *= 0.90
    subtotal += lt
    discount_note = " (10% group discount)" if qty >= 4 else ""
    print(f"{title:<14} x{qty:>3d}  @ ${price:>6.2f}  ->  ${lt:>8.2f}{discount_note}")

print("-" * 45)

# Check membership
is_member = input("Are you a member with us (y/n): ").strip().lower().startswith("y")
total = apply_member_discount(subtotal, is_member)

print("\nReceipt:")
print(f"Subtotal: ${subtotal:,.2f}")
if is_member:
    print("Membership discount applied (5%)")
print(f"Total:    ${total:,.2f}")


# --- Summaries ---

tickets_by_movie = {}
revenue_by_movie = {}
for title, qty in purchases:
    price = movies[title]
    lt, _ = apply_group_discount(qty, price)
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0.0) + lt

print("\nSummary Report")
print("{:<20} {:>10} {:>12}".format("Movie", "Tickets", "Revenue"))
print("-" * 44)

for title in tickets_by_movie:
    tickets = tickets_by_movie[title]
    revenue = revenue_by_movie[title]
    print("{:<20} {:>10} {:>12}".format(title, tickets, f"${revenue:,.2f}"))

# Top seller by tickets
if tickets_by_movie:
    top_title = max(tickets_by_movie, key=tickets_by_movie.get)
    print("Top seller:", top_title)
    print("Quantity:", tickets_by_movie[top_title])