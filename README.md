**A. Struktura systemu lub aplikacji:**

_Director_: Klasa pełniąca rolę kierowania i zarządzająca procesem budowy dania.

_Dish_: Klasa reprezentująca danie i przechowująca jego składniki.

_Builder_: Abstrakcyjna klasa definiująca interfejs dla konkretnych builderów.

_SandwichBuilder, SoupBuilder, DessertBuilder, MainMealBuilder_: Konkretne klasy implementujące interfejs _Builder_ i odpowiedzialne za budowę konkretnych dań.




**B. Scenariusze testów:**

Testy jednostkowe dla klas budowniczych (_BuilderTests_):

Test metody _dish_type()_: Sprawdza, czy metoda _dish_type()_ ustawia właściwe typy dań.

Test metody _dish_part_a()_: Sprawdza, czy metoda _dish_part_a()_ poprawnie ustawia składniki dania.

Test metody _dish_part_b()_: Sprawdza, czy metoda _dish_part_b()_ poprawnie ustawia składniki dania.

Test integracyjny dla klasy Director (_BuilderPatternTestCase_):

- Test metody _build_dish()_: Sprawdza, czy metoda _build_dish()_ poprawnie korzysta z buildera do złożenia dania i wyświetla oczekiwane składniki dania na wyjściu.




**C. Wykorzystane narzędzia i biblioteki:**

_unittest_: Moduł biblioteki standardowej Pythona do tworzenia i uruchamiania testów jednostkowych.

_io.StringIO_: Klasa umożliwiająca tworzenie bufora do przechwytywania i manipulowania danymi wyjściowymi.

_unittest.mock.patch_: Dekorator z modułu unittest.mock, umożliwiający podmianę wartości zależnych od kontekstu, takich jak standardowe wyjście.

_sandwichbuilder_: Moduł zawierający implementację klas związanych z builderem.






**D. Ewentualne problemy i ich rozwiązania:**

Problem: Nieprawidłowe ustawienie typu dania w klasie builder.

Rozwiązanie: Sprawdzić implementację metody _dish_type()_ w każdym konkretnym builderem i upewnić się, że właściwy typ jest ustawiany.


Problem: Niepoprawne ustawienie składników dania w klasach budowniczych.

Rozwiązanie: Sprawdzić implementację metod _dish_part_a()_, _dish_part_b()_, itd. w każdym konkretnym builderze i upewnić się, że składniki są poprawnie dodawane do obiektu Dish.
