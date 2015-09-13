class ConsonantToggler:
    def alternateConsonant(self, wordList):
        vowels = "aeiou"
        newList = []
        isCaps = wordList[0][0].isupper()
        for word in wordList:
            l = list(word)
            newS = ""
            for char in l:
                if char.lower() not in vowels:
                    newS += char.upper() if isCaps else char.lower()
                    isCaps = not isCaps
                else:
                    newS += char
            newList += [newS]
        return newList

#Testcases
ct = ConsonantToggler()
assert ct.alternateConsonant(["abcd","edf"]) == ['abCd', 'eDf']
assert ct.alternateConsonant(["Abcd","edf"]) == ['ABcD', 'edF']
