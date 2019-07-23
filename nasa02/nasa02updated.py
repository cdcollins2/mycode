#!/usr/bin/env python3 
import requests

def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=2018-06-01'
    enddate = '&end_date=END_DATE'
    mykey = '&api_key=Lc63sGh3PtKAsnLOck7yz8raEy2pZ8c7d43V1iAx'

    neourl = neourl + startdate + mykey

    neojson = (requests.get(neourl)).json()

    print(neojson)

main()
