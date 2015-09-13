class WordSplitter:
    ## Naive Approach
    def splitwords(self, englishWordList, wordList):
        newList = []
        for word in wordList:
            i = 1
            curWord = word[0]
            while i < len(word):
                if (curWord in englishWordList):
                    newList += [curWord]
                    curWord = ""
                elif i == len(word) -1:
                    curWord += word[i]
                    newList += [curWord]
                curWord += word[i]
                i += 1
        return newList

#Testcases
if __name__ == '__main__':
    ws = WordSplitter()
    assert ws.splitwords(["a", "cat","cats", "two", "dogs"], ['acat', "twodogs"]  ) == ["a", "cat", "two", "dogs"]
