def collatz(n):
    count=0
    while n>1:
        if(n%2):
            n=3*n+1
        else:
            n=n//2
        print(1,end=" ")
        count+=1
    print("\nCount:",count)

n=int(input("Enter n:"))
print("Sequence:",end="\n")
collatz(n)