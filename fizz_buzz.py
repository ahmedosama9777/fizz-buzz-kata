class FizzBuzz:
    def run(self, number: int) -> str:
        self._validate_input(number)

        result: str = ""

        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        if result == "":
            result += str(number)

        return result

    def _validate_input(self, number: int):
        if number < 1:
            raise ValueError("Number must be greater than 0")
        elif number > 100:
            raise ValueError("Number must be less than 100")
