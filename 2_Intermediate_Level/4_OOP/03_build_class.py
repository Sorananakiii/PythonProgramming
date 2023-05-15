class Item:

    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity=0):
        print(f'An instance created : {name}')
        assert (price >= 0), f'Price {price} is not greater than zero'
        assert (quantity >= 0), f'Quantity {quantity} is not greater than zero'
        # this line will replace external command to create self object
        self.name = name
        # So, we can create whatever self object we wanted.
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    # use Class attribute instead of external valuable
    # def calculate_total_price(self, x, y):
    #     return x*y
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# print(Item.pay_rate)
# print(Item.__dict__)

item1 = Item('Phone', 100, 5)
item2 = Item('Laptop', 10000, 3)
# item1.apply_discount()
# print(item1.price)

print(Item.all)
