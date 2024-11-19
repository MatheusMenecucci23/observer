from observer import Observer


class ConcreteObserverModulo2(Observer):
    def __init__(self):
        self._temperature_readings = []

    def update(self, temperature: float):
        self._temperature_readings.append(temperature)
        average_temp = sum(self._temperature_readings) / len(self._temperature_readings)
        print(f"Estatísticas: Temperatura média até agora é {average_temp:.2f}°C")
