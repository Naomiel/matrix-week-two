class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1

        while self.current <= self.n:
            if self.is_prime(self.current):
                return self.current
            self.current += 1

        raise StopIteration()

    def is_prime(self, num):
        if num < 2:
            return False

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False

        return True


#n = 20
#prime_iterator = PrimeIterator(n)

#for prime in prime_iterator:
    #print(prime)



def prime_generator(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True
