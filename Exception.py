def myFunc(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("Zero Division error.")
    else:
        print("c:",c)
    finally:
        print("Code Excecution Completed.")

a=int(input("a:"))
b=int(input("b:"))
myFunc(a,b)