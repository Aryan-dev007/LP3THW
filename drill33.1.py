def loop(i,n,num,a):
    for i in range(i,n):
        print(f"Top number: {i}")
        num.append(i)
        i += a
        print("Now number is:",num)
        print(f"Last number:{i}")

    print("Numbers in the list:")

    for n in num:
        print(n)


loop(0,6,[],1)