class AsciiConcatenator:
    def concat(self, wordList):
        result, i = "", 0
        while i < len(wordList):
            delimiter = str(ord(wordList[i-1][0]))
            result += wordList[i] + delimiter
            i+=1
        return result

#Testcases
ac = AsciiConcatenator()
assert ac.concat(["aa", "bb", "cc"]) == "aa99bb97cc98"
