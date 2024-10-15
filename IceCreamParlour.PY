#importing the random functionality that will be used to suggest random toppings later on. 
import random

#Creating a list with the dictionaries of the authorized users with their assigned IDs.
#Will be used by a function later that will check the ID against the name to authenticate an user. 

authUsers = [
    {"name": "Jo Lopez", "ID": "JL14358"},
    {"name": "James Brown", "ID": "JB37562"},
    {"name": "Mohammed Syed", "ID": "MS13374"},
    {"name": "Tariq Malik", "ID": "TM76117"},
    {"name": "Etta Jones", "ID": "EJ43378"},
]

#A Dictionary that is storing the flavour of ice creams that my program will offer saved as the Keys 
#As well as a touple containing the description of the flavour as a string and the price as a integer.

iceCream = {
    "Matcha": ("Ice Cream Flavour - Japanese Green Tea Flavour", 2.00),
    "Rum and Raisin" : ("Ice Cream Flavour - Rich rum ice cream with juicy raisins" ,2.00),
    "Sweetcorn" : ("Ice Cream Flavour - Creamy and slightly savory flavour", 1.50)}  

#A Dictionary that is storing the toppings that my program will offer saved as the Keys 
#As well as a touple containing the description of them as a string and the price as a integer.
 
    
toppingChoice = {   
    "Choc Flake" : ("Topping - Crunchy chocolate flakes",1.00),
    "Caramel Sauce" : ("Topping - Smooth and buttery caramel sauce",1.00)}


def checkNameandID(users):
    #Start with a while loop asking for the input until they match what I had on my list 
    while True:
        srvrName = input("Enter name: ")
        srvrID = input("Enter ID: ")
    #this checks my dictionary for the keys "name" and "ID" and checks against the srvrName and srvrID that was input
    #If a match is found then the loop breaks and gives a welcome message to the server, else it keeps asking the user to try again. 
        foundUser = False
        for user in users:
            correctUsername = user["name"]
            correctPassword = user["ID"]     
            if srvrName == correctUsername and srvrID == correctPassword:
                foundUser = True
                break

        if foundUser == True:
            print(f"Welcome {srvrName}")
            break
        else:
            print("Incorrect name or ID. Please try again.")
    #this function then returns the server's name.
    return srvrName
            
def getTableInfo():
    #Using a while loop to keep asking for an input until the valid information is given.
    while True:
        #Asks the user to input the table number which is then converted to an integer and breaks the loop.
        #If the input is equal or less than 0, asks the user to double check and input the correct table number
        #If the input can't be converted to an integer, it will also provide the error message and continue the loop until it is a valid input.
        try:
            tableNumber = int(input("Enter the table number: "))
            if tableNumber > 0:
                break
            else: 
                print("Invalid input. Please check if the table number is correct.")
        except:
            print("Invalid input. Please check if the table number is correct.")
        #Asks the user to input the amount of guests which is then converted to an integer and breaks the loop.
        #If the input is equal or less than 0, asks the user to double check and input the correct number
        #If the input can't be converted to an integer, it will also provide the error message and continue the loop until it is a valid input.
    while True:
        try:
            numPeople = int(input("Enter the number of people at the table: "))
            if numPeople > 0:
                break
            else: 
                print("Invalid input. Please check if you entered the right amount of people.")
        except:
            print("Invalid input. Please check if you entered right amount of people.")
    #After both inputs are valid, returns the table number and number of people. 
    return tableNumber, numPeople

def printMenu(icecream, toppings):

    print("These are the flavours you can choose from: ")
    #Goes through my iceCream dictionary items and prints them by printing the Key (In this case Ice cream flavour) 
    #And the touple with the description of the ice cream and the price, the price is formated to print with 2 decimal points as a float. 
    for key, (description, price) in icecream.items():
        print(f"{key} - {description} - £{price:.2f} :")
    #Goes through my toppings dictionary items and prints them by printing the Key (In this case Ice cream flavour) 
    #And the touple with the description of the toppings and the price, the price is formated to print with 2 decimal points as a float.     
    print("These are the toppings you can add: ")
    for key, (description, price) in toppings.items():
        print(f"{key} - {description} - £{price:.2f} :")

