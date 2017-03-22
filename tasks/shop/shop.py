from collections import defaultdict
from hashlib import sha256


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.name == other.name

    def __hash__(self):
        return hash((self.name, self.price))


class Cart(defaultdict):
    def __init__(self, *args):
        super().__init__(int)  # call parent class method
    # def __init__(self):
    #     self.items = defaultdict(int)  # int() == 0

    # def __getitem__(self, item):
    #     return self.items[item]

    # def __setitem__(self, item, qt):
    #     self.items[item] = qt

    @property
    def total(self):
        # return sum([item.price * self.items[item] for item in self.items])
        return sum(item.price * qt for item, qt in self.items())


class User:
    def __init__(self, login, password):
        self.login = login
        # self._password_hash = sha256(password.encode()).hexdigest()
        self.password = password  # MIGHTY SETTER!!!
        self.cart = Cart()

    @property
    def password(self):
        raise AttributeError('No password is stored, look for ._password_hash')
        # return self._password_hash

    @password.setter
    def password(self, text):
        if len(text) < 6:
            raise ValueError('Password has to be longer than 5 characters')
        self._password_hash = sha256(text.encode()).hexdigest()

    def check_pass(self, password):
        return self._password_hash == sha256(password.encode()).hexdigest()

    def buy(self, store, item, qt=1):
        if store[item] >= qt:
            self.cart[item] += qt
            store[item] -= qt
        else:
            raise ValueError('Nuf nuf minerals!')

    # def change_pass(self, old_pass, new_pass):
    #     if check_pass


class Store(defaultdict):
    def __init__(self, *args):
        super().__init__(int)


if __name__ == '__main__':
    store1 = Store()

    store1[Item('apple', 2)] = 2
    store1[Item('banana', 5)] = 7

    a = User('login', 'password')
    apple = Item('apple', 2)
    a.buy(store1, apple, 2)


# Task:
# get user.password -> Exception('pwd is not stored')
# set user.password = 'qwerty' -> pwd hash is saved in _pwd_hash
