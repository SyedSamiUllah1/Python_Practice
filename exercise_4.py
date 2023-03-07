# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
ed=int(input("Press 1 if You want to Encrypt or 2 for Decrypt: "))
if (ed==1):
    msg=input("Enter Message: ")
    lst=msg.split()
    
    for i in lst:
        if (len(i)<3):
            # print(i, end=' ')
            reversed_string = "".join(reversed(i))
            print(reversed_string)
        # else:
        #     print(i)
            # if (len(msg)<3):    
        