def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    counter = 0
    
    for i in range(length):
        
        if board[y][x] != " ":
            print("Some of the squares are occupied, failed to put the sequence on the board")
            return 
        if board[y][x] == col:
            counter += 1
        
        board[y][x] = col    
        y += d_y
        x += d_x
        
    if counter == length:
        print("The exact sequence was already found on the board")
        return 
    
    print("Success")


import os
os.chdir("/u/c/chanc144/Desktop")
f = open("data2.txt", encoding="utf-8")
text = f.read()
print(text)


text2 = text.lower() 
list= []
string = ""
for i in range(len(text2) - 3):
    if text2[i:i+3] == "lol":
        string += text[i:i+3]
print(string)
    
def dict_to_str(d):

    string = ""
    for keys in dict:        
        string += str(keys) + str(dict[keys]) + "\n"
    print(string)

dict = {1:2, 5:6}
dict_to_str(dict)


'''
print(dict.keys()) 

for keys in dict:
    print(keys, dict[keys])
'''



def dict_to_str_sorted(d):

    list = []
    string =""
    for keys in dict:        
        list.append(keys)
    list = sorted(list)
    for keys in list:
        string += str(keys) + "," + str(dict[keys]) + "\n"
    print(string)

dict ={1:2, 0:3, 10:5}
dict_to_str_sorted(dict)


#sorted(string)  returns a copy of the sorted string 
#string.sort() changes original string, returns None





os.chdir("/u/c/chanc144/Desktop")
f = open("cmudict-0.7b.phones.txt", encoding="utf-8")
text1 = f.read()
print(text1)
list_vowels = []
text1 = text1.split("\n")
for line in text1:
    line = line.split("\t")
    
    if line[1] == "vowel":
        list_vowels.append(line[0])
    
    print(list_vowels)
    

list_vowels = ['AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']


#remove spaces in the beginning and end of the entire string 




