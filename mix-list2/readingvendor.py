#!/usr/bin/env python3
"""using csv data"""
import csv

def main():
    with open ("vendor.csv", "r") as vendorfile:
        vendata = csv.reader(vendorfile, delimiter=",")
        for row in vendata:
            print("The IP address " + row[2] + " requires the driver " + row[3])

main()
