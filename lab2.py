

current_val = 0

def display_current_value():
    global current_val
    return current_val
    
def add(to_add):
    global current_val 
    global temp
    temp = current_val
    current_val += to_add
    return current_val
    
def mult(to_mult):
    global current_val
    global temp
    temp = current_val
    current_val = current_val * to_mult
    return current_val

def div(to_div):
    global current_val
    global temp
    temp = current_val
    current_val = current_val / to_div
    return current_val
    
def remember():
    global stored_val
    stored_val = current_val
    return stored_val

def recall():
    global stored_val
    return stored_val
    
def undo():
    global temp
    return temp
    
    
    
    

if __name__ == "__main__":
    print("Welcome to the calculator program.")
    print("Current value: 0 ")


print(display_current_value())
print(add(5))
print(mult(5))
print(div(5))

print(undo())
