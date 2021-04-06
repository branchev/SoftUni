from abc import ABC, abstractmethod

from survivor import Survivor


class Supply(ABC):
    @abstractmethod
    def __init__(self, needs_increase):
        if needs_increase < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self.__needs_increase = needs_increase

    def apply(self, survivor: Survivor):
        survivor.needs += self.__needs_increase
