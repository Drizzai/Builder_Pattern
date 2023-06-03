class Dish():
    def __init__(self):
        self.parts = []

    def add_part(self, part) -> None:
        self.parts.append(part)

    def dish_info(self) -> None:
        print(f"Składniki: {', '.join(self.parts)}")
