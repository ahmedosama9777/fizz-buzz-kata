from fizz_buzz import FizzBuzz

if __name__ == "__main__":
    fizz_buzz = FizzBuzz()

    for i in range(1, 101, 1):
        print(fizz_buzz.run(i))
