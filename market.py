command = input("Type yes to start entering the products ")
print(command)
cost = 0
print("Type finish when products are over")
while command != "no":
    over  = input(">> ")
    if  over == "":
         serial = input("item ")
         price = int(input("price "))
         cost += price
         print(serial + '-' + str(price))
    elif over == "finish":
        print(cost)
    
else:
    print("")
