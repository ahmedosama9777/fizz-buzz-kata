class FizzBuzz():
    def run(self, number: int) -> str:
        if number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"