from midiutil import MIDIFile


class SaveMIDI:
    def __init__(self, tempo, instrument, background, file_path):
        self.track = 0
        self.channel = 0
        self.channel2 = 1
        self.time = 0
        self.back_time = 0
        self.tempo = tempo
        self.volume = 100
        self.volume2 = 65
        self.instrument = instrument
        self.background = background
        self.file_path = file_path

        self.MyMIDI = MIDIFile(1, file_format=0)

        self.create_midi()

    def create_midi(self):
        self.MyMIDI.addTempo(self.track, self.time, self.tempo)
        self.MyMIDI.addProgramChange(self.track, self.channel, self.time, self.instrument)  # ustawienia linii melodycznej
        self.MyMIDI.addProgramChange(self.track, self.channel2, self.time, self.background) # ustawienia podkładu

    def save_midi(self):
        with open(self.file_path+".mid", "wb") as output_file:
            self.MyMIDI.writeFile(output_file)

    def write_midi(self, tacts):
        for notes in tacts:
            for note in notes:
                self.MyMIDI.addNote(self.track, self.channel, note[0], self.time, note[1], self.volume)
                self.time = self.time + note[1]

    def write_background(self, tacts):
            for notes in tacts:
                for note in notes:
                    self.MyMIDI.addNote(self.track, self.channel2, note, self.back_time, 2, self.volume2)
                self.back_time = self.back_time + 2