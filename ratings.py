# from pprint import pprint

INSTRUCTIONS = """ 
[S]eeing all restaurant ratings
[A]dding new restaurant ratings
[Q]uit app
"""

filename = open("scores.txt")


def print_restaurants(rest_dict):

    rest_sorted = (sorted(rest_dict.items()))

    for restr, rating in rest_sorted:
        print(f' {restr} is rated at {rating}.')


def add_ratings(rest_dict):

    rest_name = input("Give me the restaurant name: ")
    rest_rating = input("Give me the restaurant rating: ")

    while True:
        if not rest_rating.isdigit():
            rest_rating = input("Invalid rating, please try again: ") 
        else:
            while not 0 < int(rest_rating) < 6:
                rest_rating = input("Invalid rating, please try again: ")
            break
 

    rest_dict[rest_name] = rest_rating
    return rest_dict

    # pprint(rest_sorted)


def get_user_options(file):

    restaurants = {}

    for line in file:
        restaurant_data = line.rstrip().split(":")
        restaurants[restaurant_data[0]] = restaurant_data[1]

    while True:
        print(INSTRUCTIONS)
        user_choice = input("What would you like to do? ")
        user_choice = user_choice.upper()
        
        if user_choice == "S":
            print_restaurants(restaurants)
        elif user_choice == "A":
            restaurants = add_ratings(restaurants)
        elif user_choice == "Q":
            break
        else:
            print("invalid response: do better!!!!")


get_user_options(filename)