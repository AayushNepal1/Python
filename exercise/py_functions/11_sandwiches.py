def order_sandwich(*orders):
    print("\nMaking a sandwich with following toppings:")
    for order in orders:
        print(f"- {order}")

order_sandwich('cheese')
order_sandwich('chicken', 'green salid', 'plain')
order_sandwich('carrot', 'mushooms')
