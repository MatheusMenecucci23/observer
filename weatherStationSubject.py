from observer import Observer


class WeatherStationSubject:

    def attach(self, observer: Observer) -> None:
        raise NotImplementedError

    def detach(self, observer: Observer) -> None:
        raise NotImplementedError

    def notify(self, temperatura: float) -> None:
        raise NotImplementedError

