# from random import randint
class NotEnoughMoneyError(Exception):
    pass


class NegativeAmountError(ValueError):
    pass


class Account():
    """docstring for Account"""
    base_commission = 2

    def __init__(self, amount, overdraft_allowed=False):
        self.balance = 100 * amount  # amount in dollars, balance in cents
        self. overdraft_allowed = overdraft_allowed

    def __repr__(self):
        '''valid object constructor, str(object) by default'''
        return 'Account(amount={}, overdraft_allowed={})'.format(self.balance // 100, self.overdraft_allowed)

    def __str__(self):
        if self.overdraft_allowed:
            return 'Account with {} money units, overdraft allowed'.format(self.balance / 100)
        else:
            return 'Account with {} money units, overdraft not allowed'.format(self.balance / 100)

    def credit(self, amount, commission=base_commission):
        # commission in percents
        if amount > 0:
            self.balance += int(amount * (100 - commission))  # + randint(0, 1)
            return self.balance / 100
        else:
            raise NegativeAmountError('Negative amount is not allowed')

    def debit(self, amount, commission=base_commission):
        # commission in percents
        if amount < 0:
            raise NegativeAmountError('Negative amount is not allowed')
        if self.balance >= amount * 100:
            self.balance -= int(amount * (100 + commission))  # + randint(0, 1)
            return self.balance / 100
        elif self.overdraft_allowed:
            self.balance -= int(amount * (100 + commission * 2))  # + randint(0, 1)
            return self.balance / 100
        else:
            raise NotEnoughMoneyError('Not enough money')

    def transfer(self, target, amount, source_commission=True, target_commission=False):
        if not isinstance(target, Account):
            raise TypeError('{} is not an instance of Account'.format(target))
        try:
            if source_commission and target_commission:
                self.debit(amount, self.base_commission)
                target.credit(amount, self.base_commission)
            elif source_commission:
                self.debit(amount, 2 * self.base_commission)
                target.credit(amount, 0)
            else:
                self.debit(amount, 0)
                target.credit(amount, 2 * self.base_commission)
            print('Transfered successfully')
        except Exception:
            print('Transer failed')
            raise


if __name__ == '__main__':
    a = Account(200, True)
    a.credit(50)
    assert a.balance == 24900, 'Credit test fail'
    a = Account(200, True)
    a.debit(50)
    assert a.balance == 14900, 'Debit test fail'
    a = Account(50, True)
    a.debit(100)
    assert a.balance == -5400, 'Debit overdraft test fail'
    a = Account(200, True)
    b = Account(100)
    a.transfer(b, 100)
    assert a.balance == 9600, 'Default transfer source test fail'
    assert b.balance == 20000, 'Default transfer target test fail'
    a = Account(200, True)
    b = Account(100)
    a.transfer(b, 100, False, True)
    assert a.balance == 10000, 'Target pays commission transfer source test fail'
    assert b.balance == 19600, 'Target pays commission transfer target test fail'
    a = Account(200, True)
    b = Account(100)
    a.transfer(b, 100, True, True)
    assert a.balance == 9800, 'Target pays commission transfer source test fail'
    assert b.balance == 19800, 'Target pays commission transfer target test fail'
    a = Account(200, True)
    b = Account(100)
    try:
        b.transfer(a, 150)
    except NotEnoughMoneyError:
        pass
    else:
        raise AssertionError('Overdraft not allowed test fail')
    a = Account(200, True)
    b = Account(100)
    try:
        b.transfer(a, -150)
    except NegativeAmountError:
        pass
    else:
        raise AssertionError('Negative amount not allowed test fail')

# Home task:
# 1. transfer with commission
# 2. overdraft
# https://pypi.python.org/pypi/money/
