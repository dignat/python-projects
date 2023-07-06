import emoji

def addToInventory(direction, inventory):
 coin = emoji.emojize(":coin:")
 directionToLower = direction.lower()
 if (directionToLower == "n" or directionToLower == 'w'):
     inventory.append(coin)
 return inventory


def printInventory(inventory):
 print(inventory)
 
def game():
  yes_no = ["yes", "no"]
  directions = ["n", "w", "e" "s"]
  inventory = []
  #Intro
  name = input("What is your name adventurer?\n")
    
  print("Greetings brave " + name + ". Lets begin\n")
  print("You would need tomake choices, let's see where they lead you.")
  print("Can you find your way and collect coins?")
    
    #start
  response = ""
  while response not in yes_no:
    response = input("Would like to start your journey?\n".lower())
    if response == "yes":
        print("We will need to fill up your car with gas.")
        #print your car
    elif response == "no":
        print("You are not ready for this advneture. Goodbye" + name + "!")
        quit()
    else:
        print("I did not understand.\n")
            
            
    #second part
  response = ""
  while response not in directions:
    print("You are the gas staion. You have two choises.\n You can get s(w)shi or ask for the bathroom(e) keys.")
    response = input("What you do?\n".lower())
    if response == "w":
        print("Sushi")
        addToInventory(response, inventory)
        printInventory(inventory)
    else:
        exit

 

 

    
    
    
        
 
game()


    
