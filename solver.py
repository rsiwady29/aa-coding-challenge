import uuid, requests, base64
from utilities import vowel_shift, ascii_concatenator, fib
from utilities import consonant_toggler, word_splitter

for i in range(20):
    baseurl = "http://internal-comfybuffalo-1-dev.apphb.com/"
    guid = str(uuid.uuid1())
    r = requests.get(baseurl + "values/" + guid)
    data = r.json()

    data["words"] = [x.encode('ascii') for x in data["words"]]
    startingFib = int(data["startingFibonacciNumber"])

    # WordSplitting
    ws = word_splitter.WordSplitter()
    

    #SortValuesAlf
    values = sorted(data["words"], key=str.lower)

    #VowelShifting
    vs = vowel_shift.VowelShift()
    values = vs.shiftVowels(values)

    #consonant_toggler
    ct = consonant_toggler.ConsonantToggler()
    values = ct.alternateConsonant(values)

    #fib
    fibonacci = fib.Fibonacci()
    values = fibonacci.replaceVowelsWithFib(values, startingFib)

    #Revese Sort
    values = sorted(values, key=str.lower, reverse=True)

    #Ascii Concat
    ac = ascii_concatenator.AsciiConcatenator()
    result = ac.concat(values)

    encoded = base64.b64encode(result)

    # Send encoded values
    payload = {
        "encodedValue" : result,
        "emailAddress" : "rsiwady29@gmail.com",
        "name": "Richard Siwady",
        "webhookUrl": "https://dry-ravine-5943.herokuapp.com/",
        "repoUrl": "http://github.com/rsiwady29/aa-coding-challenge/"
    }

    response = requests.post(baseurl + "values/"+ guid, data=payload)
    dataPost = r.json()
    print dataPost["status"]
    print dataPost["message"]
