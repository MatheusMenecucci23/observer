from observer import Observer


class ConcreteObserverModulo1(Observer):
    def update(self, temperatura: float) -> None:
        print("Essa é a temperatura atual", temperatura)