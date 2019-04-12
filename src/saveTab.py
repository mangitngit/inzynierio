tab = {
    52: "0-----",
    53: "1-----",
    54: "2-----",
    55: "3-----",
    56: "4-----",
    57: "-0----",
    58: "-1----",
    59: "-2----",
    60: "-3----",
    61: "-4----",
    62: "--0---",
    63: "--1---",
    64: "--2---",
    65: "--3---",
    66: "--4---",
    67: "---0--",
    68: "---1--",
    69: "---2--",
    70: "---3--",
    71: "----0-",
    72: "----1-",
    73: "----2-",
    74: "----3-",
    75: "----4-",
    76: "-----0",
    77: "-----1",
    78: "-----2",
    79: "-----3",
    80: "-----4",
    81: "-----5",
    82: "-----6",
    83: "-----7",
    84: "-----8",
    85: "-----9",
    128: "--||--"
}

other = "??????"


def save_tab(melody, txt_file_path):
    file = open(txt_file_path+".txt", "w")
    E1 = " e |-"
    B = " B |-"
    G = " G |-"
    D = " D |-"
    A = " A |-"
    E = " E |-"

    time_takt = 0
    time_melody = 0
    for note in melody:
        if (note[0] > 85 and note[0] != 128) or note[0] < 52:
            E += other[0]
            A += other[1]
            D += other[2]
            G += other[3]
            B += other[4]
            E1 += other[5]
        else:
            E += tab[note[0]][0]
            A += tab[note[0]][1]
            D += tab[note[0]][2]
            G += tab[note[0]][3]
            B += tab[note[0]][4]
            E1 += tab[note[0]][5]

        if note[1] == 1:
            E += "---------------"
            A += "---------------"
            D += "---------------"
            G += "---------------"
            B += "---------------"
            E1 += "---------------"
        elif note[1] == 0.5:
            E += "-------"
            A += "-------"
            D += "-------"
            G += "-------"
            B += "-------"
            E1 += "-------"
        elif note[1] == 0.25:
            E += "---"
            A += "---"
            D += "---"
            G += "---"
            B += "---"
            E1 += "---"
        elif note[1] == 0.125:
            E += "-"
            A += "-"
            D += "-"
            G += "-"
            B += "-"
            E1 += "-"

        time_takt += note[1]
        time_melody += note[1]
        if time_takt == 1:
            if time_melody == 4:
                time_melody = 0
                time_takt = 0

                file.write(E1 + "-|\n")
                file.write(B + "-|\n")
                file.write(G + "-|\n")
                file.write(D + "-|\n")
                file.write(A + "-|\n")
                file.write(E + "-|\n")
                file.write("\n\n")

                E1 = " e |-"
                B = " B |-"
                G = " G |-"
                D = " D |-"
                A = " A |-"
                E = " E |-"

            else:
                time_takt = 0
                E += "|-"
                A += "|-"
                D += "|-"
                G += "|-"
                B += "|-"
                E1 += "|-"

    file.write(E1 + "-|\n")
    file.write(B + "-|\n")
    file.write(G + "-|\n")
    file.write(D + "-|\n")
    file.write(A + "-|\n")
    file.write(E + "-|\n")

    file.close()
