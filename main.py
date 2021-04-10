# Program to convert string to morse code

def convert(string):
    list1 = []
    list1[:0] = string
    return list1


morse = {
    'A': '.-',
    'B': '-..',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '...',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'Ñ': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',

}

word = input('Insert Word\n')
letters = convert(word.upper())
morse_code = [morse.get(letter) for letter in letters if letter in morse.keys()]
str1 = ""
print(str1.join(morse_code))
