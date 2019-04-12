import numpy as np
from src.dictionary import *


class Child:
    def __init__(self, tacts_number, scale):
        self.tacts_number = tacts_number
        self.scale = scale

        self.melody = []

        self.create_melody()

    def create_melody(self):
        for i in range(self.tacts_number):
            time = 0
            help_list = []
            # tworzenie poszczególnych taktów
            while time <= 2:
                if i != 0:
                    pitch = np.random.choice(self.scale)
                else:
                    pitch = self.scale[7]
                duration = np.random.choice(duration_dict)
                time = time + duration
                if time == 1:
                    help_list.append([pitch, duration])
                    break
                elif time > 1:
                    time = time - duration
                    continue
                elif time < 1:
                    help_list.append([pitch, duration])

            self.melody.append(help_list)
        self.melody.append([[128, 2]])
