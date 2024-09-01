#!/usr/bin/env python3
import sys
import requests

mac_address = sys.argv[1]

def getVendorMac():
    try:
        res = requests.get(f"https://api.macvendors.com/{mac_address}")
        if res.status_code == 200:
            return res.text
        else:
            return "Vendor not found"
        
    except:
        pass


def main():
    vendor = getVendorMac()
    print(vendor)


if __name__ == '__main__':
    main()
