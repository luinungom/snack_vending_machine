from snack import Snack
from snack_service import SnackService


class VendingMachine:

    def __init__(self):
        self.snackService = SnackService()
        self.products = []

    def vending_machine(self):
        operation_ended: bool = False
        print('*** Welcome to the vending machine ***')
        self.snackService.show_snacks()
        while not operation_ended:
            try:
                operation = self.show_menu()
                operation_ended = self.perform_option(operation)
            except ValueError as e:
                print(f'Invalid option: {e}')

    def show_menu(self):
        print(f'''Please select an option:'
        1. Buy a snack
        2. Show ticket
        3. Add a snack
        4. Show snacks inventory
        5. Exit''')
        return int(input('Please select an option: '))

    def perform_option(self, option: int):
        if option == 1:
            self.buy_snack()
        elif option == 2:
            self.show_ticket()
        elif option == 3:
            self.add_snack()
        elif option == 4:
            self.show_snacks()
        elif option == 5:
            print('Thanks for using the vending machine')
            return True
        else:
            return False

    def buy_snack(self):
        id_snack = int(input('Please enter the id of the snack you want to buy: '))
        snack = next((snack for snack in self.snackService.get_snacks() if snack.id_snack == id_snack), None)
        if snack:
            self.products.append(snack)
            print(f'You have bought the snack {snack.name} for {snack.price}€')
        else:
            print(f'There is no snack with the id {id_snack}')

    def show_ticket(self):
        if not self.products:
            print('There are no products in the ticket')
        else:
            print('Your ticket:')
            total : float = sum(snack.price for snack in self.products)
            for product in self.products:
                print(f'\t{product.name} - {product.price:.2f}€')
            print(f'\tTotal: {total:.2f}€')


    def add_snack(self):
        name = input('Please enter the name of the snack: ')
        price = float(input('Please enter the price of the snack: '))
        snack = Snack(name, price)
        self.snackService.add_snack(snack)
        print(f'The snack {snack.name} has been added to the inventory')

    def show_snacks(self):
        self.snackService.show_snacks()

if __name__ == '__main__':
    vending_machine = VendingMachine()
    vending_machine.vending_machine()
