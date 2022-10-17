def square_sum(n):

    if n==1:
        return 1
    return (n**2) + square_sum(n-1)

n=int(input("Enter a number:")) 
sum = square_sum(n)
print(sum)