def getOrder(guests, icecream, toppings):
    #First I created a empty list outside of the loop to store the order of each guest as well as a customer counter.
    orders = []
    customer = 0
    
    #For loop that will repeat depending on the number of guests, which is a argument in the function that will be used with the number of people that was taken previously.
    #And after every loop it will add +1 to the customer counter, so when it prints the f statement, it will also provide with the customer number.
    for guest in range(guests): 
        customer += 1
        print(f"order for customer {customer}:")
    #Started with an empty variable called flavour and created a while loop that will ask for an input of flavour and will keep looping
    #Until the input is in the icecream argument, once the input matches the argument, the loop ends.         
        flavour = ""
        while flavour not in icecream:
            flavour = input("Enter the ice cream flavour: ")

    #Started with an empty variable called topping and a while loop that will be asking for a valid topping or an empty string.    
        topping = "1"
        while topping not in toppings and topping != "":
            topping = input ("Enter the topping (Leave blank if none are selected): ")       
 
    #Checks if the topping variable is empty to suggest a random topping.     
        if topping == "":
            #A random topping will be selected from the toppings dictionary by using the random.choice() function.
            #This function selects a random item from a list, so the "list" function will turn my toppings dictionary into a list and 
            #the .key will make it so that list only has the keys, not the touple with price and description. 
            toppingSuggestion = random.choice(list(toppings.keys()))
            print(f"You haven't selected a topping, would you like to add: {toppingSuggestion} to the order?")
            addSuggestion = input ("Yes or No: ")
            
            #If the user inputs Yes, then it will save the suggestion into the toppings variable, if the input is No then it won't save anything.

            if addSuggestion == "Yes":
                topping = toppingSuggestion 
        #Appends the order list with dictionaries in the format of "Ice Cream" as a string and then flavour variable and then "Toppings" as a string and the choice of topping as a variable (Or left blank)
        orders.append({"Ice cream": flavour, "Topping": topping})
    #Returns the list of orders.
    return orders 

def generateReceipt(table, orders, server):
    #Printing the header of the receipt including the variable with the table number
    #And create a variable to calculate the final total of the orders outide of the loop.
    print("-" * 38)
    print(f"--- Ice Cream Parlour for: Table {table}---")
    print("-" * 38)
    finalTotal = 0

    #Start with a for loop to interate through the dictionaries saved in the list of orders  
    for i in range(len(orders)):
        
        #Saves the orders list into the variable "order" using the index "i". 
        
        order = orders[i]
        
        #from the list of dictionaries of orders, it will look at the key "Ice cream" and retrieve the flavour that was selected
        #then, using the flavour as key, it will look at the dictionary iceCream and retrieve price of the ice cream by getting index 1 inside of the touple, which is the integer with the price value.
        #then it will save that in the variable flavourPrice.
                
        flavour = order["Ice cream"]
        flavourPrice = iceCream[flavour][1]
        
        #Similar to the previous line of code, however it looks through the dictionary with the key "Topping" instead of "Ice cream"
        #however if there is no topping selected then the topping will be saved with a price of 0.
        
        topping = order["Topping"]
        if topping:
            toppingPrice = toppingChoice[topping][1]
        else:
            toppingPrice = 0
        #Save both the price of the flavour and the topping per person in this total and then add the indididual person total to the final total of the table.    
        personTotal = flavourPrice + toppingPrice
        finalTotal = finalTotal + personTotal 

        #Prints the total the current person has, including their flavour and topping if there is anything saved in the topping variable. 
        #The code then adds +1 to person, so the final display shows the order separated by the number of guests.
        #The price is also formated with .2f so it shows 2 decimal points. 

        print(f"Person {i + 1} Price")
        print(f"{flavour} £{flavourPrice:.2f}")
        if topping:
            print(f"{topping} £{toppingPrice:.2f}")

        print(f"Total: £{personTotal:.2f}")
        print()
    #Finally, it prints the total for the whole table and the name of the server that has taken the order. 
    print(f"Total for the table: £{finalTotal:.2f}")
    print(f"Your server is: {server}!")
    print("Enjoy your ice cream! Remember to recommend us to friends and family.")

#calling the first function and storing the value it returns into the variable "srvrName" and giving it the argument of the list with the users and IDs.

srvrName = checkNameandID(authUsers)

#Calling the second function and storing the integers that it returns into the variables "tableNumber" and "numPeople"

tableNumber, numPeople = getTableInfo()

#calling the third function and giving it the 2 arguments of the lists that contain the ice cream flavours and the choice of toppings.

printMenu(iceCream, toppingChoice)

#Calls the forth function, giving it as an argument the variable numPeople that was saved from a previous function as well as the two dictionaries with flavours and toppings.

order = getOrder(numPeople, iceCream, toppingChoice)

#Calls the last function and gives it an argument the variable "tableNumber", which again, was saved from a previous function and the variable "srvrName" which was also from a previous function.
#and I also gave it as an argument the list "order" that contains the dictionaries with the orders.

generateReceipt(tableNumber, order, srvrName)