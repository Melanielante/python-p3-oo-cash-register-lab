#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount  # percentage discount
        self.items = []           # list to keep track of added items
        self.last_transaction = 0  # amount of last transaction for voiding

    def add_item(self, title, price, quantity=1):
        """Add an item with a given price and quantity"""
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        """Apply discount to total and print message if available"""
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the last transaction amount from total"""
        self.total -= self.last_transaction
        self.last_transaction = 0
    pass
