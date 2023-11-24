class McDonaldsShell:
    def __init__(self):
        self.orders = []
        self.service_charge_rate = 0.1  # 10% service charge

    def place_order(self, item, quantity, price):
        order = {"item": item, "quantity": quantity, "price": price}
        self.orders.append(order)

    def calculate_order_amount(self):
        return sum(order["quantity"] * order["price"] for order in self.orders)

    def calculate_service_charge(self, order_amount):
        return order_amount * self.service_charge_rate

    def generate_bill(self):
        order_amount = self.calculate_order_amount()
        service_charge = self.calculate_service_charge(order_amount)
        final_amount = order_amount + service_charge

        print("Order Summary:")
        for order in self.orders:
            print(f"{order['quantity']} x {order['item']} - ${order['quantity'] * order['price']:.2f}")

        print(f"\nOrder Amount: ${order_amount:.2f}")
        print(f"Service Charge ({int(self.service_charge_rate * 100)}%): ${service_charge:.2f}")
        print(f"Final Amount: ${final_amount:.2f}")


def main():
    print("Welcome to McDonald's Shell (yumm)")

    mcdonalds_shell = McDonaldsShell()

    while True:
        print("\nMenu:")
        print("1. Order Item")
        print("2. Show Bill")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item: "))
            mcdonalds_shell.place_order(item, quantity, price)
            print(f"{quantity} x {item} added to your order.")

        elif choice == "2":
            mcdonalds_shell.generate_bill()

        elif choice == "3":
            print("That's all folks. Exiting McDonald's Shell. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
