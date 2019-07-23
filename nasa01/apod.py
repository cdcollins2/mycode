#!/usr/bin/env python3
import urllib.request
import json
import webbrowser
from pprint import pprint as pp 

nasaApi = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=Lc63sGh3PtKAsnLOck7yz8raEy2pZ8c7d43V1iAx' 

def main():
    nasaapiobj = urllib.request.urlopen(nasaApi + mykey)
    nasaread = nasaapiobj.read()
    convertedjson = json.loads(nasaread.decode('utf-8'))

    print(convertedjson)
    input('\nThis is converted json. Press enter to continue')
    
    pp(convertedjson)
    input('\nThis is pretty printed json. Press enter to continue')

    print(convertedjson['explanation'])
    input('\nPress enter to view this photo of the day')

    webbrowser.open(convertedjson['hdurl'])

main()

