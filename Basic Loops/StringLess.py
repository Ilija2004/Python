userinp = input("Type less than 6 charachters :  ")
count = 0

for letter in userinp:
    count += 1
    print("letter",count,"is ",letter)
    if (count >= 6):
        print("The string is too long ! ")
        break
    
                         
    
