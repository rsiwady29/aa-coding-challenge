class utilities:
    def fib(self, n):
        f1,f2 = 0, 1
        n = int(n)
        if n == 0: return (0,1)
        while f2 != n:
            f1, f2 = f2, f1+f2
            if f2 > n: raise Exception("%d is not part of the fib seq" % f2)
        return (f1, f2)

    
# Testcases
utility = utilities()

#Fib
assert utility.fib(0) == (0,1)
assert utility.fib(6765) == (4181,6765)
assert utility.fib(144) == (89,144)
