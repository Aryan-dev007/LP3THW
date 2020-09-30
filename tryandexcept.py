def divide(a,b):
    try:
        res = a/b
        print("No error")
    
    except ZeroDivisionError:
        print("You put a zero in denominatior.")
    #raise print("mkbhd")
    finally:
        print("Pehle addaoo ki bijili girayi main paas aaun to nakde dikhaye.")
        raise Exception("mkbhd")

a = int(input("> "))
b = int(input("> "))
divide(a,b)