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
    for i in range(0,LL - LS) :
        for n in range(0,LS):
            l = i + n
            CStr = CStr + LStr[l]
            if CStr == SStr:
                Locations = Locations + " " + str(i)
        CStr = ''
    return Locations

def strStr(LStr:str, SStr:str):
    LL = len(LStr)
    LS = len(SStr)
    LStr = list(LStr)
    SStr = list(SStr)
    location = -1
    for i in range(0,LL - LS) :
        location = i
        for j in range(0,LS):
            l = i + j
            if LStr[l] != SStr[j]:
                location = -1
                break
        if location >= 0 :
            return location
    return -1   

def StrCmp(str1: str, str2: str):
    L1 = len(str1)
    L2 = len(str2)
    str1 = list(str1)
    str2 = list(str2)
    r = 0
    if L1 > L2 :
        L = L2
    if L1 <= L2 :
        L = L1
    for i in range (0,L):
        if str1[i] == str2[i]:
            continue
        elif ord(str1[i]) > ord(str2[i]):
            r = -1
            return r
        else:
            r = 1
            return r
    if L1 > L2 :
        r = -1
        return r
    elif L1< L2:
        r = 1
        return r


def FileWordbyWord(filepath: str) :
    file = open(filepath, "r")
    r = file.read()
    l = len(r)

    word = ""
    for i in range (0,l):
        if r[i] != " " and r[i] != "\n" :
            word = word + r[i]
        else :
            print(word)
            word = ""

def DNAFileReader(filepath: str) :
    DNAFile = open(filepath)
    DNA = DNAFile.read()
    l = len(DNA)
    ret = ''
    for i in range(0,l):
        if DNA[i] == ">":
            flag = True
        elif DNA[i] == "\n":
            flag = False
        elif flag:
            continue
        else:
            ret = ret + DNA[i]
    return ret

def MaxRepeatLetter(filepath: str):
    DNA = DNAFileReader(filepath)
    l = len(DNA)
    MaxNumber = 1
    CompNumber = 1
    IndexPosition = 0
    MaxLetter = DNA[1]
    for i in range(1,l):
        if DNA[i] == DNA[i-1]:
            CompNumber = CompNumber + 1
        elif DNA[i] != DNA[i-1] and CompNumber > MaxNumber:
            MaxNumber = CompNumber
            IndexPosition = i - CompNumber
            MaxLetter = DNA[i-1]
            CompNumber = 1
        elif DNA[i] != DNA[i-1] and CompNumber < MaxNumber:
            CompNumber = 1
        elif DNA[i] != DNA[i-1]:
            CompNumber = 1
    if DNA[i] == DNA[i-1]:
        CompNumber = CompNumber + 1
    elif DNA[i] != DNA[i-1] and CompNumber > MaxNumber:
        MaxNumber = CompNumber
        IndexPosition = i - CompNumber
        MaxLetter = DNA[i-1]
        CompNumber = 1
    elif DNA[i] != DNA[i-1] and CompNumber < MaxNumber:
        CompNumber = 1
    elif DNA[i] != DNA[i-1]:
        CompNumber = 1

    return IndexPosition, MaxNumber, MaxLetter

#def CDNAtoRNA(filepath: str):
#    DNA = DNAFileReader(filepath)

#Make a CDNA to RNA translation code
#The final genome of sequenced SARS-CoV-2 consists of a single, 
# positive-stranded RNA that is 29,811 nucleotides long, broken down as follows:
#  8,903 (29.86%) adenosines, 5,482 (18.39%) cytosines, 5,852 (19.63%) guanines, and 9,574 (32.12%) thymines.

def NeucleotideCounter(filepath: str) :
    DNA = DNAFileReader(filepath)
    l = len(DNA)
    Total = l + 1
    AC = 0
    TC = 0
    GC = 0
    CC = 0
    UC = 0
    for i in range(0,l):
        if DNA[i] == "A" :
            AC = AC + 1
        elif DNA[i] == "T" :
            TC = TC + 1
        elif DNA[i] == "U" :
            UC = UC + 1
        elif DNA[i] == "G" :
            GC = GC + 1
        elif DNA[i] == "C" :
            CC = CC + 1
    AP = 100 *(AC/Total)
    TP = 100 * (TC/Total)
    UP = 100 * (UC/Total)
    GP = 100 * (GC/Total)
    CP = 100 * (CC/Total) 
    if UC == 0 :
        Order = "Total, ATGC"
        return Order, Total, AC, AP, TC, TP, GC, GP, CC, CP 
    elif TC == 0 :
        Order = "Total, AUGC"
        return Order, Total, AC, AP, UC, UP, GC, GP, CC, CP 


         


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

#s = string_in_string('aaaaaaaaaaaabbbbbbbbbbcccccccccccaaaaaabbbbbccccccaaabbccabab', "ab")
#t = string_in_string('mamamamamamama', "mama")
#print(s,t)

#a = string_in_string('abcdeef', "cde")

#a = strStr("abhinabhna", "bhn")
#a = StrCmp("Abhinaba", "Abhi")
#print(a)
#FileWordbyWord("C:\\Users\\prokr\\OneDrive\\python\\Dictionary.txt")

filepath = "C:\\Users\\prokr\\python\\stringprocessing\\COVID19.txt"
a,b,c = MaxRepeatLetter(filepath)
print(a,b,c)

print(NeucleotideCounter(filepath))