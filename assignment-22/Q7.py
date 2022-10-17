def sum_d(n):
    if n//10==0:
        return n
    return n%10 + sum_d(n//10)

n = int(input("Enter a number:")) 
s = sum_d(n)
print(s)       