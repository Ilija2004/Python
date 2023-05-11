
def square (s):
    for i in range(s):
        
        if (i == 0 or i == s-1):
            print("#"*s)
        else :
            print("#"+" "*(s-2)+"#")

userinp = int(input("please enter a number"))
square(userinp)
