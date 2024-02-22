from unittest import TestCase
from main import sum_file

class Test(TestCase):
    def test_sum(self):
        # Given
        file = "test_sum_input.txt"
        expected = 3
        # When
        result = sum_file(file)
        # Then
        self.assertEqual(expected, result)

    def test_sum_wrong_range(self):
        # Given
        file = "test_sum_wrong_range_input.txt"
        # When
        with self.assertRaises(ValueError) as cm:
        # Then
            sum_file(file)
            self.assertEqual("Liczba musi być w przedziale od [-10; 10]", cm.exception)

    def test_sum_text_given(self):
        # Given
        file = "test_sum_text_given_input.txt"
        # When
        with self.assertRaises(TypeError):
            # Then
            sum_file(file)

    def test_sum_pusty_plik(self):
        # Given
        file = "test_sum_pusty_plik.txt"
        expected = 0
        # When
        result = sum_file(file)
        # Then
        self.assertEqual(expected, result)

    def test_sum_plik_nie_istnieje(self):
        # Given
        file = "test_sum_plik_nie_istnieje_input.txt"
        expected = 0
        # When
        with self.assertRaises(FileNotFoundError):
            # Then
            sum_file(file)