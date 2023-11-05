class NumberStore:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def find_number(self, x):
        try:
            return self.numbers.index(x) + 1  # Indexing starts from 0, hence add 1
        except ValueError:
            return -1  # -1 if x is not found
