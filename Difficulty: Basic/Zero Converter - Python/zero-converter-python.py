def pos(n):
    while n>0:
        n-=1
        print(n,end=" ")
        
    
def neg(n):
    while n<=0:
        print(n,end=" ")
        n+=1
    
def main(n):
    if n==0:
        print("already zero")
    elif n<0:
        neg(n)
    else:
        pos(n)