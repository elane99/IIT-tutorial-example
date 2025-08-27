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
    title = input("Movie title (or 'done'): ")
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

def line_total(qty, price_each):
    total = qty * price_each
    if qty >= 4:            # 10% group discount on that line
        total *= 0.90
    return total

subtotal = 0.0
print("\nReceipt:")
for title, qty in purchases:
    price = movies[title]
    lt = line_total(qty, price)
    subtotal += lt
    print(f"{title:14s} x{qty:2d}  @ ${price:.2f}  ->  ${lt:.2f}")

is_member = input("Member code? (y/n): ").strip().lower().startswith("y")
total = subtotal * (0.95 if is_member else 1.0)
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total:    ${total:.2f}")

# --- Summaries ---

tickets_by_movie = {}
revenue_by_movie = {}
for title, qty in purchases:
    price = movies[title]
    lt = line_total(qty, price)
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0.0) + lt

print("\nSummary (tickets):", tickets_by_movie)
print("Summary (revenue):", revenue_by_movie)

# Top seller by tickets
if tickets_by_movie:
    top_title = max(tickets_by_movie, key=tickets_by_movie.get)
    print("Top seller:", top_title, tickets_by_movie[top_title])