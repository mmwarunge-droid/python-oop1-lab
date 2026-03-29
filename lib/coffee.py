#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Initialize private variable for size
        # (validation handled via setter)
        self._size = None

        # Use setter to assign size (ensures validation)
        self.size = size

        # Store price directly (no validation required per spec)
        self.price = price

    # Getter method for size
    @property
    def size(self):
        return self._size

    # Setter method for size with validation
    @size.setter
    def size(self, value):
        # Only allow specific size options
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            # Print error message if invalid
            print("size must be Small, Medium, or Large")

    # Method to simulate tipping for the coffee
    def tip(self):
        # Print appreciation message
        print("This coffee is great, here’s a tip!")

        # Increase price by 1 (simulates adding a tip)
        self.price += 1