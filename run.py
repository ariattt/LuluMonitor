from bs4 import BeautifulSoup
import requests
import lxml
import json
from datetime import datetime
import time
import random
import sys

def alert():
    url = sys.argv[1]
    requests.get( url )

def check():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        'referer':'https://www.google.com/',
        # "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        # "cookie": "wtid=q1u8d4ngigb9klhfkj5pq3e50q256jh7qea271cjf6r13k8mc0h0; _csrf=YAehfrkLJuP-n5TM33tXFned; dtm_tracker=1; _ga=GA1.2.657120786.1632786711; _lu_ga=GA1.2.657120786.1632786711; _fbp=fb.1.1632786710951.7567454833; l_ab_nav_content=1; l_ab_deferred_tags=2; l_ab_quickview_mini=1; l_ab_newrelic=2; l_ab_rewards_test=2; l_ab_fit_analytics=1; flag_enable_sitenav_v2=bSKZZ5EOVFVg2IzJL9o1VAoEkM5tID; flag_enable_adobe_deferred=false; flag_quickview_mini=8M7Es2gegHytbidYIdvni2FZREcqN0; flag_enable_browser_newrelic=false; flag_fit_analytics=8p9PmRA9kpf9D4yqj4zsyJY5eWN0Eg; img=dpr_2.0; at_check=true; _px_uAB=MTIzMTM0fHRydWU=; AMCVS_452A1F2F5755B30D7F000101%40AdobeOrg=1; AMCV_452A1F2F5755B30D7F000101%40AdobeOrg=-1124106680%7CMCIDTS%7C18898%7CMCMID%7C29825248056474602713813806217990996866%7CMCAAMLH-1633391512%7C9%7CMCAAMB-1633391512%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1632793912s%7CNONE%7CvVersion%7C5.2.0; pxcts=e3336830-1fed-11ec-8f00-2fcc35ac5f10; _pxvid=e3332766-1fed-11ec-b9f2-4e4e73474f66; wtid_p=4uv1ie-RMOwK7ROSz-b77dd0ed394e3f089af4a979b; _evga_19ff=95e7453bdb3eba27.; _gcl_au=1.1.415273759.1632786712; gpv_pn=Lulus%3AProduct%3AFull%3A579232%3ACaptain%27s%20Blog%20Tan%20Double-Breasted%20Coat; s_cc=true; _scid=6462fd14-cf1e-4675-934c-402a41b39284; _gid=GA1.2.1591521363.1632786713; fita.sid.lulus=QZidBv1w-U9rfr4NdUQthW6JB0PbLvRD; _sctr=1|1632726000000; _px_f394gi7Fvmc43dfg_user_id=ZTQ0OWJhMzAtMWZlZC0xMWVjLWE4ZWMtNDczOTU0NWY0Y2U3; _li_dcdm_c=.lulus.com; _lc2_fpi=e6f4dbd32c5a--01fgmtr3r9gpx986pejq9skkn7; ku1-sid=mrM5rbOSzUIAkIvVhD-g6; ku1-vid=fec10830-9725-9d5e-148f-75d0e9a7d9da; _pin_unauth=dWlkPVl6TTFZMk0yWlRRdE5EazJOeTAwTXpnMUxXRm1aREF0TjJWak0yWmpNVFE0WXpnMQ; mbox=session#02388c97078d4ec2b40506ad31605b0f#1632788682|PC#02388c97078d4ec2b40506ad31605b0f.35_0#1696031622; lulusdevinfo=%7B%22browserWidth%22%3A997%2C%22browserHeight%22%3A971%2C%22screenHeight%22%3A1050%2C%22screenWidth%22%3A1680%2C%22browserTimeOffset%22%3A-420%2C%22colorDepth%22%3A30%2C%22language%22%3A%22en-US%22%2C%22pluginDescriptions%22%3A%5B%22Portable%20Document%20Format%22%2C%22%22%2C%22%22%5D%7D; cto_bundle=TYNp8V9ZNkdvd0h4akZ1enpvd2VPMFh1OHBZSjRSdWolMkIwTzBPeDVuU2VxWWxTN1B1JTJCNWtlVllybGkxYjVER3JtM1RwWWozbEVRVFJ5d1FXRllVZEk1JTJGMjZxd1J4UGVtMXlsaFpNaTlqMWlLaHppZ1olMkJWMmFKY21CWkhrWndzWHQ3YmNZVEM1MWxFSWJ5ZTBvY3lvYUdqZG14ZFRJQSUyRllOd21VZ2ZWWiUyRmQzeFgxSG96SVN3MkFPJTJCanJwQzIlMkZhS3d5Zndx; gate=1; l_fv=1; _px2=eyJ1IjoiMjQxNjQ3MDAtMWZlZS0xMWVjLWFiNmUtZDc5MzkwZGZhZWYwIiwidiI6ImUzMzMyNzY2LTFmZWQtMTFlYy1iOWYyLTRlNGU3MzQ3NGY2NiIsInQiOjE2MzI3ODc5NjY3NTksImgiOiIxNGU1YWM1OWFkYTEzNTMyMzJiYzQ0N2Y4NTM3MDg4Y2NmYWM1YWQzMjljZDYyNGQ1MWFjMTIxZmEyOTllNWE3In0=; s_getNewRepeat=1632787626653-New",
    }
    response = requests.get(
        'https://www.lulus.com/products/captain-s-blog-tan-double-breasted-coat/579232.html',
        headers=headers).text

    soup = BeautifulSoup(response, 'lxml')

    data = []
    
    res = soup.findAll(text='S')
    if not res: 
        print("wrong response")
        print(soup)
        # alert()

    for container in res:
        cur_size = container.find_parent('div')
        if 'out-of-stock' in str(cur_size):
            now = datetime.now()
            current_time = now.strftime("%-I:%M %p")
            print(current_time + ': Out of Stock')
        else:
            msg = BeautifulSoup(str(cur_size.find_parent()), features="lxml").prettify()
            print(msg)
            alert()


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
    # how_long in 1 seconds

    how_long *= 10
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
    spin(minute * 60 + random.randrange(60)) # unit is second




