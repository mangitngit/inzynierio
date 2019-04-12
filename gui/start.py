import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from genetic_algorithm.algorithm import *


class StartScreen(QWidget):
    settingsClicked = pyqtSignal()

    def __init__(self):
        super(StartScreen, self).__init__()
        self.algorithm = GeneticAlgorithm()

        # Wartości komponowania
        self.iteration = 200
        self.tacts_number = 12
        self.crossing_probability = 0.95
        self.mutation_probability = 0.05
        self.population = 256
        self.tempo = 60
        self.scale_type = 1
        self.tone_of_scale = 57
        self.instrument_type = 0
        self.background_type = 0
        self.crossing_type = 1
        self.file_path = "music/compose"
        self.checkbox = 1

        # Wartości widgetów w gui
        self.iteration_minimum_value = 1
        self.iteration_maximum_value = 1000
        self.tacts_minimum_value = 4
        self.tacts_maximum_value = 32
        self.probability_minimum_value = 0
        self.probability_maximum_value = 1
        self.probability_step = 0.05
        self.population_minimum_value = 10
        self.population_maximum_value = 1024
        self.tempo_minimum_value = 30
        self.tempo_maximum_value = 240

        # Lewa kolumna widgetów
        self.settingsButton = QPushButton('Ustawienia', self)
        self.settingsButton.setGeometry(QRect(10, 360, 100, 35))
        self.settingsButton.clicked.connect(self.sett_clicked)

        self.playButton = QPushButton('Twórz', self)
        self.playButton.setGeometry(QRect(160, 360, 100, 35))
        self.playButton.clicked.connect(self.play_clicked)

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(QRect(320, 362, 280, 30))

        self.iterationQsb = QSpinBox(self)
        self.iterationQsb.move(10, 45)
        self.iterationQsb.resize(135, 20)
        self.iterationQsb.setMinimum(self.iteration_minimum_value)
        self.iterationQsb.setMaximum(self.iteration_maximum_value)
        self.iterationQsb.setValue(self.iteration)
        self.iterationQsb.valueChanged[int].connect(self.iteration_on_changed)

        self.tactsQsb = QSpinBox(self)
        self.tactsQsb.move(10, 105)
        self.tactsQsb.resize(135, 20)
        self.tactsQsb.setMinimum(self.tacts_minimum_value)
        self.tactsQsb.setMaximum(self.tacts_maximum_value)
        self.tactsQsb.setValue(self.tacts_number)
        self.tactsQsb.valueChanged[int].connect(self.tacts_on_changed)

        self.crossProbQdsb = QDoubleSpinBox(self)
        self.crossProbQdsb.move(10, 165)
        self.crossProbQdsb.resize(135, 20)
        self.crossProbQdsb.setSingleStep(self.probability_step)
        self.crossProbQdsb.setMinimum(self.probability_minimum_value)
        self.crossProbQdsb.setMaximum(self.probability_maximum_value)
        self.crossProbQdsb.setValue(self.crossing_probability)
        self.crossProbQdsb.valueChanged[float].connect(self.cross_prob_on_changed)

        self.mutationProbQdsb = QDoubleSpinBox(self)
        self.mutationProbQdsb.move(10, 225)
        self.mutationProbQdsb.resize(135, 20)
        self.mutationProbQdsb.setSingleStep(self.probability_step)
        self.mutationProbQdsb.setMinimum(self.probability_minimum_value)
        self.mutationProbQdsb.setMaximum(self.probability_maximum_value)
        self.mutationProbQdsb.setValue(self.mutation_probability)
        self.mutationProbQdsb.valueChanged[float].connect(self.mutation_prob_on_changed)

        self.crossTypeCombo = QComboBox(self)
        self.crossTypeCombo.addItem("jednopunktowy")
        self.crossTypeCombo.addItem("dwupunktowy")
        self.crossTypeCombo.addItem("trzypunktowy")
        self.crossTypeCombo.move(10, 285)
        self.crossTypeCombo.activated[str].connect(self.cross_type_combo_on_activated)

        self.cb = QCheckBox(' tak / nie ', self)
        self.cb.toggle()
        self.cb.move(80, 325)
        self.cb.stateChanged.connect(self.cb_changed)

        # Prawa kolumna widgetów
        self.populationQsb = QSpinBox(self)
        self.populationQsb.move(300, 45)
        self.populationQsb.resize(135, 20)
        self.populationQsb.setMinimum(self.population_minimum_value)
        self.populationQsb.setMaximum(self.population_maximum_value)
        self.populationQsb.setValue(self.population)
        self.populationQsb.valueChanged[int].connect(self.population_on_changed)

        self.tempoQsb = QSpinBox(self)
        self.tempoQsb.move(300, 105)
        self.tempoQsb.resize(135, 20)
        self.tempoQsb.setMinimum(self.tempo_minimum_value)
        self.tempoQsb.setMaximum(self.tempo_maximum_value)
        self.tempoQsb.setValue(self.tempo)
        self.tempoQsb.valueChanged[int].connect(self.tempo_on_changed)

        self.scaleCombo = QComboBox(self)
        self.scaleCombo.addItem("durowa")
        self.scaleCombo.addItem("molowa")
        self.scaleCombo.addItem("random")
        self.scaleCombo.move(300, 165)
        self.scaleCombo.activated[str].connect(self.scale_combo_on_activated)

        self.toneCombo = QComboBox(self)
        self.toneCombo.addItem("A")
        self.toneCombo.addItem("Ais")
        self.toneCombo.addItem("B")
        self.toneCombo.addItem("C")
        self.toneCombo.addItem("Cis")
        self.toneCombo.addItem("D")
        self.toneCombo.addItem("Dis")
        self.toneCombo.addItem("E")
        self.toneCombo.addItem("F")
        self.toneCombo.addItem("Fis")
        self.toneCombo.addItem("G")
        self.toneCombo.addItem("Gis")
        self.toneCombo.move(300, 225)
        self.toneCombo.activated[str].connect(self.tone_combo_on_activated)

        self.instruCombo = QComboBox(self)
        self.instruCombo.addItem("Acoustic Grand Piano")
        self.instruCombo.addItem("Bright Acoustic Piano")
        self.instruCombo.addItem("Electric Piano")
        self.instruCombo.addItem("Celesta")
        self.instruCombo.addItem("Music Box")
        self.instruCombo.addItem("Xylophone")
        self.instruCombo.addItem("Drawbar Organ")
        self.instruCombo.addItem("Church Organ")
        self.instruCombo.addItem("Acoustic Guitar")
        self.instruCombo.addItem("Overdriven Guitar")
        self.instruCombo.addItem("Distortion Guitar")
        self.instruCombo.addItem("Violin")
        self.instruCombo.addItem("Viola")
        self.instruCombo.addItem("Cello")
        self.instruCombo.addItem("Tremolo String")
        self.instruCombo.addItem("String Ansemble")
        self.instruCombo.addItem("String Ansemble Slow")
        self.instruCombo.addItem("Voice Oohs")
        self.instruCombo.addItem("Synthbrass")
        self.instruCombo.addItem("Piccolo")
        self.instruCombo.addItem("Pan Flute")
        self.instruCombo.addItem("Whistle")
        self.instruCombo.addItem("Bowed glass")
        self.instruCombo.addItem("Halo")
        self.instruCombo.addItem("Kalimba")
        self.instruCombo.addItem("Agogo")
        self.instruCombo.addItem("Bird Tweet")
        self.instruCombo.move(300, 285)
        self.instruCombo.activated[str].connect(self.instru_combo_on_activated)

        self.backgCombo = QComboBox(self)
        self.backgCombo.addItem("Acoustic Grand Piano")
        self.backgCombo.addItem("Electric Grand Piano")
        self.backgCombo.addItem("Drawbar Organ")
        self.backgCombo.addItem("Reed Organ")
        self.backgCombo.addItem("Viola")
        self.backgCombo.addItem("Cello")
        self.backgCombo.addItem("Contrabass")
        self.backgCombo.addItem("Tremolo String")
        self.backgCombo.addItem("SynthStrings")
        self.backgCombo.addItem("SynthStrings 2")
        self.backgCombo.addItem("Voice Oohs")
        self.backgCombo.addItem("Synth Voice")
        self.backgCombo.addItem("French Horn")
        self.backgCombo.addItem("Soprano Sax")
        self.backgCombo.addItem("Piccolo")
        self.backgCombo.addItem("Pan Flute")
        self.backgCombo.addItem("Whistle")
        self.backgCombo.addItem("Warm")
        self.backgCombo.addItem("Bowed glass")
        self.backgCombo.addItem("Goblins")

        self.backgCombo.move(430, 285)
        self.backgCombo.activated[str].connect(self.backg_combo_on_activated)

        self.filePathQle = QLineEdit(self)
        self.filePathQle.move(322, 365)
        self.filePathQle.resize(240, 25)
        self.filePathQle.setText(self.file_path)
        self.filePathQle.textChanged[str].connect(self.file_path_on_changed)

        # Przygotowanie i wypisanie opisów
        self.prepare_labels()

    def iteration_on_changed(self, text):
        self.iteration = int(text)

    def tacts_on_changed(self, text):
        self.tacts_number = int(text)

    def cross_prob_on_changed(self, text):
        self.crossing_probability = float(text)

    def mutation_prob_on_changed(self, text):
        self.mutation_probability = float(text)

    def cross_type_combo_on_activated(self, text):
        self.crossing_type = crossing_type_dict[text]

    def cb_changed(self, state):
        if state == Qt.Checked:
            self.checkbox = 1
        else:
            self.checkbox = 0

    def population_on_changed(self, text):
        self.population = int(text)

    def tempo_on_changed(self, text):
        self.tempo = int(text)

    def scale_combo_on_activated(self, text):
        self.scale_type = scales_dict[text]

    def tone_combo_on_activated(self, text):
        self.tone_of_scale = notes_dict[text]

    def instru_combo_on_activated(self, text):
        self.instrument_type = instrument_type_dict[text]

    def backg_combo_on_activated(self, text):
        self.background_type = instrument_type_dict[text]

    def file_path_on_changed(self, text):
        self.file_path = text

    def prepare_labels(self):
        self.font = QFont('times', 12)
        self.little_font = QFont('times', 9)

        # Lewa kolumna opisów
        self.iterationLabel = QLabel("Liczba iteracji:", self)
        self.iterationLabel.setFont(self.font)
        self.iterationLabel.setGeometry(QRect(10, 20, 100, 20))
        self.iterationRangeLabel = QLabel(str(self.iteration_minimum_value) + " - "
                                          + str(self.iteration_maximum_value), self)
        self.iterationRangeLabel.setFont(self.little_font)
        self.iterationRangeLabel.setGeometry(QRect(100, 60, 100, 20))

        self.tactsLabel = QLabel("Liczba taktów:", self)
        self.tactsLabel.setFont(self.font)
        self.tactsLabel.setGeometry(QRect(10, 80, 100, 20))
        self.tactsRangeLabel = QLabel(str(self.tacts_minimum_value) + " - "
                                      + str(self.tacts_maximum_value), self)
        self.tactsRangeLabel.setFont(self.little_font)
        self.tactsRangeLabel.setGeometry(QRect(100, 120, 100, 20))

        self.crossProbLabel = QLabel("Prawdopodobieństwo krzyżowania:", self)
        self.crossProbLabel.setFont(self.font)
        self.crossProbLabel.setGeometry(QRect(10, 140, 300, 20))
        self.crossRangeProbLabel = QLabel(str(self.probability_minimum_value) + " - "
                                          + str(self.probability_maximum_value), self)
        self.crossRangeProbLabel.setFont(self.little_font)
        self.crossRangeProbLabel.setGeometry(QRect(100, 180, 100, 20))

        self.mutationProbLabel = QLabel("Prawdopodobieństwo mutacji:", self)
        self.mutationProbLabel.setFont(self.font)
        self.mutationProbLabel.setGeometry(QRect(10, 200, 300, 20))
        self.mutationRangeProbLabel = QLabel(str(self.probability_minimum_value) + " - " +
                                             str(self.probability_maximum_value), self)
        self.mutationRangeProbLabel.setFont(self.little_font)
        self.mutationRangeProbLabel.setGeometry(QRect(100, 240, 100, 20))

        self.crossTypeLabel = QLabel("Typ krzyżowania:", self)
        self.crossTypeLabel.setFont(self.font)
        self.crossTypeLabel.setGeometry(QRect(10, 260, 300, 20))

        self.diagramLabel = QLabel("Wykresy:", self)
        self.diagramLabel.setFont(self.font)
        self.diagramLabel.setGeometry(QRect(10, 320, 80, 20))

        # Prawa kolumna opisów
        self.populationLabel = QLabel("Populacja:", self)
        self.populationLabel.setFont(self.font)
        self.populationLabel.setGeometry(QRect(300, 20, 300, 20))
        self.populationRangeLabel = QLabel(str(self.population_minimum_value) + " - " +
                                           str(self.population_maximum_value), self)
        self.populationRangeLabel.setFont(self.little_font)
        self.populationRangeLabel.setGeometry(QRect(385, 60, 100, 20))

        self.tempoLabel = QLabel("Tempo:", self)
        self.tempoLabel.setFont(self.font)
        self.tempoLabel.setGeometry(QRect(300, 80, 100, 20))
        self.tempoRangeLabel = QLabel(str(self.tempo_minimum_value) + " - " + str(self.tempo_maximum_value), self)
        self.tempoRangeLabel.setFont(self.little_font)
        self.tempoRangeLabel.setGeometry(QRect(385, 120, 100, 20))

        self.scaleLabel = QLabel("Rodzaj skali:", self)
        self.scaleLabel.setFont(self.font)
        self.scaleLabel.setGeometry(QRect(300, 140, 100, 20))

        self.toneLabel = QLabel("Tonacja:", self)
        self.toneLabel.setFont(self.font)
        self.toneLabel.setGeometry(QRect(300, 200, 300, 20))

        self.instruLabel = QLabel("Instrument:", self)
        self.instruLabel.setFont(self.font)
        self.instruLabel.setGeometry(QRect(300, 260, 300, 20))

        self.backLabel = QLabel("Tło:", self)
        self.backLabel.setFont(self.font)
        self.backLabel.setGeometry(QRect(460, 260, 300, 20))

        self.pathLabel = QLabel("Ścieżka zapisu:", self)
        self.pathLabel.setFont(self.font)
        self.pathLabel.setGeometry(QRect(320, 340, 300, 20))

    def sett_clicked(self):
        self.settingsClicked.emit()

    def play_clicked(self):
        self.algorithm.start(self.iteration, self.tacts_number, self.crossing_probability, self.mutation_probability,
                             self.tempo, self.scale_type, self.tone_of_scale, self.instrument_type,
                             self.background_type, self.crossing_type, self.file_path, self.population, self.checkbox)

        self.algorithm.run()

        reply = QMessageBox.question(self, 'Message', 'Komponowanie zakończone', QMessageBox.Ok, QMessageBox.Ok)
        if reply == QMessageBox.Ok:
            #print(self.file_path[0:self.file_path.rfind("/")])
            plt.show()
            os.startfile(self.file_path[0:self.file_path.rfind("/")])   # otworzenie folderu docelowego
