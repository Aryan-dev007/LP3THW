def loop(i,n,num,a):
    for i in range(i,n):
        print(f"The first number is: {i}")
        num.append(i)
        #i+=a
        print("Numbers:",num)
        print(f"Last number: {i}")
    
    print("The number list:")
    
    for n in num:
        print(n)

print("Enter i , n, a")
i = int(input(">> "))
n = int(input(">> "))
num = []
a = int(input(">> "))

loop(i,n,num,a)