# Define the data structure for attractions
class Attraction:
    def __init__(self, name: str, country: str) -> None: 
        self.name = name
        self.country = country

#Read File
def read_attractions():
    attractions = []
    with open("7location.txt", "r") as file:
        for line in file:
            name, country = line.strip().split(",")
            attraction = Attraction(name, country)
            attractions.append(attraction)
    return attractions

# Create a list of attractions
attractions = read_attractions()

# show up
while True:
    print("Menu items:")
    print("1. List of attractions (Like right now)")
    print("2. Show all Counntries have in text")
    print("3. Show all  every City have in text")
    print("0. Close")
    choice = input("Choose the number/or name of City/Country ")

    if choice == "1":
        #list
        for attraction in attractions:
            print(attraction.name)

    elif choice == "2":
        # countries and list of attractions
        country_set = set(attraction.country for attraction in attractions)
        for i, country in enumerate(country_set):
            print(f"{i+1}. {country}")

        #country
        choice = input("What you choose: ")
        country_chosen = list(country_set)[int(choice.strip())-1]



        #Print  country
        for attraction in attractions:
            if attraction.country == country_chosen:
                print(attraction.name)

    elif choice == "3":
        # cities and list of attractions
        city_set = set(attraction.name for attraction in attractions)
        for i, city in enumerate(city_set):
            print(f"{i+1}. {city}")

        # Ask the user to select a city
        choice = input("What you choose: ")
        city_chosen = list(city_set)[int(choice)-1]

        # Print the names of attractions and the name of the country for the chosen city
        for attraction in attractions:
            if attraction.name == city_chosen:
                print(f"{attraction.name}, {attraction.country}")

    elif choice == "0":
        break

    else:
        print("ONLY between 1-3!!!!")
