class FizzBuzz:

    def game(self, i):
        if isinstance(i, str):
            return ValueError
        elif i % 3 == 0 and i % 5 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0:
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'
        else:
            return ':('


tmp = FizzBuzz()
