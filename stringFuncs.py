stringFuncs/
	__init__.py
	utils/
			__init__.py
			utils.py

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

	#Same as generator, but now written into a file
def experimenter(d,length,numSample):
    i = 0
    for i in range(numSample+1):
        s = generator(d,length)
    with open('data.txt','w') as f:
        info = f.write(s)
    return s
experimenter({"a":.1,"b":.3,"c":.6},50,3)

#Prints probabilites of characters used to make string with experimenter function
def examiner():
    a = 0
    b = 0
    c = 0
    m = True
    print("1. Frequencies:{'a':.1,'b':.3,'c':.6}, Length:50,  Samples:1")
    print("2. Frequencies:{'a':.9,'b':.05,'c':.05}, Length:50,  Samples:1")
    while m == True:
        pmt = input("Which one would you like to examine (enter 0 to exit)?")
        if pmt == '0':
            break
        if pmt == '1':
            sample = experimenter({"a":.1,"b":.3,"c":.6},50,1)
            print("|  a  |  b  |  c  |")
            print("-------------------")
            for char in sample:
                if char == 'a':
                    a = a + 1
                elif char == 'b':
                    b = b + 1
                elif char == 'c':
                    c = c + 1
            a = a / 50
            b = b / 50
            c = c / 50
            print("| ", a, " | ", b, " | ", c, " |")
            print(sample)
        elif pmt == '2':
            sample = experimenter({"a":.9,"b":.05,"c":.05},50,1)
            print("|  a  |  b  |  c  |")
            print("-------------------")
            for char in sample:
                if char == 'a':
                    a = a + 1
                elif char == 'b':
                    b = b + 1
                elif char == 'c':
                    c = c + 1
            a = a / 50
            b = b / 50
            c = c / 50
            print("| ", a, " | ", b, " | ", c, " |")
            print(sample)