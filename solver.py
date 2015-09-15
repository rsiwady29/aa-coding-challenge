import uuid, requests, base64
from utilities import vowel_shift, ascii_concatenator, fib
from utilities import consonant_toggler, word_splitter

englishDictionary = ["drool", "cats", "clean", "code", "dogs", "materials",
"needed", "this", "is", "hard", "what", "are", "you", "smoking", "shot", "gun",
"down", "river", "super", "man", "rule", "acklen", "developers", "are", "amazing"]

for i in range(40):
    baseurl = "http://internal-comfybuffalo-1-dev.apphb.com/"
    guid = str(uuid.uuid1())
    r = requests.get(baseurl + "values/" + guid)
    data = r.json()

    data["words"] = [x.encode('ascii') for x in data["words"]]
    startingFib = int(data["startingFibonacciNumber"])

    #1 WordSplitting
    ws = word_splitter.WordSplitter()
    values = ws.splitwords(englishDictionary, data["words"])

    #2 SortValuesAlf
    values = sorted(values, key=str.lower)

    #3 VowelShifting
    vs = vowel_shift.VowelShift()
    values = vs.shiftVowels(values)

    #4 consonant_toggler
    ct = consonant_toggler.ConsonantToggler()
    values = ct.alternateConsonant(values)

    #5 fib
    fibonacci = fib.Fibonacci()
    values = fibonacci.replaceVowelsWithFib(values, startingFib)

    #6 Revese Sort
    values = sorted(values, key=str.lower, reverse=True)

    #7 Ascii Concat
    ac = ascii_concatenator.AsciiConcatenator()
    result = ac.concat(values)

    #8 base64 encode
    encoded = base64.b64encode(result)

    # Send encoded values
    payload = {
        "encodedValue" : encoded,
        "emailAddress" : "rsiwady29@gmail.com",
        "name": "Richard Siwady",
        "webhookUrl": "https://fnatpithih.localtunnel.me", #https://dry-ravine-5943.herokuapp.com/
        "repoUrl": "http://github.com/rsiwady29/aa-coding-challenge/"
    }

    response = requests.post(baseurl + "values/"+ guid, data=payload)
    dataPost = response.json()
    print dataPost
