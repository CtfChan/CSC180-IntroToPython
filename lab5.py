#problem 1
def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] != list2[i]:
                return False
        return True
    return False
    

p = [1, 2, 3]
p1 = [1, 0, 3]

print(list1_start_with_list2(p, p1))

#problem 2
def match_pattern(list1, list2):
    for i in range(len(list1) - len(list2) + 2):
        u = 0
        while u <= len(list2)-1 and list1[i] == list2[u]:
            i += 1
            u += 1
        if u == len(list2):
            return True
    return False 
    
p1 = [4, 10, 2, 3, 50, 100] 
p2 = [2, 2, 50]

print(match_pattern(p1, p2))

#problem 3
def duplicate(list0):
    for i in range(len(list0) - 2):
        if list0[i] == list0[i + 1]:
            return True
    return False

p3 = [4, 10, 2, 2, 50, 100]

print(duplicate(p3))


#problem 4a
def print_matrix_dim(M):
    row = len(M) 
    column = len(M[0]) 
    print(row, "x", column)

p4 = [[1,2],[3,4],[5,6]]
print_matrix_dim(p4)

#problem 4b
def mult_M_v(M, v):
    #create matrix
    
    newM = []
 
    for i in range(len(M)):
        n = 0
        for p in range(len(v)):
            n += M[i][p] * v[p]
        newM.append(n)
        n += 1
    
    return newM


p4 = [[1,2],[3,4],[5,6]]
p5 = [0, 0]


print(mult_M_v(p4, p5))




#problem 5a
def print_list(list):
    for i in range(len(list)):
        print(list[i])

pets = [["Shoji", "cat", 18],
["Hanako", "dog", 15],
["Sir Toby", "cat", 10],
["Sachiko", "cat", 7],
["Sasha", "dog", 3],
["Lopez", "dog", 13]]

print_list(pets)


#5b
def print2_list(list):
    for i in range(len(list)):
        print(list[i][1])


pets = [["Shoji", "cat", 18],
["Hanako", "dog", 15],
["Sir Toby", "cat", 10],
["Sachiko", "cat", 7],
["Sasha", "dog", 3],
["Lopez", "dog", 13]]

print2_list(pets)


#5c
def total_age(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i][2]
    print(sum)
    
pets = [["Shoji", "cat", 18],
["Hanako", "dog", 15],
["Sir Toby", "cat", 10],
["Sachiko", "cat", 7],
["Sasha", "dog", 3],
["Lopez", "dog", 13]]
    
total_age(pets)

#5d
def num_dogs(list):
    counter = 0
    for i in range(len(list)):
        if list[i][1] == "dog":
            counter += 1
    print(counter)
    
pets = [["Shoji", "cat", 18],
["Hanako", "dog", 15],
["Sir Toby", "cat", 10],
["Sachiko", "cat", 7],
["Sasha", "dog", 3],
["Lopez", "dog", 13]]
    
num_dogs(pets)

#problem 6
def expressible_as_sum_squares(k):
    count = 0
    for i in range(1, k):
        for p in range(i, k):
            if i **2 + p**2 == k:
                count += 1
    if count >= 2:
        return True
    return False


def square_taxi_count(n):

    counter = 0
    for i in range(50, n + 1):
        if expressible_as_sum_squares(i) == True:
            counter += 1
    print(counter)
    
    
square_taxi_count(65)




















