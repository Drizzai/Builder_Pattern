import unittest
from io import StringIO
from unittest.mock import patch
from sandwichbuilder import SandwichBuilder
from director import Director


class BuilderTests(unittest.TestCase):
    def test_dish_type(self):
        builder = SandwichBuilder()
        builder.dish_type()
        self.assertEqual(builder.dish_type, "Kanapka")

    def test_dish_part_a(self):
        builder = SandwichBuilder()
        builder.dish_part_a("Part A")
        self.assertEqual(builder.part_a, "Part A")

    def test_dish_part_b(self):
        builder = SandwichBuilder()
        builder.dish_part_b("Part B")
        self.assertEqual(builder.part_b, "Part B")


class BuilderPatternTestCase(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_build_dish(self, mock_stdout):
        expected_output = "Składniki: Bułka pszenna, Szynka, Pomidor\n"

        director = Director()
        builder = SandwichBuilder()
        director.builder = builder

        builder.dish_part_a("Bułka pszenna")
        builder.dish_part_b("Szynka")
        builder.dish_part_c("Pomidor")
        director.build_dish()

        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
