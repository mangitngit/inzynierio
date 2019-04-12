from src.evaluation import *


def calc(melody):
    straight_line = []

    intervals_variety_dict = intervals_data[0]
    intervals_mean_dict = intervals_data[1]
    intervals_value_weight_dict = intervals_mean_dict

    rhytm_variety_dict = rhytm_data[0]
    rhytm_mean_dict = rhytm_data[1]
    rhytm_value_weight_dict = rhytm_mean_dict

    tone_deviation_dict = others_data[0]
    break_value_dict = others_data[1]

    intervals = [0 for i in range(14)]  # interwały, poszczególne liczba występowania
    intervals_variety = 0  # różnorodność interwałów
    intervals_mean = 0     # średnia interwałów

    interval_mean_denominator = 0
    interval_mean_numerator = 0

    rhytms = [0 for i in range(4)]  # długości dźwięków
    rhytms_variety = 0      # różnorodnośc dźwięków
    rhytm_mean = 0      # średnia długośći

    rhytm_mean_denominator = 0
    rhytm_mean_numerator = 0

    tone_mean = 0
    tone_deviation = 1

    tone_mean_denominator = 0

    break_value = 1     # liczba przerw

    rate_intervals_value = 0
    rate_intervals_variety = 0
    rate_intervals_mean = 0

    rate_rhytm_value = 0
    rate_rhytm_variety = 0
    rate_rhytm_mean = 0

    rate_tone_deviation = 0
    rate_break = 0

    for tact in melody: # wczytanie melodii
        for note in tact:
            straight_line.append(note)
    for i in range(len(straight_line)-1):
        interval_value = abs(straight_line[i][0] - straight_line[i+1][0])   # interwał

        if interval_value > 13:     # przypisanie iinterwałów
            intervals[13] += 1
        else:
            intervals[interval_value] += 1
            if interval_value != 0:
                interval_mean_denominator += interval_value   # zmienne pomocnicze do średniej
                interval_mean_numerator += 1

        if straight_line[i][0] != 128:
            if straight_line[i][1] == 1:
                rhytms[0] += 1
                rhytm_mean_denominator += 0
            elif straight_line[i][1] == 0.5:
                rhytms[1] += 1
                rhytm_mean_denominator += 1
            elif straight_line[i][1] == 0.25:
                rhytms[2] += 1
                rhytm_mean_denominator += 2
            elif straight_line[i][1] == 0.125:
                rhytms[3] += 1
                rhytm_mean_denominator += 3

            tone_mean += abs(straight_line[i][0] - straight_line[0][0])
            rhytm_mean_numerator += 1
        else:
            break_value += 1

    intervals_variety = 13 - intervals.count(0)
    if interval_mean_numerator != 0:
        intervals_mean = interval_mean_denominator / interval_mean_numerator

    rhytms_variety = 4 - rhytms.count(0)

    if rhytm_mean_numerator != 0:
        rhytm_mean = rhytm_mean_denominator / rhytm_mean_numerator
        tone_deviation = tone_mean/rhytm_mean_numerator + 1

    helper_interval = 0
    helper_interval_numerator = 0
    for i in range(len(intervals)):
        if intervals[i] != 0:
            helper_interval += intervals[i]*intervals_value_dict[i]
            helper_interval_numerator += intervals[i]

    helper_rhytm = 0
    helper_rhytm_numerator = 0
    for i in range(len(rhytms)):
        if rhytms[i] != 0:
            helper_rhytm += rhytms[i] * rhytm_value_dict[i]
            helper_rhytm_numerator += rhytms[i]

    rate_intervals_value = intervals_value_weight_dict*(helper_interval/helper_interval_numerator)
    if intervals_variety != 0:
        rate_intervals_variety = intervals_variety_dict/intervals_variety
    if intervals_mean != 0:
        rate_intervals_mean = intervals_mean_dict*intervals_value_dict[round(intervals_mean)]

    rate_rhytm_value = rhytm_value_weight_dict*(helper_rhytm/helper_rhytm_numerator)
    if rhytms_variety != 0:
        rate_rhytm_variety = rhytm_variety_dict/rhytms_variety
    rate_rhytm_mean = rhytm_mean_dict*rhytm_value_dict[round(rhytm_mean)]

    if tone_deviation != 0:
        rate_tone_deviation = tone_deviation_dict/tone_deviation
    if break_value != 0:
        rate_break = break_value_dict/break_value

    information = ("Średnia ważona interwałów:           " + str(round(helper_interval / helper_interval_numerator, 3)) + # średnia z interwałów jak najlepsza
                   "\nŚrednia wartość interwałów:          " + str(round(intervals_value_dict[round(intervals_mean)], 3)) +   # średnia interwałów policzona
                   "\nRóżnorodność interwałów:             " + str(round(rate_intervals_variety / intervals_variety_dict, 3)) +  # różnorodność jak najmniejsza
                   "\nŚrednie odchylenie wysokości tonów:  " + str(round(rate_tone_deviation / tone_deviation_dict, 3)) +  # średnio ważne

                   "\nŚrednia ważona wartości rytmicznych: " + str(round(helper_rhytm / helper_rhytm_numerator, 3)) + # średnia z nut nie ważna
                   "\nŚrednia z wartości rytmicznych:      " + str(round(rhytm_value_dict[round(rhytm_mean)], 3)) +   # średnia z nut nie ważna
                   "\nRóżnorodność rytmiczna:              " + str(round(rate_rhytm_variety / rhytm_variety_dict, 3)) +  # różnorodność ważna
                   "\nLiczba wystąpień pauz:               " + str(round(rate_break / break_value_dict, 3)) + "\n")  # jak najmniej

    rate_value = 100 * (rate_intervals_value + rate_intervals_variety + rate_intervals_mean + rate_rhytm_value +
                        rate_rhytm_variety + rate_rhytm_mean + rate_tone_deviation + rate_break) / \
                       (intervals_value_weight_dict + intervals_variety_dict + intervals_mean_dict +
                        rhytm_value_weight_dict + rhytm_variety_dict + rhytm_mean_dict + tone_deviation_dict +
                        break_value_dict)

    return rate_value, information
