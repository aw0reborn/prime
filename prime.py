## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(x):
    num=0
    num=int(x)
    if(num!=x):
        return False
    
        
    if x== 2:
        return True

    if x%3==0:
        return False
    if x==1:
        return False
    for i in range(3,x):
        if x%2==0:
            return False
        else:
            return True 
#### End OF MARKER

#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(x):
    x = int(x)
    for i in range(1,x+1):
        if x%i == 0:
            print i
        
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(x):
    
    x=int(x)
    
    
        
    for i in range (x,0,-1):
        
        if i==2:
            return 2
        if i%2==0:
            continue

        if i%3==0:
            continue
        
        if i < 2:
            return None
        else:
            return i
            break
    
#### End OF MARKER

