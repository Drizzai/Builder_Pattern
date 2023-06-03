from builder import Builder


class Director:
    def __init__(self) -> None:
        self.builder = None

    def builder(self, builder: Builder):
        self.builder = builder

    def build_dish(self):
        self.builder.dish_type()
        self.builder.dish.dish_info()
