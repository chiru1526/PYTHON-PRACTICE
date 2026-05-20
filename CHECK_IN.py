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
        
        print("Enter boarding pass details")
        seat=int(input("Enter seat number 1-60: "))
        if seat>60:
            print("Seat dosent exist")
        elif seat<0:
            print("Seat dosent exist")
        else:
            name=str(input("Enter your name: "))
            flight=int(input("Enter your destination 1.HYD-TPT 2.HYD-BLR 3.HYD-DEL: "))
            if flight==1:
               print("You are now boarding HYD-TPT")
            elif flight==2:
                print("You are now boarding HYD-BLR")
            elif flight>3:
                print("INVALID")
            else:
                print("You are now boarding HYD-DEL")
            print("Welcome",name)
            
        
            
        

    

