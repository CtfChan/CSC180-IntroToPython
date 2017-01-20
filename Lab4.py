#Problem 1

def list_to_str(lis):
    sum = "["
    for i in range(len(lis)):
        if i == len(lis) - 1:
            sum += str(lis[i])
        else: 
            sum += str(lis[i]) + ", "
    sum += "]"
    print(sum)
    
#Problem 2 
def lists_are_the_same(list1, list2):
    i = 0 
    if len(list1) != len(list2):
        return False 
    while list1[i] == list2[i] and i < len(list1) - 1:
        i += 1 
    if list1[i] != list2[i]:
        return False
    return True 


L = [1, 2, 3]
L1 = [1, 2, 3]
print(lists_are_the_same(L, L1))



list_to_str(L)