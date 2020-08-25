#Assigment 2 - exercise 1

#Function that creates a tuple from a line in a file
def stringtotuple(player): 
    x=player.split()
    return tuple(x)

#Function that prints a display of players in a neat way using fixed width fields
def printdetails(player):
    print("{:<15}, {:<15} {:<8} {:<15} {:<15}".format(player[3],player[2],player[4],player[1],player[0]))
    return player

#Trying to open a file    
inFile=input("Specify a name of a file you want to open: ") #Lets the user to enter the file name
try:
    fileIn=open(inFile,'r')
    
#Prints a message of error if the file cannot be found
except IOError as e:
    fileIn=None
    print("Failed to open", inFile, "- program aborted")

if fileIn!=None: #A notation needed, after an try function, in order for the program to work
    
#Makes a list of all players
    listOfPlayers=[]
    for line in fileIn:
       listOfPlayers.append(stringtotuple(line))
    fileIn.close()
    
#Prints a neat list
    for each in listOfPlayers:
        printdetails(each)
        
    opt=0  #the start point of an option value

    #Entering an options loop
    while(opt!=4):
        
        #Options
        print('Options:')
        print('Type 1 for full details of the player with a given last-name')
        print('Type 2 for full details of the player with a salary in particular range')
        print('Type 3 for the first- and last- names of all players of a team')
        print('Type 4 to quit the options')
        opt=int(input("Enter a number:")) #Asks user to enter an option number
        
        #Option 1
        if(opt==1):
            print('Option 1, full details of the player with a given last-name')
            #Asks user to enter a last name, and uppers the first letter to match the list
            lastname=input('Enter the last-name:').title()
            #Introducing the counter, in order to later check if there are any results
            counter=0
            #Checks if the lastname is in a list: if so prints details of a player, if not counter rises by one
            for each in listOfPlayers:
                if (lastname in each):
                    printdetails(each)
                else:
                    counter=counter+1
            #Checks if there any  results, if not prints a meesage
            if(counter==len(listOfPlayers)):
                print("No results found")
    
        #Option 2
        elif(opt==2):
            print('Option 2, full details of the player with a salary in particular range')
            #Asks user to enter a lower and upper ranges of salary
            range1=int(input("Enter lower range  of a salary in numbers:"))
            range2=int(input("Enter upper range of a salary in numbers:"))
            #Introducing the  counter
            counter=0
            for each in listOfPlayers:
                #Checks if the salary is in range: if so prints details of a player, if not counter rises by one
                if (int(''.join(each[4].split(','))) in range(range1,range2+1)):
                    printdetails(each)
                else:
                    counter=counter+1
            #Checks if there any  results, if not prints a meesage
            if(counter==len(listOfPlayers)):
                print("No results found")

        #Option 3
        elif(opt==3):
            print('Option 3, the first- and last- names of all players of a team')
            #Asks user to enter a team name, and uppers the first letter to match the list
            team=input("Enter a team name:").title()
            #Prints the team name
            print(team,":")
            #Introducing the counter
            counter=0
            #Checks if there are any players in a list: if so prints last,first names of a player, if not counter rises by one
            for each in listOfPlayers:
                if(team in each):
                    print("{:<15}{:<15}".format(each[2],each[3]))
                else:
                    counter=counter+1
            #Checks if there any  results, if not prints a meesage
            if(counter==len(listOfPlayers)):
                print("No results found")
                
    ""  
    else:
        print("You quit the options")
        
    #Asks the user to supply the position and the  team name and uppers the first letters
    position=input("Supply the position:").title()
    team=input("Supply the team name:").title()
    #Introucing the counter
    counter=0
    #Checks if there are  any matching results: if yes prints the details  of a player, if not counter rises by one
    for each in listOfPlayers:
        if(position in each)and(team in each):
            printdetails(each)
        else:
            counter=counter+1
    #Checks if there any  results, if not prints a meesage
    if(counter==len(listOfPlayers)):
        print("Player not found")
        
    #Asks the user to supply the position and the ranges of salary  and uppers the first letter of the position
    pos=input("Supply the position:").title()
    rang1=int(input("Enter lower range  of a salary in numbers:"))
    rang2=int(input("Enter upper range of a salary in numbers:"))
    #Sorts the list depending on the salary
    sorted(listOfPlayers, key = lambda x: int(''.join(x[4].split(','))))
    #Introducing the counter
    counter=0
    #Checks if there are  any matching results: if yes prints the details  of a player, if not counter rises by one
    for each in listOfPlayers:
        if(pos in each)and(int(''.join(each[4].split(','))) in range(rang1,rang2+1)):
                      printdetails(each)
        else:
            counter=counter+1
    #Checks if there any  results, if not prints a meesage
    if(counter==len(listOfPlayers)):
        print("Player not found")

#End of program
                      
