print ("WELCOME TO THE HOTEL")
import time
time.sleep(1) 
print ("ROOMS 101-105 ARE LUXURY ROOMS")
time.sleep(1) 
Room=int(input("SELECT A ROOM 101-110: "))
money=0
if Room>110:
    print("ROOM DOSENT EXIST")
elif Room<101:
     print("ROOM DOSENT EXIST")
else:
     print ("You have chosen room",Room)
     time.sleep(2) 
     BREAKFAST=int(input("WOULD YOU LIKE BREAKFAST? 1=YES,2=NO: "))
     if BREAKFAST==1:
         time.sleep(2)
         print("You have added breakfast PRICE: ")
         print(money+500)
         money=money+500
     elif BREAKFAST==2:
         time.sleep(2)
         print("NO added breakfast")
     else:
         time.sleep(2)
         print("INVALID")
     if Room<=105:
        time.sleep(2)
        print("It is a luxury room PRICE: ")
        print(money+2000)
        money=money+2000
     else:
        time.sleep(2)
        print("It is a normal room PRICE: ")
        print(money+500)
total_price=money
time.sleep(2)
print("TOTAL PRICE=",total_price)
print("THANK YOU FOR CHOOSING OUR HOTEL")
        
        