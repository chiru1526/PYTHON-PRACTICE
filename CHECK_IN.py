#AIRPORT CHECK IN 
import time
print ("Welcome to the Airport")
time.sleep (2)
print ("Check in your luggage")
time.sleep (2)
baggage=int(input("Enter number of baggage: "))
if baggage>7:
    print ("Luggage is too much,you may need to remove items")
else:
    weight=int(input("Enter weight of 1 baggage: "))
    total_weight=weight*baggage
    print("Maximum weight=150 kg")
    print("Total weight=",total_weight)
    if total_weight>150:
        print("Luggage is too heavy,you may need to remove items")
    else:
        print("Check in complete")
        time.sleep(2)
        area=int(input("1.DOMESTIC or 2.INTERNATIONAL? "))
        if area==1:
            print("Enter boarding pass details")
            seat=int(input("Enter seat number 1-60: "))
            if seat>60:
               print("Seat dosent exist")
            elif seat<0:
               print("Seat dosent exist")
            else:
               name=str(input("Enter your name: "))
            flight=int(input("Enter your destination 1.HYD-TPT 2.HYD-BLR 3.HYD-DEL: "))
            time.sleep(2)
            if flight==1:
               print("You are now boarding HYD-TPT")
            elif flight==2:
                print("You are now boarding HYD-BLR")
            elif flight>3:
                print("INVALID")
            else:
                print("You are now boarding HYD-DEL")
            time.sleep(1)
            print("Welcome",name)
            time.sleep(2)
            print("---BOARDING PASS---")
            print("Seat=",seat)
            print("Name=",name)
            print("Flight=",flight)
            print("Domestic")
            print("-------------------")
        elif area==2:
            visa=int(input("Do you have a visa or visa on arrival? 1.YES 2.NO: "))
            if visa==1:
                print("Enter boarding pass details")
                seat=int(input("Enter seat number 1-150: "))
                if seat>150:
                   print("Seat dosent exist")
                elif seat<0:
                   print("Seat dosent exist")
                else:
                   name=str(input("Enter your name: "))
                   flight2=int(input("Enter your destination 1.HYD-DUBAI 2.HYD-TOKYO 3.HYD-NEWYORK: "))
                   time.sleep(2)
                   if flight2==1:
                      print("You are now boarding HYD-DUBAI")
                   elif flight2==2:
                      print("You are now boarding HYD-TOKYO")
                   elif flight2>3:
                      print("INVALID")
                   else:
                      print("You are now boarding HYD-NEWYORK")
                   time.sleep(1)
                   print("Welcome",name)
                   time.sleep(2)
                   print("---BOARDING PASS---")
                   print("Seat=",seat)
                   print("Name=",name)
                   print("Flight=",flight2)
                   print("International")
                   print("-------------------")
            elif visa==2:
               print("You cant board the flight")
            else:
               print("ERROR")

               