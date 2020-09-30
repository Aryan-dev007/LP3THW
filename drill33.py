def loop(i,n,num,a):
    while i<n:
        print(f"The first number i is {i}")
        num.append(i)
        i += a
        print("The numbers now are:",num)
        print(f"The last number is {i}")
        #return loop(i,n,num,a)
        

print("Enter two numbers , in which second number is greater than the first number.")
print("Also enter the steps if you want, otherwise press 1 .")
i = int(input())
n = int(input())
a = int(input())
num = []

loop(i,n,num,a)
print("The final list: ",num)
