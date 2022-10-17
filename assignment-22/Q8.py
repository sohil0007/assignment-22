def bin(n):
    if n>1:
        bin(n//2)
    print(n%2,end='')       

n = int(input("Enter a decimal number:"))
bin(n)    