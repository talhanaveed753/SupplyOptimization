###########################################################################
# Talha Naveed
# Project 1 Phase 1
###########################################################################

def loadData(cityList, coordList, popList, distanceList):

    # Required to initialize elements for distanceList
    readingDistances = False  # Keep track of whether we're currently reading a line of distances

    # Open the file and skip the first 4 lines of info
    f = open("miles.dat")
    f.readline()
    f.readline()
    f.readline()
    f.readline()

    for line in f:

        # Check to see if the first char on line in f is a capital letter
        if ("A" <= line[0]) and (line[0] <= "Z"):

            # Create cityList --> (cityName, statName)
            i = 0
            while (line[i] != ","):
                   i = i + 1

            cityName = line[:i]
            stateName = line[i + 2:i + 4]

            cityList.append(cityName + " " + stateName)

            # Create coordList --> (lattitude, longitude)
            firstBracket = str.find(line, "[")
            comma = str.rfind(line,",")
            secondBracket = str.rfind(line,"]")

            lattitude = int(line[firstBracket + 1:comma])
            longitude = int(line[comma + 1:secondBracket])

            cityCoordList = [lattitude, longitude]

            coordList.append(cityCoordList)

            # Create popList --> (cityPop)
            endLine = str.find(line, "\n")
            cityPop = int(line[secondBracket + 1:endLine])

            popList.append(cityPop)

            # Initialize distanceList with an emptyList for first city
            distanceList.append([])

            # change bool to false
            readingDistances = False

        # determine if the current line is city distances or not
        elif all(c.isspace() or c.isdigit() for c in line):
            
            distances = [int(x) for x in line.split()]  # Convert all string numbers to type int
            
            if not readingDistances:
                
                distanceList[-1] = distances  # Replace the last element in distanceList with distances
                readingDistances = True
                
            else:
                distanceList[-1] += distances  # Append the distances to the last element in distanceList
                
    # Reverse the list to meet function specification
    for i in range(len(distanceList)):
        distanceList[i] = list(reversed(distanceList[i]))

def getCoordinates(cityList, coordList, name):

    # Get the index of the named city in cityList
    i = cityList.index(name)
    return coordList[i]

def getPopulation(cityList, popList, name):

    # Get the index of the named city in cityList
    i = cityList.index(name)
    return popList[i]

def getDistance(cityList, distanceList, name1, name2):

    # Get the index of the name1 city in cityList
    i = cityList.index(name1)

    # Get the index of the named city in cityList
    j = cityList.index(name2)

    # Check to see which city comes first and get distances accordingly
    if (i > j):
        return distanceList[i][j]
    elif (j > i):
        return distanceList[j][i]
    elif (i == j):
        return 0

def nearbyCities(cityList, distanceList, name, r):

    # The list result will eventually contain the names of cities
    # at distance <= r from name
    result = []

    # Get the index of the named city in cityList
    i = cityList.index(name)

    # Walk down the distances between the named city and previous cities
    j = 0
    for d in distanceList[i]:      # For every other previous city
        if d <= r:      # If within r of named city
            result = result + [cityList[j]]    # Add to result
        j = j + 1

    # Walk down the distances between the named city and later cities
    j = j + 1
    while (j < len(distanceList)):  # For every other previous city
        if distanceList[j][i] <= r: # If within r of named city
            result = result + [cityList[j]] # Add to result

        j = j + 1

    return result
