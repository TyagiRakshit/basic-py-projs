#this is to code a basics secret language like encryption and decryption
# tip:(not for the proj but in general)
'''str1= " hi there rm , r u alright?"
newch = str1.replace("hi", "hello").replace("rm", "kj")
print(newch) #this is to show that replace method can also be used like this i.e if we want multiple substrings to get replaced
''' 
list1 = "hi there"
dict1 = {'a':00 , 'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9}
for i in list1:                                                                      # GENERAL APPORACH
    for j in dict1:
        if i == j:
            print(f" encrypted form of {i} is {dict1[j]}")

