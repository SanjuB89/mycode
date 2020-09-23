import requests

def main():
    # create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    result = r.json()
    print(r.json())
   # print("People in space: " + str(result.get("number")))

    #print(result["people"][0]["name"] + " on the " + result["people"][0]["craft"])
    #print(result["people"][1]["name"] + " on the " + result["people"][1]["craft"])
    #print(result["people"][2]["name"] + " on the " + result["people"][2]["craft"])
    
    print("\n\n\n\n")
    print("People in space: " + str(result.get("number")))
    for element in result["people"]:
        print(f"{element['name']} on the {element['craft']}")


main()
