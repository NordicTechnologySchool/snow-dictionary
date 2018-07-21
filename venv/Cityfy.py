import CityManager
import deleteme


if __name__ == '__main__':
    #distrcitCityDict =  CityManager.createDistrictCityDict()
    #cities = CityManager.getCitiesOfFrom('HRJU', distrcitCityDict)
    #district = CityManager.searchDistrictThatHasCity('Maasikas', distrcitCityDict)

    #CityManager.addCityToDistrict("Pärnu", "HRJU", distrcitCityDict)
    #CityManager.addCityToDistrict("Pärnu", "HRJU", distrcitCityDict)
    #CityManager.addCityToDistrict("Pärnu", "HRJUsdasd", distrcitCityDict)
    districtCityDict = {
        "JV": ["Jakarta", "Sumarekon", "Semarang", "Solo"],
        "BL": ["Denpasar", "Ubud"],
        "MONK": ["randomeCity", "someCity"]
    }
    city = deleteme.getLastCityNameOfDistrict("JV", districtCityDict)

    district = deleteme.getDistricCodeThatHasCity("Solo", districtCityDict)
    print(district)
    # >> "JV"


