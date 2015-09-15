class WordSplitter:
    ## Naive Approach
    def splitwords(self, englishWordList, wordList):
        newList = []
        for word in wordList:
            i = 1
            curWord = word[0]
            while i < len(word):
                if (curWord.lower() in englishWordList):
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
    englishDictionary = ["drool", "cats", "clean", "code", "dogs", "materials",
    "needed", "this", "is", "hard", "what", "are", "you", "smoking", "shot", "gun",
    "down", "river", "super", "man", "rule", "acklen", "developers", "are", "amazing"]
    assert ws.splitwords(englishDictionary, ['materiAlsriver', "dogsare"]) == ["materiAls", "river", "dogs", "are"]
