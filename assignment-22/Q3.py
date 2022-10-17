def even(n):

    if n==1:
        return 2
    return (2*n) + even(n-1)

n=int(input("Enter a number:")) 
sum = even(n)
print(sum)