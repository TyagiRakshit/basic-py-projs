#this is to code a basics secret language like encryption and decryption
# tip:(not for the proj but in general)
'''str1= " hi there rm , r u alright?"
newch = str1.replace("hi", "hello").replace("rm", "kj")
print(newch) #this is to show that replace method can also be used like this i.e if we want multiple substrings to get replaced
''' 
encry_decrypt_diary = {
    'a':'@', 'b':'#', 'c':'$', 'd':'%', 'e':'&',
    'f':'*', 'g':'!', 'h':'?', 'i':'+', 'j':'=',
    'k':'<', 'l':'>', 'm':'^', 'n':'~', 'o':'/',
    'p':'|', 'q':';', 'r':':', 's':'-', 't':'_',
    'u':'0','v':'1','w':'2','x':'3','y':'4','z':'5',
    '0':'A','1':'B','2':'C','3':'D','4':'E',
    '5':'F','6':'G','7':'H','8':'I','9':'J',
    ' ':' '
}

def encrypt(msg):
    encrypted_msg = ""
    for char in msg:
        if char == " ":
            encrypted_msg += " "  # keep spaces
        elif char not in encry_decrypt_diary:
            extra = f"({char})"
            encrypted_msg +=extra
        else:
            encrypted_msg += encry_decrypt_diary[char]
    return encrypted_msg


# Step 1: create reverse dictionary just like list comprehension
decrypt_dict = {str(v): k for k, v in encry_decrypt_diary.items()}

def decrypt(msg):
    decrypted_msg = ""
    for char in msg:
        decrypted_msg += decrypt_dict.get(char, char) #key → the key you want to look up in the dictionary
                                                      # default_value → the value to return if the key does not exist in the dictionary
    return decrypted_msg
print("hey ! enter ur choice:")
print("1. Encrypt msg\n 2. decrypt message:\n")
choice = int(input("enter ur choice:\n"))
match(choice):
    case 1:
        message = input("enter message to encrypt:")
        encrypted_mssg = encrypt(message)
        print(f"encrypted message is:\n{encrypted_mssg}")

    case 2:
        de_message = input("enter message to decrypt:")
        decrypted_message = decrypt(de_message)
        print(f"decrypted message is:\n{decrypted_message}")
    case _:
        print("invalid message!")






