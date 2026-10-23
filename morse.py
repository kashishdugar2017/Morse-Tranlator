MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.', 
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---', 
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-', 
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
    'Z': '--..',  '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', 
    '-': '-....-', '(': '-.--.',  ')': '-.--.-'
}

def english_to_morse(text):
    morse_words = []
    
    words = text.upper().split(' ')
    
    for word in words:
        morse_letters = []
        for char in word:
            if char in MORSE_CODE_DICT:
                morse_letters.append(MORSE_CODE_DICT[char])
        
        if morse_letters:
            morse_words.append(' '.join(morse_letters))
            
    return ' / '.join(morse_words)

if __name__ == "__main__":
    user_input = input("Enter the text to translate: ")
    translated_output = english_to_morse(user_input)
    
    print("\nOriginal Text:", user_input)
    print("Morse Code:   ", translated_output)
