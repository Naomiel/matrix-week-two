class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.present = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.present += 1

        while self.present <= self.n:
            if self.is_prime(self.present):
                return self.present
            self.present += 1

        raise StopIteration()

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True


# n = 20
# prime_iter = PrimeIterator(n)

# for prime in prime_iter:
# print(prime)


def prime_generator(n):
    present = 1
    while present <= n:
        present += 1
        if is_prime(present):
            yield present


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
