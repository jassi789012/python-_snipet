import random
import string

def encode(en):
    en = list(en)
    if len(en) < 3:
        return ''.join(en[::-1])
    else:
        temp = en[0]
        for i in range(0, len(en) - 1):
            en[i] = en[i + 1]
        en[len(en) - 1] = temp

        length = 3

        random_string1 = random.choices(string.ascii_lowercase, k=length)
        new_en = []
        new_en.extend(random_string1)
        new_en.extend(en)
        random_string2 = random.choices(string.ascii_lowercase, k=length)
        new_en.extend(random_string2)

        return ''.join(new_en)
    
def decode(str):
    str = list(str)
    if(len(str) < 3):
        return ''.join(str[::-1])

    else:
        
        str = str[3:-3]

        new_str = [str[len(str) - 1]]
        str = str[:-1]
        new_str.extend(str)
        

        

        return ''.join(new_str)



option = input('''Enter 'E' to Enconde and 'D' to Decode''')

if(option == 'E' or option == 'e'):
    str = input("Enter string to encode: ")
    print("Encoded string: ",encode(str))

# if(option = 'D' or option == 'd'):
#     str = input("Enter string to Decode: ")
#     print("Decoded String : ",decode(str))
