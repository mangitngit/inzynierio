import numpy as np
from copy import deepcopy
from genetic_algorithm.calculator import *


def rating_music(list_of_melody, final_music_argument, final_music_value):
    valuation = []
    valuation_sum = 0
    oceny = []

    for melody in list_of_melody:
        rating_value, ad = calc(melody)
        valuation_sum += rating_value
        valuation.append(rating_value)
        oceny.append(deepcopy(ad))

    probal_valuation = [item/valuation_sum for item in valuation]

    max_rate = np.max(valuation)
    max_arg = np.argmax(valuation)
    medium_rate = valuation_sum/len(valuation)

    if max_rate > final_music_value:
        final_music_value = max_rate
        final_music_argument = deepcopy(list_of_melody[max_arg])
        print("Wartość funkcji przystosowania:      " + str(round(final_music_value, 3)) + "%")
        print(oceny[int(max_arg)])

    oceny.clear()

    return valuation, probal_valuation, max_rate, medium_rate, final_music_argument, final_music_value
