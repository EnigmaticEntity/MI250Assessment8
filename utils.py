from random import random
#Generates random string of characters, each with a chosen probability
def generator(d, length):
    s = ""
    i = 0
    while i <= length:
        for k, v in d.items():
            rn = random()
            if rn <=  v:
                s += str(k)
        i = i + 1
    return s
	
#Abridges string into one that shows a character and how many times it appeared consecutively
def compressor(s):
    result = ''
    i = 0
    temp = ''
    c_char = s[0]
    temp = c_char
    for char in s:
        if char == temp:
            i = i + 1
        else:
            if i != 1:
                result = result + temp + str(i)
            else:
                result = result + temp
            i = 1
            temp = char
    result = result + s[-1]
    return result
	
#Supposed to be the converse of compressor, but didn't work
def decompressor(s):
    result = ''
    temp = ''
    for char in s:
        if char.isalpha() == True:
            temp = char
        elif char.isnumeric() == True:
            result = result + (temp * int(char))
    return result