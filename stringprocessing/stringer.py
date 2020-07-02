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
    string = list(string)
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

def is_integer(ns: str):
    try:
        int(ns) 
    except ValueError :
        return False
    else :
        return True

def is_int_or_EOL(ns: list, n:int ):
        try:
            x = is_integer(ns[n])
        except IndexError:
            return False
        if x == False:
            return False
        else :
            return True
    
def rldecode (string: str):
    l = len(string)
    og = ""
    string = list(string)
    i = 0
    multi = 1
    multistr = ''
    chara = ''
    for i in range(0,l) :
        if not is_integer(string[i]):
            chara = string[i]
            og = og + chara
            multi = 1
        else :
            multistr = multistr + string[i]

        if not is_int_or_EOL(string, (i+1)):
            if is_integer(multistr):
                multi = int(multistr)
                og = og + ((multi - 1) * chara)
            multi = 1
            multistr = ''
                
    return og

def testRLE(string) :
    res = rlencode(string)
    res2 = rldecode(res)
    print(string + " -> " + res + " -> " + res2)
    if res2 == string:
        print("     PASS")
    else:
        print("     FAIL")

def string_in_string(LStr:str, SStr:str):
    LL = len(LStr)
    LS = len(SStr)
    LStr = list(LStr)
    CStr = ''
    Locations = "Matches Begin at Index Posititions:"
    for i in range(0,LL) :
        for n in range(0,LS):
            l = i + n
            try :
                CStr = CStr + LStr[l]
            except IndexError:
                return Locations
            if CStr == SStr:
                Locations = Locations + " " + str(i)
        CStr = ''
    return Locations



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
#testRLE("aaaaabbbaaccd")

#testRLE("abacd")

#testRLE("aaaaaaaa")

#testRLE("a")

#testRLE("aaaaaaaaaaaaabbcc")

s = string_in_string('aaaaaaaaaaaabbbbbbbbbbcccccccccccaaaaaabbbbbccccccaaabbccabab', "ab")
t = string_in_string('mamamamamamama', "mama")
print(s,t)