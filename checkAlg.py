import re
import sys

agrv = sys.argv[1]

def checkAlgorithm(input):
    input = input.strip()

    if re.fullmatch(r'[0-9a-fA-F]{32}', input):
        return "MD5"

    if re.fullmatch(r'[0-9a-fA-F]{40}', input):
        return "SHA-1"

    if re.fullmatch(r'[0-9a-fA-F]{64}', input):
        return "SHA-256"

    if re.fullmatch(r'[A-Za-z0-9+/=]+', input):
        if len(input) % 4 == 0:
            return "Base64"
    
    return "not found"

def main():
    result = checkAlgorithm(agrv)
    print(result)

if __name__ == '__main__':
    main()


