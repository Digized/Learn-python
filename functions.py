x = 5
def sum(a,b):
    return (x + b, a) 

def editX(a):
    global x 
    x = a

sum(20, 2) #7

editX(20)

print(sum(20, 20)) #

print(sum(1,2))