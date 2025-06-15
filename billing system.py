import datetime

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class BillingSystem:
    def __init__(self):
        self.items = []
        self.tax_rate = 0.05  # 5% GST

    def add_item(self, name, price, quantity):
        item = Item(name, price, quantity)
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.total() for item in self.items)

    def calculate_tax(self, subtotal):
        return subtotal * self.tax_rate

    def calculate_total(self, subtotal, tax):
        return subtotal + tax

    def generate_bill(self):
        print("\n" + "="*40)
        print("           XYZ Store Billing System")
        print("        Date:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("="*40)
        print("{:<20} {:<8} {:<8} {:<8}".format("Item", "Price", "Qty", "Total"))
        print("-"*40)

        for item in self.items:
            print("{:<20} {:<8.2f} {:<8} {:<8.2f}".format(
                item.name, item.price, item.quantity, item.total()))

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        total = self.calculate_total(subtotal, tax)

        print("-"*40)
        print("{:<20} {:>18.2f}".format("Subtotal", subtotal))
        print("{:<20} {:>18.2f}".format("GST (5%)", tax))
        print("{:<20} {:>18.2f}".format("Total", total))
        print("="*40)
        print("       Thank you for shopping with us!")
        print("="*40)


def main():
    system = BillingSystem()
    print("Welcome to XYZ Store Billing System")

    while True:
        name = input("Enter item name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            price = float(input("Enter item price (in ₹): "))
            quantity = int(input("Enter item quantity: "))
            system.add_item(name, price, quantity)
        except ValueError:
            print("Invalid input. Please try again.")

    if system.items:
        system.generate_bill()
    else:
        print("No items were added. Exiting...")


if __name__ == "__main__":
    main()
