from genetic_algorithm.child import *
from genetic_algorithm.rating import *
from genetic_algorithm.crossing import *
from genetic_algorithm.mutation import *
from genetic_algorithm.roulette import *
from src.dictionary import *
from src.saveMidi import *
from src.saveTab import *
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches


class GeneticAlgorithm:
    def __init__(self):
        self.iterations = 250
        self.tacts_number = 8
        self.mutation_probability = 0.1
        self.crossing_probability = 0.8
        self.tempo = 60
        self.scale_type = 1
        self.tone = 57
        self.instrument = 0
        self.background = 0
        self.crossing_type = 1
        self.file_path = "music/compose"
        self.population = 3

        self.cross_two_line_arg = []
        self.scale = []
        self.generation = []
        self.next_generation = []
        self.melody = []
        self.group_of_melody = []
        self.valuation = []
        self.valuation_probability = []
        self.melody_to_tab = []
        self.victory_melody = []
        self.save = None

        self.plot_y_max = []
        self.plot_y_mean = []

        self.final_music_argument = []
        self.final_music_value = 0

        self.max_rate = 0
        self.medium_rate = 0

        self.tonika = []
        self.subdominata = []
        self.dominata = []

        self.checkbox = 1

    def start(self, iterations, tacts_number, crossing_probability, mutation_probability, tempo, scale_type, tone,
              instrument, backgroud, crossing_type, file_path, population, checkbox):

        # W niektórych przypadkach zamiana z krotki do wartości
        self.iterations = iterations
        self.tacts_number = tacts_number,
        for item in self.tacts_number:
            self.tacts_number = item
        self.crossing_probability = crossing_probability,
        for item in self.crossing_probability:
            self.crossing_probability = item
        self.mutation_probability = mutation_probability,
        for item in self.mutation_probability:
            self.mutation_probability = item
        self.tempo = tempo,
        for item in self.tempo:
            self.tempo = item
        self.scale_type = scale_type,
        for item in self.scale_type:
            self.scale_type = item
        self.tone = tone,
        for item in self.tone:
            self.tone = item
        self.instrument = instrument
        self.background = backgroud
        self.crossing_type = crossing_type
        self.file_path = file_path
        self.population = population
        self.checkbox = checkbox

        # Wybór skali
        if self.scale_type == 1:
            self.scale = [item + self.tone for item in major_scale]
        elif self.scale_type == 2:
            self.scale = [item + self.tone for item in minor_scale]
        elif self.scale_type == 3:
            self.scale = chromatic_scale

        # wygenerowanie triady charmonicznej do danego typu skali
        self.tonika = [self.scale[0]-12, self.scale[2]-12, self.scale[4]-12]
        self.subdominata = [self.scale[3]-12, self.scale[5]-12, self.scale[7]-12]
        self.dominata = [self.scale[4]-12, self.scale[6]-12, self.scale[8]-12]

        # Wartość 128 jako przerwa
        self.scale.append(128)

    # początek działania algorytmu
    def run(self):

        # przypisanie do tablicy gorup_of_melody wszystkich wygenerowanych linii melodyczbych
        for child in range(self.population):
            self.generation.append(Child(self.tacts_number, self.scale))
        for child in self.generation:
            self.group_of_melody.append(child.melody)

        self.plot_y_max = []
        self.plot_y_mean = []

        for iteration in range(self.iterations):
            self.next_generation = []
            self.valuation_probability = []

            # ocena wszystkich linii melodycznych
            self.valuation, self.valuation_probability, self.max_rate, self.medium_rate, self.final_music_argument, \
            self.final_music_value = rating_music(self.group_of_melody.copy(), self.final_music_argument,
                                                  self.final_music_value)
            self.plot_y_max.append(self.max_rate)
            self.plot_y_mean.append(self.medium_rate)

            for sub_iteration in range(self.population):
                self.melody = []

                # wybranie dwóch najlepiej przystosowanych osobników z zadanym prawdopodobieństwem
                self.cross_two_line_arg = []
                self.cross_two_line_arg = chosen_two(self.valuation_probability.copy())

                # krzyżowanie
                flag = np.random.choice([0, 1], p=[(1 - self.crossing_probability), self.crossing_probability])
                if flag:
                    self.melody = crossing(self.group_of_melody[self.cross_two_line_arg[0]].copy(),
                                           self.group_of_melody[self.cross_two_line_arg[1]].copy(), self.crossing_type)
                else:
                    x = np.random.choice(len(self.group_of_melody))
                    self.melody = self.group_of_melody[x].copy()

                # mutacja
                flag = np.random.choice([0, 1], p=[(1 - self.mutation_probability), self.mutation_probability])
                if flag:
                    self.melody = mutation(self.melody.copy(), self.scale, self.tacts_number).copy()

                # przypisanie do następnej generacji przetworzonej melodii
                self.next_generation.append(self.melody.copy())

            # zastąpienie starej generacji nową
            self.group_of_melody = self.next_generation.copy()

        # dodanie podkłądu do stworzonej linii
        back = []
        chord_progression = [self.tonika, self.subdominata, self.dominata]
        for chord in range(self.tacts_number):
            if chord % 2 == 0:
                back.append(chord_progression[int(chord/2) % 3])
        back.append(self.tonika)

        # zapisanie wytworzonej muzyki
        self.save = SaveMIDI(self.tempo, self.instrument, self.background, self.file_path)
        self.save.write_midi(self.final_music_argument)
        self.save.write_background(back)

        self.save.save_midi()

        # zapisywanie tabulatury
        for tact in self.final_music_argument:
            for note in tact:
                self.melody_to_tab.append(note)

        save_tab(self.melody_to_tab, self.file_path)

        # czyszczenie tablic
        self.scale = []
        self.generation = []
        self.next_generation = []
        self.melody = []
        self.group_of_melody = []
        self.valuation = []
        self.valuation_probability = []
        self.melody_to_tab = []
        self.victory_melody = []
        self.final_music_value = 0
        self.final_music_argument = []

        # wyświetlenie danych statystycznych
        if self.checkbox:
            plt.figure(1)
            plt.plot([x for x in range(self.iterations)], self.plot_y_max, 'r',
                     [x for x in range(self.iterations)], self.plot_y_mean, 'b')
            plt.title('Oceny utworów z funkcji przystosowania')
            plt.xlabel('Generacja')
            plt.ylabel('Ocena')
            red_patch = mpatches.Patch(color='red', label='Maksimum')
            blue_patch = mpatches.Patch(color='blue', label='Średnia')
            plt.legend(handles=[red_patch, blue_patch])

        print("Done")
