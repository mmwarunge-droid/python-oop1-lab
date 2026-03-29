#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        # Store the book title directly
        self.title = title

        # Initialize a private variable for page_count
        self._page_count = None

        # Use the setter to assign page_count (ensures validation runs)
        self.page_count = page_count

    # Getter method for page_count
    @property
    def page_count(self):
        return self._page_count

    # Setter method for page_count with validation
    @page_count.setter
    def page_count(self, value):
        # Check if the value is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            # Print error message if invalid
            print("page_count must be an integer")

    # Method to simulate turning a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        