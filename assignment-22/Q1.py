def add(n):
    if n==1:
        return 1
    return n + add(n-1)

n=int(input("Enter a number:")) 
sum = add(n)
print(sum)       