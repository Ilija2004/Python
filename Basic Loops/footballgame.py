
stand = input("Please choose one of these stands WA, WC, M : ")
adult = int(input("Please enter the number of adults : "))
child = int(input("Please enter the number of children : "))
pens = int(input("Please enter the number of pensioners : "))

if ( stand == "wa" or "wc" ):
    childPrice = child * 10
    adPrice = adult * 20
    penPrice = pens * 15
    total = childPrice+adPrice+penPrice
    print("The Total price of your tickets are:",total,"€")
    
elif (stand == "m"):
      childPriceM = child * 5
      adPriceM = adult * 12
      penPriceM = pens * 10
      totalM = childPriceM+adPriceM+penPriceM
      print("The Total price of your tickets are  :",totalM,"€")
else :
    print("input valid stand")


    
