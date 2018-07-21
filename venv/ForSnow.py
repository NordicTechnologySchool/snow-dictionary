def getLastCityNameOfDistrict(district_code, dict):

    #1 - get all cities of a district
    cities = dict[district_code]
    #2 - return last city
    return cities[-1]


# Return a district code, that has the search_city in its city lis
def getDistricCodeThatHasCity(search_city, dict):
    # for loop thorugh all items
    # loop thorugh each items city list
    # if city == search_city
    #   return the key (district code)

    for key in dict:
        for city in dict[key]:
            if(city == search_city): return key










