# from pprint import pprint

filename = open("scores.txt")


def get_restaurant_ratings(file):

    restaurants = {}

    for line in file:
        restaurant_data = line.rstrip().split(":")
        restaurants[restaurant_data[0]] = restaurant_data[1]
    
    rest_sorted = (sorted(restaurants.items()))

    for restr, rating in rest_sorted:
        print(f' {restr} is rated at {rating}.')

    # pprint(rest_sorted)


get_restaurant_ratings(filename)
