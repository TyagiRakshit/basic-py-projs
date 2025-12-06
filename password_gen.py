#here we will be using two modules random and string.
# so lets talk about string module
import random
import string
'''
Constants in string

These are predefined sets of characters you can use — instead of writing them manually.

Constant	Description	Example Output
string.ascii_letters	All ASCII letters (uppercase + lowercase)->	'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.ascii_lowercase	Lowercase letters only->	'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase	Uppercase letters only->	'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.digits	All digit characters->	'0123456789'
string.hexdigits	Hexadecimal digits->	'0123456789abcdefABCDEF'
string.octdigits	Octal digits->	'01234567'
string.punctuation	All punctuation symbols	->'!"#$%&\'()*+,-./:;<=>?@[\\]^_{
string.printable	All printable characters-> (letters, digits, punctuation, whitespace)	includes letters, digits, punctuation, and space
string.whitespace	All whitespace characters->	' \t\n\r\x0b\x0c' (space, tab, newline, etc.)
'''
# basically these are strings containing range of chars as string
def generate_pswd(min_len,uppercase_criteria = None,special_chars = None,numbers_criteria = None):
    uppercase = list(string.ascii_uppercase)
    special = list(string.punctuation)
    digits = list(string.digits)
    lowercase = list(string.ascii_lowercase)
    mega_list = lowercase
    if numbers_criteria!=None:
        mega_list+=digits
    if special_chars!=None:
        mega_list+=special
    if uppercase_criteria!=None:
        mega_list+=uppercase
    criteria = False
    min_length_criteria = least_uppercase_criteria = least_special_chars = least_numbers_criteria = False
    while not criteria:
        min_length_criteria = least_uppercase_criteria = least_special_chars = least_numbers_criteria = False
        pswd = ''
        count = 0
        while count < min_len:
            pswd +=random.choice(mega_list)
            count+=1
            if len(pswd)>=min_len:
                min_length_criteria = True
            for i in pswd:
                if i in uppercase:
                    least_uppercase_criteria = True
                if i in special:
                    least_special_chars = True
                if i in digits:
                    least_numbers_criteria = True
            criteria = min_length_criteria
            if uppercase_criteria is not None:
                criteria = criteria and uppercase_criteria
            if special_chars is not None:
                criteria = criteria and least_special_chars
            if numbers_criteria is not None:
                criteria = criteria and least_numbers_criteria

    # criteria = min_length_criteria and least_uppercase_criteria and least_special_chars and least_numbers_criteria
    # see we cant use the above conditon coz if the user didnt enter numbers_criteria , then is would result in criteria = false even is all the criterias are met
        print(pswd)

generate_pswd(10,'yes','yes','yes')
''' now here we can also modify as which special characters are allowed by creating the special_char list using list compression'''