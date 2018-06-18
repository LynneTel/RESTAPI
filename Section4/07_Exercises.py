# exercise 1
# class Store:
#     def __init__(self, name):
#         # You'll need 'name' as an argument to this method.
#         # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
#         self.name = name
#         self.items = []
#
#
#     def add_item(self, name, price):
#         # Create a dictionary with keys name and price, and append that to self.items.
#         self.items.append({'name':name, 'price':price})
#
#
#     def stock_price(self):
#         # Add together all item prices in self.items and return the total.
#         total = 0
#         for item in self.items:
#             total += item['price']
#         return total
#
#
# mystore = Store('JCPenny')
# print(mystore.name)
# mystore.add_item("tshirt", 9.99)
# print(mystore.items)
# mystore.add_item("tomato", .99)
# print(mystore.items)
# print(mystore.stock_price())


class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        self.items.append({'name':name, 'price':price})

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))


mystore = Store('Test')
mystore.add_item("Keyboard", 160)
mystore2 = Store('Amazon')
print(Store.franchise(mystore))
print(Store.franchise(mystore2))

print(Store.store_details(mystore))
print(Store.store_details(mystore2))
