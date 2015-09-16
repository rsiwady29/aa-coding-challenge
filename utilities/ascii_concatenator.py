class AsciiConcatenator:
    def concat(self, wordList):
        return "".join([ word + str(ord(wordList[i-1][0])) for i, word in enumerate(wordList) ])
        """result, i = "", 0
        while i < len(wordList):
            delimiter = str(ord(wordList[i-1][0]))
            result += wordList[i] + delimiter
            i+=1
        return result"""

#Testcases
if __name__ == '__main__':
    ac = AsciiConcatenator()
    assert ac.concat(["aa", "bb", "cc"]) == "aa99bb97cc98"
    assert ac.concat(["dog", "cat", "bird"]) == "dog98cat100bird99"
