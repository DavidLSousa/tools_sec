import re
import sys
import subprocess

agrv = sys.argv[1]

def decodeBase16(input):
    res =  subprocess.run(f'echo "{input}" | xxd -r -p 2>/dev/null', check=False, shell=True, text=True, capture_output=True)
    return res.stdout

def decodeBase32(input):
    res =  subprocess.run(f'echo "{input}" | base32 --decode 2>/dev/null', check=False, shell=True, text=True, capture_output=True)
    return res.stdout

def decodeBase64(input):
    res =  subprocess.run(f'echo "{input}" | base64 --decode 2>/dev/null', check=False, shell=True, text=True, capture_output=True)
    return res.stdout

def decodeBinary(input):
    hex_string = subprocess.run(f"echo '{input}' | perl -lne 'print pack \"B*\", $_' | xxd -p", shell=True, capture_output=True, text=True)
    res =  subprocess.run(f'echo "{hex_string.stdout}" | xxd -r -p 2>/dev/null', check=False, shell=True, text=True, capture_output=True)
    return res.stdout

def checkAlgorithm(input):
    input = input.strip().replace(" ", "")

    if (re.fullmatch(r'[01]+', input)):
        return f'Binary: {decodeBinary(input)}'

    if re.fullmatch(r'[0-9a-fA-F]{32}', input):
        return 'MD5'

    if re.fullmatch(r'[0-9a-fA-F]{40}', input):
        return f'SHA-1'

    if re.fullmatch(r'[0-9a-fA-F]{64}', input):
        return f'SHA-256'

    if re.fullmatch(r'^[A-Z2-7=]+$', input):
        if len(input) % 4 == 0:
            return f'Base32: {decodeBase32(input)}'

    if re.fullmatch(r'[A-Za-z0-9+/=]+', input):
        if len(input) % 4 == 0:
            return f'Base64: {decodeBase64(input)}'
    
    if re.fullmatch(r'^[0-9a-fA-F]+$', input):
        return f'Hexadecimal ou Base64: {decodeBase16(input)}'

    return "not found"

def main():
    result = checkAlgorithm(agrv)
    print(result)

if __name__ == '__main__':
    main()
