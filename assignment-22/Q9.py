def oct(n):
    if n>8:
        oct(n//8)
    print(n%8,end='')       

n = int(input("Enter a decimal number:"))
oct(n)    