###############################################################################
#
# Specification: This "helper" function extracts the city name and state name
# from the given "city line" and returns these, concatenated in the correct
# format, as a single string.
#
###############################################################################
def extractCityStateNames(line):
    pieces = line.split(",")
    return pieces[0] + pieces[1][:3]

###############################################################################
#
# Specification: This "helper" function extracts the latitude and longitude
# from the given "city line" and returns these, in a size-2 list of integers.
#
###############################################################################
def extractCoordinates(line):
    pieces = line.split(",")
    return [int(pieces[1].split("[")[1]), int(pieces[2].split("]")[0])]


###############################################################################
#
# Specification: This "helper" function extracts the city population
# from the given "city line" and returns this an an integer.
# 
###############################################################################
def extractPopulation(line):
    pieces = line.split(",")
    return int(pieces[2].split("]")[1])

###############################################################################
#
# Specification: Reads information from the files "miles.dat" and loads the data
# structures cityList, coordList, popList, and distanceList with this information.
# Assumes that these 4 data structures are sent in empty.
# 
###############################################################################
def loadData(cityList, coordList, popList, distanceList):
    f = open("miles.dat")
    
    # Tracks which city we are currently processing
    cityIndex = 0
    
    # Keeps track of distances from current city to previous cities
    distances = []
    distanceList.append([])
    
    # Reads from the file, one line at a time
    for line in f:
        
        # Checks if the line is a "city line", i.e., contains information about
        # the city
        if line[0].isalpha():
            
            # Distances from the previous city need to be loaded into distanceList
            if distances != []:
                distanceList.append(distances[::-1])
                distances = []
                
            cityList.append(extractCityStateNames(line))
            coordList.append(extractCoordinates(line))
            popList.append(extractPopulation(line))
            cityIndex = cityIndex + 1
        
        # Checks if the line is a "distance line", i.e., contains information
        # distances from this city to previous cities            
        elif line[0].isdigit():
            distances.extend([int(x) for x in line.split()])
            
    # Distances from the previous city need to be loaded into distanceList
    if distances != []:
        distanceList.append(distances[::-1])

###############################################################################
#
# Specification: returns the coordinates (which is a list of 2 integers) of the 
# given city. It assumes that the given city name is in cityList.
#
###############################################################################
def getCoordinates(cityList, coordList, name):
    return coordList[cityList.index(name)]

###############################################################################
#
# Specification: returns the population (which is an integer) of the 
# given city. It assumes that the given city name is in cityList.
#
###############################################################################
def getPopulation(cityList, popList, name):
    return popList[cityList.index(name)]

###############################################################################
#
# Specification: returns the distance (an int) between cities name1 and name2. 
# If name1 and name2 are identical, return 0. It assumes that the given city names
# city1 and city2 are both in cityList.
#
###############################################################################    
def getDistance(cityList, distanceList, name1, name2):
    index1 = cityList.index(name1)
    index2 = cityList.index(name2)
    
    if index1 == index2:
        return 0
    elif index1 < index2:
        return distanceList[index2][index1]
    else:
        return distanceList[index1][index2]

###############################################################################
#
# Specification: The function takes 4 arguments:
#    
# cityList: is a list of strings, representing names of cities.
#
# distanceList: contains distances between pairs of cities in cityist. 
# distanceList has the same length as cityList and each element in distanceList
# is itself a list. Furthermore, distanceList[i] is a list of length i, where
# distanceList[i][j] (0 <= j <= i-1) represents the distance between cityList[i]
# and cityList[j] . 
#
# --------------
# EXAMPLE: cityList = ["X", "A", "B", "Z", "D"]
# distanceList = [[], [95], [170, 125], [150, 80, 225], [110, 175, 210, 120]]
#
# Then distanceList[2] represents the distances between city "B" and cities "X"
# and "A". More specifically, "X" is 170 miles from "B" and "A" is 125 miles from
# "B". 
#
# Note that distances between city "B" and cities "Z" and "D" appear in 
# distanceList[3][2] and distanceList[4][2] respectively. Thus the distance 
# between city "B" and "Z" is 225 and between city "B" and "D" is 210.
# --------------
# 
# name: is a name of a city; you can assume that name will be in cityList
#
# r: is a non-negative floating point number
#
# The function is required to return a list of cities at distance at most r
# from the city name. This list should contain names of cities in the same order
# as they appear in cityList.
#
# --------------
# EXAMPLE: cityList = ["X", "A", "B", "Z", "D"]
# distanceList = [[], [95], [170, 125], [150, 80, 225], [110, 175, 210, 120]]
#
# nearbyCities(cityList, distanceList, "B", 200) returns 
# ['X', 'A']
#
# nearbyCities(cityList, distanceList, "B", 210) returns
# ['X', 'A', 'D']
#
# nearbyCities(cityList, distanceList, "B", 500) returns
# ['X', 'A', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "X", 150) returns
# ['A', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "X", 0) returns
# []
#
# nearbyCities(cityList, distanceList, "X", 170) returns
# ['A', 'B', 'Z', 'D']
#
# nearbyCities(cityList, distanceList, "D", 170) returns
# ['X', 'Z']
#
# nearbyCities(cityList, distanceList, "D", 175.5) returns
# ['X', 'A', 'Z']
# 
###############################################################################

def nearbyCities(cityList, distanceList, name, r):

    # The list result will eventually contain the names of cities
    # at distance <= r from name
    result = []
    
    # Get the index of the named city in cityList
    i = cityList.index(name)           
    
    # Walk down the distances between the named city and previous cities
    j = 0
    for d in distanceList[i]:      # For every other previous city
        if d <= r :      # If within r of named city
            result = result + [cityList[j]]  # Add to result
        j = j + 1
        
    # Walk down the distances between the named city and later cities       
    j = i + 1
    while (j < len(distanceList)): # For every other previous city
        if distanceList[j][i] <= r: # If within r of named city
            result = result + [cityList[j]] # Add to result
            
        j = j + 1     

    return result

#################################################################################
#
# project1Phase 2 code
#
# defined 2 functions, the first one, locateFacilities, does all the assignment
# work, and the second one, unservedCities, finds the cities that have not been
# served by any facility in range yet
#
#################################################################################

def locateFacilities(cityList, distanceList, r):

    # initialze a bool list to represent cities served to all false, indicating that no
    # city has been served
    served = [False] * len(cityList)

    # initialize facilities to an empty string to keep track of least number of facilities
    # that serve the most cities
    facilities = []

    
    while not all(served):

        # determine which cities can serve the most other cities
        maxUnservedCount = -1
        facility = None

        # iterate through each individual city and determine how many unserved cities are
        # within its radius and compare it to find the city with the most and turn it into
        # a facility
        for city in cityList:
            
            unservedCount = numberOfUnservedCities(cityList, distanceList, served, city, r)

            if unservedCount > maxUnservedCount:
                
                maxUnservedCount = unservedCount
                facility = city
                
        # add the city to the facilities list
        facilities.append(facility)

        # go through served and convert the cities that are in range of facility to True
        for i in range(len(cityList)):
            
            city = cityList[i]
            
            if served[i] == False:
                
                if getDistance(cityList, distanceList, facility, city) <= r:
                    
                    served[i] = True

    return facilities

def numberOfUnservedCities(cityList, distanceList, served, city, r):

    # initialize variable "count" to keep track of the number of cities unserved
    count = 0

    # find the number of unserved cities in range r of city and store the value in count
    for i in range(len(cityList)):
        
        newCity = cityList[i]

        if served[i] == False:
            
            if getDistance(cityList, distanceList, city, newCity) <= r:
                
                count = count + 1

    return count
