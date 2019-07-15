# from pprint import pprint

filename = open("scores.txt")


def print_restaurants(rest_dict):

    rest_sorted = (sorted(rest_dict.items()))

    for restr, rating in rest_sorted:
        print(f' {restr} is rated at {rating}.')



def get_restaurant_ratings(file):

    restaurants = {}

    for line in file:
        restaurant_data = line.rstrip().split(":")
        restaurants[restaurant_data[0]] = restaurant_data[1]

    print_restaurants(restaurants)

    rest_name = input("Give me the restaurant name: ")
    rest_rating = input("Give me the restaurant rating: ")   

    restaurants[rest_name] = rest_rating

    print_restaurants(restaurants)

    # pprint(rest_sorted)

get_restaurant_ratings(filename)
