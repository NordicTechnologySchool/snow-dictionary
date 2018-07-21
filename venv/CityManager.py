def createDistrictCityDict():
    return {
        'HRJU':['Tallinn', 'Harku', 'Keila'],
        'SAAR': ['Kardla', 'Suurvete', 'Maasikas']
    }

def getCitiesOfFrom(searchKey, dict):
    return dict[searchKey][-1]

def searchDistrictThatHasCity(searchCity, dict):
    # WARN: Double for loops!
    for key  in dict:
        for city in dict[key]:
            if(city==searchCity):
                return key

def addCityToDistrict(city, distCode, dict):
    # cities = dict[distCode]   # Note: this will throw "key error" if key is not found, use this to check for key instead:
    cities = dict.get(distCode, None)

    if not(cities is None):
        if(city not in cities):
            cities.append(city)
            print("Success | Added city {} to district {} ".format(city, distCode))
        else:
            print("Notice! | City {} already in list".format(city))
    else:
        print("Error! | Cannot add city {}, district {} not found".format(city, distCode))