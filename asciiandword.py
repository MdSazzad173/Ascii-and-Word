#defining a function that generates ASCCI code
def ascii_code(line):   
    lst=[]
   

# in this line first we used ord() function for finding the ascii value of the letter and format function used to convert the ascii vlaue into 8bit binary string
    for i in line:
        lst.append(format(ord(i),'08b')) 
        

    result=""
    for l in lst:
        result+=l
    return result

#defining a function that converts ASCII code into the readable sentence
def asciicode_to_meaning(ascii_value):  
#creating a dictionary of ascii value and keys  
    import string
    ascii_map={}
    keyboard_chars = list(string.printable)
    for i in keyboard_chars:
        ascii_map[format(ord(i),'08b')]=i

    substrings=[]
    for j in range(0,len(ascii_value),8):       # this loop is for dividing the string 8 bit substring
        substrings.append(ascii_value[j:j+8])
    
  
    meaning=''  
    for a in substrings:                        # comparing the keys
                                                # and taking the values
        if a in ascii_map:
                meaning+=ascii_map[a]           # that contains the 
                                                # similar keys as the substring
    return meaning


print('1. ASCII to meaning\n 2. Word to ASCII')
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
