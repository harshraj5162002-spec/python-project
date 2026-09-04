class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car is starting")

    @staticmethod
    def stop():
        print("car is stopping")


class toyatacar(car):
    def __init__(self, type, model):
        super().__init__(type)
        self.model = model


car1 = toyatacar("prius", "electric")

print(car1.type)
print(car1.model)

car1.start()
car1.stop()
