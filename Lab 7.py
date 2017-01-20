
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i 
    return len(row)
   
#row = [0, 0, 0]
#print(get_lead_ind(row))   


def get_row_to_swap(M, start_i):

    update = get_lead_ind(M[start_i])
    stored = start_i 
    for row in range((start_i) + 1, len(M)):
        if get_lead_ind(M[row]) < update:
            update = get_lead_ind(M[row])
            stored = row
    return stored 
    
M = [[5, 6, 7, 8],
[0, 0, 0, 1],
[0, 0, 5, 2],
[0, 1, 0, 0]]

#print(get_row_to_swap(M, 1))

def add_rows_coefs(r1, c1, r2, c2):
    list = []
    for i in range(len(M[r1])):
        list.append((M[r1][i] * c1) + (M[r2][i] * c2))
    return list
    
    '''
M = [[5, 6, 7, 8],
[0, 0, 0, 1],
[0, 0, 5, 2],
[0, 1, 0, 0]]

#print(add_rows_coefs(1, 2, 2, 0))
'''

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub + 1, len(M)):
        k = M[i][best_lead_ind] / M[row_to_sub][best_lead_ind]
        M[i] = add_rows_coefs(i, 1, row_to_sub, -k)
       
M = [[5, 6, 7, 8],
[0,0, 1, 1],
[0, 0, 5, 2],
[0, 0, 7, 0]]

#eliminate(M, 1, 2)
#print(M)
            
def normalize_row(r):
    k = 1 / (sum(M[r]))
    for i in range(len(M[r])):
        M[r][i] *= k
'''           
M = [[1, 2, 3]]
normalize_row(0)
print(M)
'''
            
            
def forward_step(M):
    for i in range(len(M)):
        v = get_row_to_swap(M, i)
        M[i], M[v] = M[v], M[i]
       
        eliminate(M, i, get_lead_ind(M[i]))
        
    print(M)

def backward_step(M):
    for row in(len(M), -1, -1):
        M
    
        k = M[i][best_lead_ind] / M[row_to_sub][best_lead_ind]
        M[i] = add_rows_coefs(i, 1, row_to_sub, -k)
  


        
M = [[5, 6, 7, 8],
[0, 0, 0, 1],
[2, 0, 5, 2],
[0, 1, 0, 0]]

forward_step(M)

        
 