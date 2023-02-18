class ascii_and_word:
    def __init__(self,string):
        self.string= string 
#########################################################################################################################  
   
    def ascii_code(self):   
        lst=[]
        for i in self.string:
            lst.append(format(ord(i),'08b')) 
        result=""
        for l in lst:
            result+=l
       
        return result
######################################################################################################################   
    
    def asciimeaning(self):  
        import string
        ascii_map={}
        keyboard_chars = list(string.printable)
        for i in keyboard_chars:
            ascii_map[format(ord(i),'08b')]=i
  
        substrings=[]
        for j in range(0,len(self.string),8):       
            substrings.append(self.string[j:j+8]) 
       
        meaning=''  
        for a in substrings:                                                                 
            if a in ascii_map:
                meaning+=ascii_map[a]                                                   
        
        return meaning
#########################################################################################################################

print('1. Massage to ASCII\n2. ASCII to massage')
inp=int(input("Enter the mode of operation:\t"))
##############################################

if inp==1:
    ascii_value=input('Enter your massage:\t')
    obj1=ascii_and_word(ascii_value)
    print(obj1.ascii_code())
#########################################################################################################################

elif inp==2:
    ascii_number=input('Enter your ascii code:\t')
    obj2=ascii_and_word(ascii_number)
    print(obj2.asciimeaning())
#########################################################################################################################

else:
    print('wrong input!')

##################################################### COMPLETED ##########################################################
