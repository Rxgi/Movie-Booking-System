print("Welcome to the Cinema Website")
print("")
print("Below are the options of what you can do:")
print("")
print("Movies")
print("Showtimes")
print("Tickets")
print("")

Total = 0
TicketTotal = 0
OptionTrue = True
MovieChoose = True
ShowtimeTrue = True
TicketsTrue = True

while OptionTrue == True:    
    OptionInput = input("Please enter a Category: ").lower()  
    
    if OptionInput == "movies":  
        print("")
        print("Here are the options for the different Movies:")
        print("")
        print("A")
        print("B")
        print("C")
        print("")
        
        MovieTrue = True
        while MovieTrue == True:
            MoviePick = input("Please enter a Movie option: ")
            print("")
            if MoviePick == "A" or MoviePick == "a":
                print("Movie A details:")
                print("Duration: 120 Mins")
                print("Genre: Action")
                print("")
                MovieTrue = False
            elif MoviePick == "B" or MoviePick == "b":
                print("Movie B details:")
                print("Duration: 95 Mins")
                print("Genre: Comedy")
                print("")
                MovieTrue = False
            elif MoviePick == "C" or MoviePick == "c":
                print("Movie C details:")
                print("Duration: 150 Mins")
                print("Genre: Drama")
                print("")
                MovieTrue = False
            else:
                print("Please enter a valid Movie option")
        
        again = input("Would you like to go back to the options menu? (yes/no): ").lower()
        if again.lower() == "yes":
            OptionTrue = True
        else:
            print("Next you will be able to order tickets")
            break  

    elif OptionInput == "showtimes":
        print("Here are the available showtimes for the movies:")
        print("")
        print("Morning: 9:00 - 12:00")
        print("")
        print("Afternoon: 12:00 - 18:00")
        print("")
        print("Evening: 18:00 - 21:00")
        print("")
        
        again = input("Would you like to go back to the options menu? (yes/no): ").lower()
        if again.lower() == "yes":
            OptionTrue = True  
        else:
            print("Next you will be able to order tickets")
            break  

    elif OptionInput == "tickets":
        print("Here are the ticket prices:")
        print("")
        print("Child: £5")
        print("Adult: £10")
        print("Senior : £7")
        print("")
        print("for per movie the prices are:")
        print("")
        print("Movie A: £10")
        print("Movie B: £8")
        print("Movie C: £12")
        print("")
        print("The Age Ranges for these are:")
        print("")
        print("Child: 4-16")
        print("Adult: 17-60")
        print("Senior: 60+")
    
        again = input("Would you like to go back to the options menu? (yes/no): ").lower()
        if again.lower() == "yes":
            OptionTrue = True  
        else:
            print("Next you will be able to order tickets")
            break  

    else:
        print("Invalid category. Please enter 'Movies', 'Showtimes', or 'Tickets'.")

A = 10
B = 8
C = 12
a = 10
b = 8
c = 12

while MovieChoose == True:
    print("")
    Movie_Option = input("Please enter what movie you would like to see: ")
    if Movie_Option == "A":
        Total = Total + 10
        MovieChoose = False
    elif Movie_Option == "a":
        Total = Total + 10
        MovieChoose = False
    elif Movie_Option == "B":
        Total = Total + 8
        MovieChoose = False
    elif Movie_Option == "b":
        Total = Total + 8
        MovieChoose = False
    elif Movie_Option == "C":
        Total = Total + 12
        MovieChoose = False
    elif Movie_Option == "c":
        Total = Total + 12
        MovieChoose = False
    else:
        print("Please choose a valid Movie")

print("\nNow you are able to buy up to 10 tickets through all age groups\n")

while TicketsTrue == True:
    ChildTickets = input("\nPlease enter the ammount child tickets you need: \n")
    if not ChildTickets.isdigit():
        print("Please enter a numeric digit")
        continue
    else:
        ChildTickets = int(ChildTickets)
    
    AdultTickets = input("\nPlease enter the ammount adult tickets you need: \n")
    if not AdultTickets.isdigit():
        print("Please enter a numeric digit")
        continue
    else:
        AdultTickets = int(AdultTickets)
    
    SeniorTickets = input("\nPlease enter the ammount senior tickets you need: \n")
    if not SeniorTickets.isdigit():
        print("Please enter a numeric digit")
        continue
    else:
        SeniorTickets = int(SeniorTickets)
    
    TicketTotal = ChildTickets + AdultTickets + SeniorTickets
    
    if TicketTotal <= 10 and TicketTotal > 0:
        TicketsTrue = False
    else:
        print("Please order between 1 to 10 tickets")

ChildTotal = ChildTickets * 5
AdultTotal = AdultTickets * 10
SeniorTotal = SeniorTickets * 7

Total = Total + ChildTotal + AdultTotal + SeniorTotal
Totalfloat = float(Total)
BookingFee = Totalfloat + 1.50

print("\nYour total for this order is:\n")
print("Total: £" + str(BookingFee))





