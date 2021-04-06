from abc import ABC, abstractmethod

from survivor import Survivor


class Medicine(ABC):
    @abstractmethod
    def __init__(self, health_increase):
        if health_increase < 0:
            raise ValueError("Health increase cannot be less than zero.")
        self.__health_increase = health_increase

    def apply(self, survivor: Survivor):
        survivor.health += self.__health_increase

