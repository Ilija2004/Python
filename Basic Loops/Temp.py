temp = int(input("Please enter the temperature: "))
if temp < 0 :
    print ("Freezing Weather")
elif temp >= 1 and temp <= 10:
    print ("Very Cold Weather")
elif temp >= 11 and temp <= 20:
    print ("Cold Weather")
elif temp >= 21 and temp <= 30:
    print ("Normal in Temp")
elif temp >= 31 and temp <= 40:
    print ("its Hot")
else :
    print ("its very Hot")
