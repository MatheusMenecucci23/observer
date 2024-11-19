from random import randrange

from observer import Observer
from weatherStationSubject import WeatherStationSubject


class WeatherStationConcreteSubject(WeatherStationSubject):

    def __init__(self):
        self._observers = []
        self._temperature = 0.0  # Temperatura inicial

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperatura(self, temperatura: float) -> None:
        print(
         "\nSubject: Setando a temperatura."
        )
        self._temperature = temperatura

        print(f"Subject: My temperature has just changed to: {self._temperature}")
        self.notify()



