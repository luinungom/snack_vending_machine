import os.path

from snack import Snack


class SnackService:
    FILE_NAME = 'snacks.txt'

    def __init__(self):
        self.list_snacks = []
        if os.path.isfile(self.FILE_NAME):
            self.list_snacks = self.get_snacks_in_file()
        else:
            self.load_initial_snacks()

    def load_initial_snacks(self):
        snacks = [
            Snack(name='Chocolate', price=1.50),
            Snack(name='Coke', price=1.00),
            Snack(name='Chips', price=0.50)
        ]
        self.list_snacks.extend(snacks)
        self.save_snacks_in_file(snacks)

    def save_snacks_in_file(self, snacks):
        try:
            with open(self.FILE_NAME, 'a') as file:
                for snack in snacks:
                    file.write(snack.write_snack() + '\n')
        except Exception as e:
            print(f'Error saving snacks in file: {e}')

    def get_snacks_in_file(self):
        snacks = []
        try:
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    id_snack, name, price = line.strip().split(',')
                    snack = Snack(name, float(price))
                    snacks.append(snack)
        except Exception as e:
            print(f'Error reading snacks in file: {e}')
        return snacks

    def add_snack(self, snack):
        self.list_snacks.append(snack)
        self.save_snacks_in_file([snack])

    def show_snacks(self):
        for snack in self.list_snacks:
            print(snack)

    def get_snacks(self):
        return self.list_snacks
