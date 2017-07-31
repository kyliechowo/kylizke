groceries = []
#groceryList = ["cheese","milk","cereal","granola","juice"]
#for x in groceryList:
    #print(x)


#Interactive Grocery List

while True:
    print("Would you like to add an item to your list?(y/n)")
    answer = input()
    if  answer == "y":
        print("What would you like to add?")
        answer = input()
        groceries.append(answer)
    if answer == "n":
        print("Ok")
        print (groceries)
        break

   
    
