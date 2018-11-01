import urllib.request
import urllib.parse

def read_text():
    quotes = open("./Class 8/movie_quotes.txt", "r")

    content_of_file = []
    with quotes as f:
        for line in f:
            content_of_file.append(line.replace("\n", ""))

    quotes.close()

    for content in content_of_file:
        check_profanity(content)

def check_profanity(text_to_check):
    parameter = urllib.parse.quote(text_to_check)
    request = urllib.request.Request('http://www.wdylike.appspot.com/?q=' + parameter)
    result = urllib.request.urlopen(request)
    resulttext = result.read()

    print("[" + text_to_check + "] result: " + str(resulttext))

    result.close()

read_text()