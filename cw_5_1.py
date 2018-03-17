class Basket():
    def __init__(self, max_size):
        self.max_size = max_size
        self.content = []

    def add(self, obj):
        if len(self.content) < self.max_size:
            self.content.append(obj)
        else:
            self.max_size_warrning()

    def max_size_warrning(self):
        print("Корзина переполнена")


class Packet(Basket):
    def max_size_warning(self):
        print("Пакет переполнен")


class Product():
    def add_to(self, destination):
        destination.add(self)


apple = Product()
phone = Product()
car = Product()
basket = Basket(3)
packet = Packet(2)

apple.add_to(basket)
phone.add_to(basket)
car.add_to(packet)
phone.add_to(packet)
apple.add_to(packet)
