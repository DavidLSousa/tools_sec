import subprocess

path_of_binary = ''

def decodeBinary(binaryCode):
    hex_string = subprocess.run(f"echo '{binaryCode}' | perl -lne 'print pack \"B*\", $_' | xxd -p", shell=True, capture_output=True, text=True)
    res =  subprocess.run(f'echo "{hex_string.stdout}" | xxd -r -p 2>/dev/null', check=False, shell=True, text=True, capture_output=True)
    return res.stdout

def checkAlgorithm():
    with open(path_of_binary) as binaryCode:
        return f'Binary: {decodeBinary(binaryCode)}'

def main():
    print(checkAlgorithm())

if __name__ == '__main__':
    main()
