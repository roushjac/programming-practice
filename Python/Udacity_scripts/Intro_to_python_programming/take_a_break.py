import webbrowser
import time

for a in range(3):
    'every 5 seconds, 3 times, open up a link'
    time.sleep(5)
    webbrowser.open('https://www.reddit.com/r/learnprogramming/')
