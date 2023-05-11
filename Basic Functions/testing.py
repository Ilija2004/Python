def sum (a,b):
    print(a+b)

#Main  code

n1 = int(input("Please input first number : "))
n2 = int(input("Please input second number : "))

sum(n1,n2)

#-----------------------------------------------------------------------------

def average (a,b,c,d):
    return (a+b+c+d)/4

#Main Code

n1 = int(input("Please input first number : "))
n2 = int(input("Please input second number : "))
n3 = int(input("Please input third number : "))
n4 = int(input("Please input fourth number : "))

print("Your average is:",average(n1,n2,n3,n4))


#-----------------------------------------------------------------------------

def name (name):
    print("Hello there",name)

def age (a):
    return 2021-a

#Main code

user1 = input("Please input your name :")
name(user1)

user2 = int(input("Please enter your age : "))

print("You wrere born in ",age(user2))
