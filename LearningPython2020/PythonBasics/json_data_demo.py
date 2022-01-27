# ----------------------------------
# Demo with JSON data in Python 
# ----------------------------------
# displaying data from nested JSON format 

import json 

def main():

    # opening the json file 
    data_filepath = 'data/donutData.json'
    file = open(data_filepath) 
    
    # returns json object as dictionary 
    data = json.loads(file.read())

    # print the name of each donut type 
    print("Donut Types: ")
    for donut in data:
        print(donut['name'])
    print("----------------------")

    # print the type of each topping for cake donuts
    print("Cake Donut Toppings: ")
    for donut in data: 
        if donut["name"] == "Cake":
            for topping in donut["topping"]:
                print(topping["type"])
    print("----------------------")

    # print the types of batters for old fashioned donuts 
    print("Old Fashioned Donut Batters: ")
    for donut in data: 
        if donut["name"] == "Old Fashioned": 
            for batter in donut["batters"]["batter"]:
                print(batter["type"])

    file.close()
    return 

if __name__ == "__main__":
    main()