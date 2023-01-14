from unittest import TestCase
from fizz_buzz import FizzBuzz

class TestFizzBuzz(TestCase):
    def test_create_fizz_buzz(self):
        fizz_buzz = FizzBuzz()
        self.assertEqual(fizz_buzz.run(), "0")
    