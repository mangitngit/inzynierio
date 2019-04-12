import numpy as np


def mutation(melody, scale, tacts_number):
    choose_tact = np.random.choice(tacts_number)
    if np.random.choice([0, 1], p=[0.15, 0.85]):
        for note in melody[choose_tact]:
            note[0] = np.random.choice(scale[0:-1])
    else:
        note = np.random.randint(0, len(melody[choose_tact]))
        if choose_tact + note == 0:
            pass
        else:
            melody[choose_tact][note][0] = 128

    return melody
