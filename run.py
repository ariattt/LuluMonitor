from bs4 import BeautifulSoup
import requests
import lxml
import json
from datetime import datetime
import time
import random
import sys

def check():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    response = requests.get(
        'https://www.lulus.com/products/captain-s-blog-tan-double-breasted-coat/579232.html',
        headers=headers).text

    soup = BeautifulSoup(response, 'lxml')

    data = []

    for container in soup.findAll(text='S'):
        cur_size = container.find_parent('div')
        if 'out-of-stock' in str(cur_size):
            now = datetime.now()
            current_time = now.strftime("%-I:%M %p")
            print(current_time + ': Out of Stock')
        else:
            msg = BeautifulSoup(str(cur_size.find_parent()), features="lxml").prettify()
            print(msg)
            url = sys.argv[1]
            requests.get( url )

def spinning_cursor():
    frames = [
            "⢀⠀",
            "⡀⠀",
            "⠄⠀",
            "⢂⠀",
            "⡂⠀",
            "⠅⠀",
            "⢃⠀",
            "⡃⠀",
            "⠍⠀",
            "⢋⠀",
            "⡋⠀",
            "⠍⠁",
            "⢋⠁",
            "⡋⠁",
            "⠍⠉",
            "⠋⠉",
            "⠋⠉",
            "⠉⠙",
            "⠉⠙",
            "⠉⠩",
            "⠈⢙",
            "⠈⡙",
            "⢈⠩",
            "⡀⢙",
            "⠄⡙",
            "⢂⠩",
            "⡂⢘",
            "⠅⡘",
            "⢃⠨",
            "⡃⢐",
            "⠍⡐",
            "⢋⠠",
            "⡋⢀",
            "⠍⡁",
            "⢋⠁",
            "⡋⠁",
            "⠍⠉",
            "⠋⠉",
            "⠋⠉",
            "⠉⠙",
            "⠉⠙",
            "⠉⠩",
            "⠈⢙",
            "⠈⡙",
            "⠈⠩",
            "⠀⢙",
            "⠀⡙",
            "⠀⠩",
            "⠀⢘",
            "⠀⡘",
            "⠀⠨",
            "⠀⢐",
            "⠀⡐",
            "⠀⠠",
            "⠀⢀",
            "⠀⡀"
        ]
    while True:
        for cursor in frames:
            yield cursor

def spin( how_long ):
    # how_long in 0.1 seconds
    spinner = spinning_cursor()
    for _ in range( how_long ):
        tar = next(spinner)
        msg = tar
        sys.stdout.write( msg )
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b' * (len(msg)))

starttime = time.time()
while True:
    check()
    minute = 5
    spin(10 * (minute * 60 + random.randrange(60))) # unit is second




