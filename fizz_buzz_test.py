from unittest import TestCase
from fizz_buzz import FizzBuzz

class TestFizzBuzz(TestCase):
    def setUp(self) -> None:
        self.fizz_buzz = FizzBuzz()
    
    def test_multiples_of_three(self):
        self.assertEqual(self.fizz_buzz.run(3), "Fizz")
    
    def test_multiples_of_five(self):
        self.assertEqual(self.fizz_buzz.run(5), "Buzz")
    
    def test_multiple_of_five_and_three(self):
        self.assertEqual(self.fizz_buzz.run(45), "FizzBuzz")
    
    def test_neither_multiple_of_three_nor_five(self):
        self.assertEqual(self.fizz_buzz.run(1), "1")
    
    def test_input_less_than_range(self):
        with self.assertRaises(ValueError):
            self.fizz_buzz.run(0)
