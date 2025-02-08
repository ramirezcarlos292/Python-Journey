
def window(arry, w):
    l = len(arry)
    # slide window passes over array
    # length_array - window_size + 1 array_starts_0
    for i in range(l-w+1):
        print(arry[i:w+i])
    
w = 3
arry = []  
for k in range(10):
    arry.append(k)
window(arry, w)