def cubes_sum(n):

    if n==1:
        return 1
    return (n**3) + cubes_sum(n-1)

n=int(input("Enter a number:")) 
sum = cubes_sum(n)
print(sum)