import os
os.chdir("/u/c/chanc144/Desktop")
f = open("pride.txt", encoding="utf-8").read().split()


# 1a
for i in range(len(f)):
    f[i].replace(".","")
    f[i].replace(",","")
    f[i].replace("?","")
print(f)
    
dict = {}
for i in f:
    if i not in dict:
        dict.update({i: 1})
    else:
        dict[i] += 1
        
print(dict)

#1b
import random
list_ints = []
for i in range (100):
    list_ints.append(int((random.random()*100)))
print(list_ints)


largest = []
for i in range(11):
    largest.append(max(list_ints))
    del list_ints[list_ints.index(max(list_ints))]
    
print(largest)
    
    
#1c

inv_freq = {6: "the", 12: "a", 1:"hi"}
print(inv_freq.items())
print(sorted(inv_freq.items()))


#invert dict
def get_inv(dict):
    inv_dict= {}
    
    for keyz, valuez in dict.items():
        if valuez not in inv_dict:
            inv_dict[valuez] = keyz
        else:
            inv_dict[valuez] += ", "+ keyz

    return inv_dict
inv_dict = get_inv(dict)
print(inv_dict)
print(sorted(inv_dict.items()))


largest =[]
list_num = list(inv_dict.keys())
print(list_num)
for i in range(11):
    largest.append(max(list_num))
    del list_num[list_num.index(max(list_num))]
    
print(largest)

for k in largest:
    print(inv_dict[k])


#problem 2









#problem 3
import urllib.request
f = urllib.request.urlopen("http://www.cs.toronto.edu/~guerzhoy/180/lab9.html")
page = f.read().decode("utf-8")
f.close()
print(page)

import urllib.request

def searcher(search_term):
    f = urllib.request.urlopen("https://ca.search.yahoo.com/search?p=" + search_term)
    page = f.read().decode("utf-8")
    f.close()
    print(page.index(">Next</a><span>"))
    start = page.index(">Next</a><span>") + 1
    print(page.index("</span></div></div></li></ol></div></div><div"))
    end = page.index("</span></div></div></li></ol></div></div><div")
    print(page[start:end].strip("Next</a><span>").strip("resul"))
    number = page[start:end].strip("Next</a><span>").strip("resul")
    number1 = number.replace(",","")
    print(number1)
    return int(number1)
    
    
    
searcher("engineering science")


def chooser_variant(string1, string2):
    num1 = searcher(string1)
    num2 = searcher(string2)
    
    if num1 > num2:
        return string1
    else: 
        return string2

print(chooser_variant("top ranked school uoft", "top ranked school waterloo"))


















