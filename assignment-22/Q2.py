def odd(n):

    if n==1:
        return 1
    return (2*n-1) + odd(n-1)

n=int(input("Enter a number:")) 
sum = odd(n)
print(sum) 