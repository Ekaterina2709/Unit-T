#Задание 1.
#Проект Vehicle. Написать следующие тесты с использованием JUnit5:
#- Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор instanceof).
#- Проверить, что объект Car создается с 4-мя колесами.
#- Проверить, что объект Motorcycle создается с 2-мя колесами.
#- Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
#- Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
#- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
#- Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0).
#В этом проекте, вы будете работать с проектом ""Vehicle"", который представляет собой иерархию классов, включающую абстрактный базовый класс ""Vehicle"" и два его подкласса ""Car"" и ""Motorcycle"".
#Базовый класс ""Vehicle"" содержит абстрактные методы ""testDrive()"" и ""park()"", а также поля ""company"", ""model"", ""yearRelease"", ""numWheels"" и ""speed"".
#Класс ""Car"" расширяет ""Vehicle"" и реализует его абстрактные методы. При создании объекта ""Car"", число колес устанавливается в 4, а скорость в 0. В методе ""testDrive()"" скорость устанавливается на 60, а в методе ""park()"" - обратно в 0.
#Класс ""Motorcycle"" также расширяет ""Vehicle"" и реализует его абстрактные методы. При создании объекта ""Motorcycle"", число колес устанавливается в 2, а скорость в 0. В методе ""testDrive()"" скорость устанавливается на 75, а в методе ""park()"" - обратно в 0.


from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    def __init__(self, company: str,
                 model: str,
                 year_release: int,
                 num_wheels: int,
                 speed: int):
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = num_wheels
        self._speed = speed

    @abstractmethod
    def test_drive(self) -> None:
        pass

    @abstractmethod
    def park(self) -> None:
        pass

    @property
    def company(self):
        return self._company

    @property
    def model(self):
        return self._model

    @property
    def year_release(self):
        return self._year_release

    @property
    def num_wheels(self):
        return self._num_wheels

    @property
    def speed(self):
        return self._speed


class Motorcycle(Vehicle):
    def __init__(self, company: str, model: str, year_release: int):
        super().__init__(company, model, year_release, num_wheels=2, speed=0)

    def test_drive(self) -> None:
        self._speed = 75

    def park(self) -> None:
        self._speed = 0

    def __repr__(self):
        return f'Motorcycle("{self._company}", "{self._model}", {self._year_release})'


class Car(Vehicle):
    def __init__(self, company: str, model: str, year_release: int):
        super().__init__(company, model, year_release, num_wheels=4, speed=0)

    def test_drive(self) -> None:
        self._speed = 60

    def park(self) -> None:
        self._speed = 0

    def __repr__(self):
        return f'Car("{self._company}", "{self._model}", {self._year_release})'
