class FizzBuzz():
    def run(self, number: int) -> str:
        result: str = ""

        if number % 3 == 0:
            result += "Fizz"
        if number % 5 == 0:
            result += "Buzz"
        if result == "":
            result += str(number)
        
        return result