"""A function that selects quotes randomly"""

from quotes import funny_quotes
import random


def display_random_quote():
    quotes = funny_quotes()
    nr_of_quotes = len(quotes)
    selected_quote = quotes[random.randint(0, nr_of_quotes)]
    return selected_quote


# quote = display_random_quote()
# print(quote)

"""A function that selects all quotes"""


def all_quotes():
    quotes = funny_quotes()
    nr_of_quotes = len(quotes)
    counter = 0
    for quote in quotes:
        if counter <= nr_of_quotes:
            print(quote)
            counter += 1


# all_quotes()

quotes = funny_quotes()
for quote in quotes:
    print(quote)

