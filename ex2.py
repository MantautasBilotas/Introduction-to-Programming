#Assigment 2 - exercise 2

#Importing math in order to count distance later
import math

#Function that creates a tuple from a line in a file
def stringtotuple(city):
    x=city.split()
    return tuple(x)

#Function that prints a display of cities in a neat way using fixed width fields
def printdetails(city):
    #Turns a number into a list with number with commas
    num=list(city[3])
    for element in range(-3,((len(num)*(-1)-1)),-4):
        num.insert(element,",")
    print("{:<30} n. citizens: {:<8}".format(city[0],str(''.join(num))))
    return city

#Function to calculate distance between two points using latitude(x) and longitude(y)
def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist

#Trying to open a file    
inFile=input("Specify a name of a file you want to open: ")
try:
    fileIn=open(inFile,'r')

#Prints a message of error if the file cannot be found
except IOError as e:
    fileIn=None
    print("Failed to open", inFile, "- program aborted")

if fileIn!=None:  #A notation needed, after an try function, in order for the program to work

#Makes a list of all cities
    citylist=[]
    for line in fileIn:
       citylist.append(stringtotuple(line))
    fileIn.close()

#Prints a neat list
    for each in citylist:
        printdetails(each)
    opt=0 #the start point of an option value

    #Entering an options loop
    while(opt!=4):
        #Options
        print('Options:')
        print('Type 1 for full details of the city with a given name')
        print('Type 2 for full details of the cities with a population in particular range')
        print('Type 3 for the cities within 10Km of the given cordinates')
        print('Type 4 to quit the options')
        opt=int(input("Enter a number:"))  #Asks user to enter an option number

        #Option 1
        if(opt==1):
            print('Option 1, full details of the city with a given name')
            #Asks user to enter a city name, and uppers the first letter to match the list
            name=input('Enter the name:').title() 
            #Introducing the counter, in order to later check if there are any results
            counter=0
            #Checks if the name is in a list: if so prints details of a city, if not counter rises by one
            for each in citylist:
                if (name in each):
                    printdetails(each)
                else:
                    counter=counter+1
            #Checks if there any  results, if not prints a meesage
            if(counter==len(citylist)):
                print("No results found")
                
        #Option 2
        elif(opt==2):
            print('Option 2, full details of the cities with a population in particular range')
            #Asks user to enter a lower and upper ranges of population
            pop1=int(input("Enter lower range  of a population in numbers:"))
            pop2=int(input("Enter upper range of a population in numbers:"))
            #Introducing the  counter
            counter=0
            for each in citylist:
                if (int(each[3]) in range(pop1,pop2+1)):
                    printdetails(each)
                else:
                    counter=counter+1
            #Checks if there any  results, if not prints a meesage
            if(counter==len(citylist)):
                print("No results found")
                
        #Option 3
        elif(opt==3):
            print('Option 3, the cities within 10Km of the given cordinates')
            #Asks the  user to enter latitude and longitude
            lat=int(input("Enter latitude in numbers:"))
            lon=int(input("Enter longitude in numbers:"))
            #Introducing the  counter
            counter=0
            for each in citylist:
                if(calculateDistance(lat,lon,int(each[1]),int(each[2]))<=10000):
                    print(each[0])
                else:
                    counter=counter+1
            #Checks if there any  results, if not prints a meesage
            if(counter==len(citylist)):
                print("No results found")

    #Prints the message thatthe user has  left the loop                
    else:
        print("You quit the options")

    #Asks the user to provide two names of the cities and uppers the first letters
    firstname=input("Enter the first name of a city:").title()
    secondname=input("Enter the second name of a city:").title()
    for each in citylist:
        if firstname in each:
            a=citylist.index(each) #a is index value
        elif secondname in each:
            b=citylist.index(each) #b is index value
    print("Distance:",round(calculateDistance(int(citylist[a][1]),int(citylist[a][2]),int(citylist[b][1]),int(citylist[b][2]))),"Km")

#End of program
