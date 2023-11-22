def readData():
    cityMPG = list() # Lists for storing data from 'carModelData_city' and 'carModelData_hwy'
    hwyMPG = list()
    
    infile = open("carModelData_city.txt", "r") # Saves data to list 'cityMPG'
    for line in infile.readlines():
        cityMPG.append(float(line))
    infile.close()
    
    infile = open("carModelData_hwy.txt", "r") # SAves data to list 'hwyMPG'
    for line in infile.readlines():
        hwyMPG.append(float(line))
    infile.close()

    carsTested = len(cityMPG) # Calculates quanitity of cars tested (Lists are equal in length, so its safe to equate this way)
    
    
    return cityMPG, hwyMPG, carsTested


def averageMPG(cityMPG, hwyMPG):
    # Calculate  the average mpg for all vehicles
    # tested given a list [from readData()].
    cityMPG_avg = sum(cityMPG) / len(cityMPG)
    hwyMPG_avg = sum(hwyMPG) / len(hwyMPG)
    
    return cityMPG_avg, hwyMPG_avg


def countGasGuzzlers(cityMPG, hwyMPG):
    # Calculate the number of gas guzzlers (defined as <22mpg/city or < 27mpg/highway)
    gasGuzzlers = list() # List which we used to store T/F values, letting us know which vehicles are gas guzzlers.
    gasGuzzlersCount = 0
    n = 0 # Used as an increment for counting gas guzzlers.

    for i in cityMPG: # Adds T/F values to the gasGuzzlers list by sorting through the cityMPG list, deciding if each is a gas guzzler or not.
        if i < 22:
            gasGuzzlers.append(True)
        else:
            gasGuzzlers.append(False)

    for i in hwyMPG: # Goes back through the gasGuzzlers list and changes F to T for vehicles that don't meet the designated values.
        
        if i < 27:
            gasGuzzlers[n] = True
        n = n + 1

    
    for i in gasGuzzlers: # Counts all T values in the gasGuzzlers list, resulting in the amount of gas guzzlers tested.
        if i == True:
            gasGuzzlersCount = gasGuzzlersCount + 1
    
    return gasGuzzlersCount



def output(carsTested, cityMPG_avg, hwyMPG_avg, gasGuzzlersCount):
    # Uses output from previous functions to print data
    # to the console.
    print(carsTested, " cars were tested.") # 1: Total number of vehicles tested.
    print("The average fuel economy of the vehicles tested is ", cityMPG_avg, " MPG in the city, and ", hwyMPG_avg, " MPG on the highway.") # 2: Avg. mpg in city, Avg. mpg on highway
    print("There were ", gasGuzzlersCount, " vehicles among those tested that perform lower than 22 MPG in the city or 27 MPG on the highway.") # 4: Number of gas guzzlers among tested vehicles
    


def Main():
    cityMPG, hwyMPG, carsTested = readData()
    cityMPG_avg, hwyMPG_avg = averageMPG(cityMPG, hwyMPG)
    gasGuzzlersCount = countGasGuzzlers(cityMPG, hwyMPG)
    
    output(carsTested, cityMPG_avg, hwyMPG_avg, gasGuzzlersCount)
    
    
Main()
