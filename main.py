from director import Director
from sandwichbuilder import SandwichBuilder
from soupbuilder import SoupBuilder
from mainmealbuilder import MainMealBuilder
from desertbuilder import DesertBuilder

director = Director()

builder = SoupBuilder()
director.builder = builder

builder.dish_part_a("Woda")
builder.dish_part_b("Makaron")
builder.dish_part_c("Przecier pomidorowy")
builder.dish_part_d("Kostka rosołowa")
director.build_dish()

print("________________________________________________________________")

builder = MainMealBuilder()
director.builder = builder

builder.dish_part_a("Kotlet schabowy")
builder.dish_part_b("Frytki")
builder.dish_part_c("Surówka")
director.build_dish()

print("________________________________________________________________")

builder = SandwichBuilder()
director.builder = builder

builder.dish_part_a("Bułka pszenna")
builder.dish_part_b("Szynka")
builder.dish_part_c("Pomidor")
director.build_dish()

print("________________________________________________________________")

builder = DessertBuilder()
director.builder = builder

builder.dish_part_a("Lody")
builder.dish_part_b("Pistacjowe")
builder.dish_part_b("Polewa czekoladowa")
director.build_dish()
