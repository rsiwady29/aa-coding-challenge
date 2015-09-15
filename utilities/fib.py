class Fibonacci:
    def fib(self, n):
        f1,f2 = 0, 1
        n = int(n)
        if n == 0: return (0,1)
        while f2 != n:
            f1, f2 = f2, f1+f2
            if f2 > n: raise Exception("%d is not part of the fib seq" % f2)
        return (f1, f2)

    def replaceVowelsWithFib(self, wordList, startingFib):
        vowels = "aeiouy"
        newList = []
        f1, f2 = self.fib(startingFib)
        for word in wordList:
            l = list(word)
            newS = ""
            for char in l:
                if char.lower() in vowels:
                    newS += str(f2)
                    f1, f2 = f2, f1+f2
                else:
                    newS += char
            newList += [newS]
        return newList

# Testcases
if __name__ == '__main__':
    fib = Fibonacci()

    #fib
    assert fib.fib(0) == (0,1)
    assert fib.fib(6765) == (4181,6765)
    assert fib.fib(144) == (89,144)
    #replaceVowelsWithFib
    assert fib.replaceVowelsWithFib( ["aa", "ba", "cc"] , 1597 ) == ['15972584', 'b4181', 'cc']
