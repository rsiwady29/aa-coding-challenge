class VowelShift:
    def shiftVowels(self,words):
        vowels = "aeiou"
        newListOfWords = []
        for word in words:
            l = list(word)
            i = 0
            while i < len(l):
                if l[i].lower() in vowels:
                    if i == len(l)-1:
                        value = l[i]
                        del l[i]
                        l = [value] + l
                    else:
                        tmp = l[i+1]
                        l[i+1], l[i] = l[i], tmp
                    i += 1
                i += 1
            newListOfWords += ["".join(l)]
        return newListOfWords

#Testcases
vs = VowelShift()
assert vs.shiftVowels([]) == []
assert vs.shiftVowels(["abc", "bca", "aa", "hello"]) == ["bac", "abc", "aa", "ohlel"]
