class Snack:

    total_snacks: int = 0

    def __init__(self, name: str = '', price: float = 0.0):
        Snack.total_snacks += 1
        self.id_snack: int = Snack.total_snacks
        self.name: str = name
        self.price: float = price

    def __str__(self):
        return f'Snack: id {self.id_snack} - Name {self.name} - price: {self.price}'

    def write_snack(self):
        return f'{self.id_snack},{self.name},{self.price}'