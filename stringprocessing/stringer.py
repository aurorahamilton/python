import string

def string_chara_separator(string: str): 
    i = 0
    l = len(string)
    string = list(string)
    for i in range(0, l):
        print(string[i])


def reverse_string_chara_separator(string: str): 
    l = len(string)
    i = l - 1
    string = list(string)
    while i >= 0:
        print(string[i])
        i = i - 1

def find_char(string: str, character: str):
    # find the location of ch in str
    # for ("abhinaba", 'i') it should print 3
    # for ("prokriti", 'a') it should print -1 which means not found
    l = len(string)
    i = 0
    string = list(string.lower())
    for i in range(0,l):
        if string[i] == character :
            return i
    #    if string[i] != character:
    #        i = i + 1
    return -1

def count_char(string: str, character: str):
    l = len(string)
    i = 0
    num = 0
    string = list(string.lower())
    for i in range(0,l) :
        if string[i] == character :
            num = num + 1
    #    i = i + 1
    return num

def rlencode(string: str):
    # aaaaabbbaac, a5b3a2c1
    l = len(string)
    shrt = ""
    string = list(string.lower())
    i = 0
    num = 1
    chara = str(string[i])
    for i in range(1,l) :
        ch = string[i]
        if chara == ch :
            num = num + 1
        elif num == 1:
            shrt = shrt + chara
            num = 1
            chara = ch
        else:
            shrt = shrt + chara + str(num)
            num = 1
            chara = ch
    if num == 1 :
        shrt = shrt + chara 
    else :
        shrt = shrt + chara + str(num)
    return shrt

#print("Hello World")
#s1 = "Abhinaba"
#s2 = "Prokriti"
#string_chara_separator(s1)
#reverse_string_chara_separator(s1)
#Location1 = find_char(s2, "a")
#Location2= find_char(s1, "i")
#print(Location1, Location2)
#count1 = count_char(s2, "i")
#count2 = count_char(s1, "a")
#print(count1, count2)
RLE = "aaaaabbbaaccd"
rle_run = rlencode(RLE)
print(rle_run)