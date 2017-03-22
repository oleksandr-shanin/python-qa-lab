import unittest
from shop import User, Item, Cart, Store
from random import randint
from hashlib import sha256


class TestUser(unittest.TestCase):
    def setUp(self):  # executed BEFORE each and every test in TestCase
        self.banana = Item('banana', 2)
        self.apple = Item('apple', 8)
        self.store1 = Store()
        self.store1[self.banana] = 10
        self.store1[self.apple] = 7
        self.user = User('username', 'qwerty')

    def tearDown(self):  # executed AFTER each and every test in TestCase
        pass

    def test_create(self):
        # user = User('username', 'qwerty')
        self.assertEqual(self.user.login, 'username')
        self.assertEqual(self.user._password_hash, sha256('qwerty'.encode()).hexdigest())

    def test_short_password(self):
        with self.assertRaises(ValueError):
            self.user.password = 'qwert'

    def test_empty_cart(self):
        # user = User('username', 'qwerty')
        self.assertEqual(len(self.user.cart), 0)

    def test_default_buy(self):
        self.user.buy(self.store1, self.banana)
        self.assertEqual(self.user.cart[self.banana], 1)
        self.assertEqual(self.store1[self.banana], 9)

    def test_buy_enough(self):
        self.user.buy(self.store1, self.apple, 5)
        self.assertEqual(self.user.cart[self.apple], 5)
        self.assertEqual(self.store1[self.apple], 2)

    def test_buy_not_enough(self):
        with self.assertRaises(ValueError):
            self.user.buy(self.store1, self.banana, 15)


class TestItem(unittest.TestCase):
    def test_create(self):
        price = randint(0, 10000)
        item = Item('item_name', price)
        self.assertEqual(item.name, 'item_name')
        self.assertEqual(item.price, price)

    def test_equality(self):
        price = randint(0, 10000)
        item1 = Item('item_name', price)
        item2 = Item('item_name', price)
        self.assertEqual(item1, item2)


class TestCart(unittest.TestCase):
    def setUp(self):  # executed BEFORE each and every test in TestCase
        self.banana = Item('banana', 2)
        self.apple = Item('apple', 8)
        self.store1 = Store()
        self.store1[self.banana] = 10
        self.store1[self.apple] = 7
        self.user = User('username', 'qwerty')

    def test_total(self):
        self.user.buy(self.store1, self.banana)
        self.user.buy(self.store1, self.apple, 5)
        self.assertEqual(self.user.cart.total, 42)


if __name__ == '__main__':
    unittest.main(verbosity=2)

# HOME_TASK:
# testcases for shop
