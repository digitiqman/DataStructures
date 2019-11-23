"""
Semiprime is a number which is the product of two prime numbers
"""

class Semiprime:
    def __init__(self,number):
        self.number = number

    def check(self):
        if type(self.number) != int:
            raise ValueError("Integers Only")
        if self.number == 4:
            return True
        if self.number < 6:
            #only a positive integer could be a semiPrime
            return False
    def isPrime(self, number):
        comp1 = 1
        for r in range(2,number):
            if isinstance(number/r, int):
                return r
        return comp1

    def run(self):
        number = self.number
        if Semiprime(number).check() != None:
            return Semiprime(number).check()
        comp1 = self.isPrime(number)
        # it is a prime
        comp2 = number/comp1
        ccomp2 = self.isPrime(int(comp2))        
        if ccomp2* comp1 == 1:
            return True
        return False
         
