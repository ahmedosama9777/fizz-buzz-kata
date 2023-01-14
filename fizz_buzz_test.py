from unittest import TestCase
from fizz_buzz import FizzBuzz

class TestFizzBuzz(TestCase):
    def setUp(self) -> None:
        self.fizz_buzz = FizzBuzz()
    
    def test_multiples_of_three(self):
        self.assertEqual(self.fizz_buzz.run(3), "Fizz")
    
    def test_multiples_of_five(self):
        self.assertEqual(self.fizz_buzz.run(5), "Buzz")