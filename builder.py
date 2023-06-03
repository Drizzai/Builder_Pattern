from abc import ABC, abstractmethod

class Builder(ABC):
    @abstractmethod
    def dish_type(self) -> None:
        pass

    @abstractmethod
    def dish_part_a(self, part_a) -> None:
        pass

    @abstractmethod
    def dish_part_b(self, part_b) -> None:
        pass
