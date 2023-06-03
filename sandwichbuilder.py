from builder import Builder
from dish import Dish


class SandwichBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self.dish = Dish()

    def dish(self) -> Dish:
        dish = self.dish
        self.reset()
        return dish

    def dish_type(self) -> None:
        self.dish_type = "Kanapka"
        print(self.dish_type)

    def dish_part_a(self, part_a) -> None:
        self.part_a = part_a
        self.dish.add_part(self.part_a)

    def dish_part_b(self, part_b) -> None:
        self.part_b = part_b
        self.dish.add_part(self.part_b)

    def dish_part_c(self, part_c) -> None:
        self.part_c = part_c
        self.dish.add_part(self.part_c)
