#defining a function that generates ASCCI code
def ascii_code(line):   
    lst=[]
    # d=''

# in this line first we used ord() function for finding the ascii value of the letter and format function used to convert the ascii vlaue into 8bit binary string
    for i in line:
        lst.append(format(ord(i),'08b')) 
        

    result=""
    for l in lst:
        result+=l
    return result

#defining a function that converts ASCII code into the readable sentence
def asciicode_to_meaning(ascii_value):  
    ascii_map = {
    "00100000": " ",
    "01000001": "A",
    "01000010": "B",
    "01000011": "C",
    "01000100": "D",
    "01000101": "E",
    "01000110": "F",
    "01000111": "G",
    "01001000": "H",
    "01001001": "I",
    "01001010": "J",
    "01001011": "K",
    "01001100": "L",
    "01001101": "M",
    "01001110": "N",
    "01001111": "O",
    "01010000": "P",
    "01010001": "Q",
    "01010010": "R",
    "01010011": "S",
    "01010100": "T",
    "01010101": "U",
    "01010110": "V",
    "01010111": "W",
    "01011000": "X",
    "01011001": "Y",
    "01011010": "Z",
    "01100001": "a",
    "01100010": "b",
    "01100011": "c",
    "01100100": "d",
    "01100101": "e",
    "01100110": "f",
    "01100111": "g",
    "01101000": "h",
    "01101001": "i",
    "01101010": "j",
    "01101011": "k",
    "01101100": "l",
    "01101101": "m",
    "01101110": "n",
    "01101111": "o",
    "01110000": "p",
    "01110001": "q",
    "01110010": "r",
    "01110011": "s",
    "01110100": "t",
    "01110101": "u",
    "01110110": "v",
    "01110111": "w",
    "01111000": "x",
    "01111001": "y",
    "01111010": "z"
}
    substrings=[]
    for i in range(0,len(ascii_value),8):       # this loop is for diving the string 8 bit substring
        substrings.append(ascii_value[i:i+8])
    meaning=''
   
   
    for a in substrings:                        # comparing the keys
                                                # and taking the values
        if a in ascii_map:
                meaning+=ascii_map[a]           # that contains the 
                                                # similar keys as the substing
    return meaning


print('1. ASCII to meaning\n2. Word to ASCII')
# For mode of oparetion:
inp=int(input('\nchoose your mode of operation:\t'))

if inp==1:
    ascii_value=input('Enter your binary ascii string:\t')
    print(asciicode_to_meaning(ascii_value))


elif inp==2:
    line=input('Enter your line:\t')
    print(ascii_code(line))
    

else:
    print('please choose the right option!!!')
    
#Completed........