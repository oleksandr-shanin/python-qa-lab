from shop import User, Item, buy


item1 = Item('banana', 2)
item2 = Item('apple', 8)
user1 = User('user1', 'pswd')

buy(user1, item1, 5)
buy(user1, item2, 10)

assert user1.cart[item1] == 5, 'Buy test fail'
assert user1.cart.total == 90, 'Total value test fail'
