import time
import webbrowser

turns = 3
turn = 0

print("Started at: " + time.ctime())
while turn < turns:
    time.sleep(5)
    webbrowser.open("https://soundcloud.com/guigo-vedovato/funky-de-la-cabrera")
    turn += 1