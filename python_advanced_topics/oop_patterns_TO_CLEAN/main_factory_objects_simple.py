"""
Python Beyond The Basics: The Factory Pattern: SIMPLE
"""

import re

class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    @classmethod
    def from_pennies(cls, num_pennies):
        print('from_pennies(cls, num_pennies): -->')
        dollars, cents = divmod(num_pennies, 100)
        return cls(dollars, cents)

    @classmethod
    def from_string(cls, amount):
        match = re.search(r'^\$(?P<dollars>\d+)\.(?P<cents>\d\d)$', amount)
        assert match is not None, 'Invalid amount: {}'.format(amount)
        dollars = int(match.group('dollars'))
        cents = int(match.group('cents'))
        return cls(dollars, cents)

    def print(self):
        print(f'dollars={self.dollars}')
        print(f'cents={self.cents}')
        print(self.__class__.__name__)


if __name__ == '__main__':
    print('Start factory here - SIMPLE FACTORY')
    a_wallet_01 = Money(12, 10)
    a_wallet_01.print()
    a_wallet_02 = Money.from_pennies(105)
    a_wallet_02.print()
    a_wallet_03 = Money.from_string('$12.50')
    a_wallet_03.print()
