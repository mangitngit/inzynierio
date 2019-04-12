from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from src.evaluation import *


class SettingsScreen(QWidget):
    backClicked = pyqtSignal()

    def __init__(self):
        super(SettingsScreen, self).__init__()

        self.maximum_value = 100
        self.minimum_value = 0

        self.backButton = QPushButton('Powrót', self)
        self.backButton.setGeometry(QRect(10, 360, 100, 35))
        self.backButton.clicked.connect(self.back_clicked)

        self.saveButton = QPushButton('Zapisz', self)
        self.saveButton.setGeometry(QRect(160, 360, 100, 35))
        self.saveButton.clicked.connect(self.save_clicked)

        self.interval_pryma = QDoubleSpinBox(self)
        self.interval_pryma.setGeometry(QRect(160, 30, 100, 20))
        self.interval_pryma.setMinimum(self.minimum_value)
        self.interval_pryma.setMaximum(self.maximum_value)
        self.interval_pryma.setValue(intervals_value_dict[0])

        self.interval_sekunda_m = QDoubleSpinBox(self)
        self.interval_sekunda_m.setGeometry(QRect(160, 30 + 25 * 1, 100, 20))
        self.interval_sekunda_m.setMinimum(self.minimum_value)
        self.interval_sekunda_m.setMaximum(self.maximum_value)
        self.interval_sekunda_m.setValue(intervals_value_dict[1])

        self.interval_sekunda_w = QDoubleSpinBox(self)
        self.interval_sekunda_w.setGeometry(QRect(160, 30 + 25 * 2, 100, 20))
        self.interval_sekunda_w.setMinimum(self.minimum_value)
        self.interval_sekunda_w.setMaximum(self.maximum_value)
        self.interval_sekunda_w.setValue(intervals_value_dict[2])

        self.interval_tercja_m = QDoubleSpinBox(self)
        self.interval_tercja_m.setGeometry(QRect(160, 30 + 25 * 3, 100, 20))
        self.interval_tercja_m.setMinimum(self.minimum_value)
        self.interval_tercja_m.setMaximum(self.maximum_value)
        self.interval_tercja_m.setValue(intervals_value_dict[3])

        self.interval_tercja_w = QDoubleSpinBox(self)
        self.interval_tercja_w.setGeometry(QRect(160, 30 + 25 * 4, 100, 20))
        self.interval_tercja_w.setMinimum(self.minimum_value)
        self.interval_tercja_w.setMaximum(self.maximum_value)
        self.interval_tercja_w.setValue(intervals_value_dict[4])

        self.interval_kwarta = QDoubleSpinBox(self)
        self.interval_kwarta.setGeometry(QRect(160, 30 + 25 * 5, 100, 20))
        self.interval_kwarta.setMinimum(self.minimum_value)
        self.interval_kwarta.setMaximum(self.maximum_value)
        self.interval_kwarta.setValue(intervals_value_dict[5])

        self.interval_kwarta_zw = QDoubleSpinBox(self)
        self.interval_kwarta_zw.setGeometry(QRect(160, 30 + 25 * 6, 100, 20))
        self.interval_kwarta_zw.setMinimum(self.minimum_value)
        self.interval_kwarta_zw.setMaximum(self.maximum_value)
        self.interval_kwarta_zw.setValue(intervals_value_dict[6])

        self.interval_kwinta = QDoubleSpinBox(self)
        self.interval_kwinta.setGeometry(QRect(160, 30 + 25 * 7, 100, 20))
        self.interval_kwinta.setMinimum(self.minimum_value)
        self.interval_kwinta.setMaximum(self.maximum_value)
        self.interval_kwinta.setValue(intervals_value_dict[7])

        self.interval_seksta_m = QDoubleSpinBox(self)
        self.interval_seksta_m.setGeometry(QRect(160, 30 + 25 * 8, 100, 20))
        self.interval_seksta_m.setMinimum(self.minimum_value)
        self.interval_seksta_m.setMaximum(self.maximum_value)
        self.interval_seksta_m.setValue(intervals_value_dict[8])

        self.interval_seksta_w = QDoubleSpinBox(self)
        self.interval_seksta_w.setGeometry(QRect(160, 30 + 25 * 9, 100, 20))
        self.interval_seksta_w.setMinimum(self.minimum_value)
        self.interval_seksta_w.setMaximum(self.maximum_value)
        self.interval_seksta_w.setValue(intervals_value_dict[9])

        self.interval_septyma_m = QDoubleSpinBox(self)
        self.interval_septyma_m.setGeometry(QRect(160, 30 + 25 * 10, 100, 20))
        self.interval_septyma_m.setMinimum(self.minimum_value)
        self.interval_septyma_m.setMaximum(self.maximum_value)
        self.interval_septyma_m.setValue(intervals_value_dict[10])

        self.interval_septyma_w = QDoubleSpinBox(self)
        self.interval_septyma_w.setGeometry(QRect(160, 30 + 25 * 11, 100, 20))
        self.interval_septyma_w.setMinimum(self.minimum_value)
        self.interval_septyma_w.setMaximum(self.maximum_value)
        self.interval_septyma_w.setValue(intervals_value_dict[11])

        self.interval_oktawa = QDoubleSpinBox(self)
        self.interval_oktawa.setGeometry(QRect(160, 30 + 25 * 12, 100, 20))
        self.interval_oktawa.setMinimum(self.minimum_value)
        self.interval_oktawa.setMaximum(self.maximum_value)
        self.interval_oktawa.setValue(intervals_value_dict[12])

        self.interval_pauza = QDoubleSpinBox(self)
        self.interval_pauza.setGeometry(QRect(425, 30, 100, 20))
        self.interval_pauza.setMinimum(self.minimum_value)
        self.interval_pauza.setMaximum(self.maximum_value)
        self.interval_pauza.setValue(intervals_value_dict[12])

        self.rhytm_nuta = QDoubleSpinBox(self)
        self.rhytm_nuta.setGeometry(QRect(425, 30 + 25 * 1, 100, 20))
        self.rhytm_nuta.setMinimum(self.minimum_value)
        self.rhytm_nuta.setMaximum(self.maximum_value)
        self.rhytm_nuta.setValue(rhytm_value_dict[0])

        self.rhytm_polnuta = QDoubleSpinBox(self)
        self.rhytm_polnuta.setGeometry(QRect(425, 30 + 25 * 2, 100, 20))
        self.rhytm_polnuta.setMinimum(self.minimum_value)
        self.rhytm_polnuta.setMaximum(self.maximum_value)
        self.rhytm_polnuta.setValue(rhytm_value_dict[1])

        self.rhytm_cwiercnuta = QDoubleSpinBox(self)
        self.rhytm_cwiercnuta.setGeometry(QRect(425, 30 + 25 * 3, 100, 20))
        self.rhytm_cwiercnuta.setMinimum(self.minimum_value)
        self.rhytm_cwiercnuta.setMaximum(self.maximum_value)
        self.rhytm_cwiercnuta.setValue(rhytm_value_dict[2])

        self.rhytm_osemka = QDoubleSpinBox(self)
        self.rhytm_osemka.setGeometry(QRect(425, 30 + 25 * 4, 100, 20))
        self.rhytm_osemka.setMinimum(self.minimum_value)
        self.rhytm_osemka.setMaximum(self.maximum_value)
        self.rhytm_osemka.setValue(rhytm_value_dict[3])

        self.interval_variety = QDoubleSpinBox(self)
        self.interval_variety.setGeometry(QRect(425, 30 + 25 * 6, 100, 20))
        self.interval_variety.setMinimum(self.minimum_value)
        self.interval_variety.setMaximum(self.maximum_value)
        self.interval_variety.setValue(intervals_data[0])

        self.interval_mean = QDoubleSpinBox(self)
        self.interval_mean.setGeometry(QRect(425, 30 + 25 * 7, 100, 20))
        self.interval_mean.setMinimum(self.minimum_value)
        self.interval_mean.setMaximum(self.maximum_value)
        self.interval_mean.setValue(intervals_data[1])

        self.rhytm_variety = QDoubleSpinBox(self)
        self.rhytm_variety.setGeometry(QRect(425, 30 + 25 * 9, 100, 20))
        self.rhytm_variety.setMinimum(self.minimum_value)
        self.rhytm_variety.setMaximum(self.maximum_value)
        self.rhytm_variety.setValue(rhytm_data[0])

        self.rhytm_mean = QDoubleSpinBox(self)
        self.rhytm_mean.setGeometry(QRect(425, 30 + 25 * 10, 100, 20))
        self.rhytm_mean.setMinimum(self.minimum_value)
        self.rhytm_mean.setMaximum(self.maximum_value)
        self.rhytm_mean.setValue(rhytm_data[1])

        self.tone_deviation = QDoubleSpinBox(self)
        self.tone_deviation.setGeometry(QRect(425, 30 + 25 * 12, 100, 20))
        self.tone_deviation.setMinimum(self.minimum_value)
        self.tone_deviation.setMaximum(self.maximum_value)
        self.tone_deviation.setValue(others_data[0])

        self.break_value = QDoubleSpinBox(self)
        self.break_value.setGeometry(QRect(425, 30 + 25 * 13, 100, 20))
        self.break_value.setMinimum(self.minimum_value)
        self.break_value.setMaximum(self.maximum_value)
        self.break_value.setValue(others_data[1])

        self.prepareLabels()

    def back_clicked(self):
        self.backClicked.emit()

    def save_clicked(self):
        intervals_value_dict[0] = self.interval_pryma.value()
        intervals_value_dict[1] = self.interval_sekunda_m.value()
        intervals_value_dict[2] = self.interval_sekunda_w.value()
        intervals_value_dict[3] = self.interval_tercja_m.value()
        intervals_value_dict[4] = self.interval_tercja_w.value()
        intervals_value_dict[5] = self.interval_kwarta.value()
        intervals_value_dict[6] = self.interval_kwarta_zw.value()
        intervals_value_dict[7] = self.interval_kwinta.value()
        intervals_value_dict[8] = self.interval_seksta_m.value()
        intervals_value_dict[9] = self.interval_seksta_w.value()
        intervals_value_dict[10] = self.interval_septyma_m.value()
        intervals_value_dict[11] = self.interval_septyma_w.value()
        intervals_value_dict[12] = self.interval_oktawa.value()
        intervals_value_dict[13] = self.interval_pauza.value()

        rhytm_value_dict[0] = self.rhytm_nuta.value()
        rhytm_value_dict[1] = self.rhytm_polnuta.value()
        rhytm_value_dict[2] = self.rhytm_cwiercnuta.value()
        rhytm_value_dict[3] = self.rhytm_osemka.value()

        intervals_data[0] = self.interval_variety.value()
        intervals_data[1] = self.interval_mean.value()

        rhytm_data[0] = self.rhytm_variety.value()
        rhytm_data[1] = self.rhytm_mean.value()

        others_data[0] = self.tone_deviation.value()
        others_data[1] = self.break_value.value()

    def prepareLabels(self):
        self.font = QFont('times', 13)
        self.font2 = QFont('times', 11)
        self.font3 = QFont('times', 12)
        self.font4 = QFont('times', 15)

        self.wagi = QLabel("Wagi ocen cząstkowych: ", self)
        self.wagi.setFont(self.font4)
        self.wagi.setAlignment(Qt.AlignRight)
        self.wagi.setGeometry(QRect(10, 2, 400, 25))

        self.pryma = QLabel("Pryma: ", self)
        self.pryma.setFont(self.font)
        self.pryma.setAlignment(Qt.AlignRight)
        self.pryma.setGeometry(QRect(10, 30, 150, 20))

        self.sekunda_m = QLabel("Sekunda mała: ", self)
        self.sekunda_m.setFont(self.font)
        self.sekunda_m.setAlignment(Qt.AlignRight)
        self.sekunda_m.setGeometry(QRect(10, 30 + 25 * 1, 150, 20))

        self.sekunda_w = QLabel("Sekunda wielka: ", self)
        self.sekunda_w.setFont(self.font)
        self.sekunda_w.setAlignment(Qt.AlignRight)
        self.sekunda_w.setGeometry(QRect(10, 30 + 25 * 2, 150, 20))

        self.tercja_m = QLabel("Tercja mała: ", self)
        self.tercja_m.setFont(self.font)
        self.tercja_m.setAlignment(Qt.AlignRight)
        self.tercja_m.setGeometry(QRect(10, 30 + 25 * 3, 150, 20))

        self.tercja_w = QLabel("Tercja wielka: ", self)
        self.tercja_w.setFont(self.font)
        self.tercja_w.setAlignment(Qt.AlignRight)
        self.tercja_w.setGeometry(QRect(10, 30 + 25 * 4, 150, 20))

        self.kwarta = QLabel("Kwarta czysta: ", self)
        self.kwarta.setFont(self.font)
        self.kwarta.setAlignment(Qt.AlignRight)
        self.kwarta.setGeometry(QRect(10, 30 + 25 * 5, 150, 20))

        self.kwarta_zw = QLabel("Kwarta zwiększona:", self)
        self.kwarta_zw.setFont(self.font)
        self.kwarta_zw.setAlignment(Qt.AlignRight)
        self.kwarta_zw.setGeometry(QRect(10, 30 + 25 * 6, 150, 20))

        self.kwinta = QLabel("Kwinta czysta: ", self)
        self.kwinta.setFont(self.font)
        self.kwinta.setAlignment(Qt.AlignRight)
        self.kwinta.setGeometry(QRect(10, 30 + 25 * 7, 150, 20))

        self.seksta_m = QLabel("Seksta mała: ", self)
        self.seksta_m.setFont(self.font)
        self.seksta_m.setAlignment(Qt.AlignRight)
        self.seksta_m.setGeometry(QRect(10, 30 + 25 * 8, 150, 20))

        self.seksta_w = QLabel("Seksta wielka: ", self)
        self.seksta_w.setFont(self.font)
        self.seksta_w.setAlignment(Qt.AlignRight)
        self.seksta_w.setGeometry(QRect(10, 30 + 25 * 9, 150, 20))

        self.septyma_m = QLabel("Septyma mała: ", self)
        self.septyma_m.setFont(self.font)
        self.septyma_m.setAlignment(Qt.AlignRight)
        self.septyma_m.setGeometry(QRect(10, 30 + 25 * 10, 150, 20))

        self.septyma_w = QLabel("Septyma wielka: ", self)
        self.septyma_w.setFont(self.font)
        self.septyma_w.setAlignment(Qt.AlignRight)
        self.septyma_w.setGeometry(QRect(10, 30 + 25 * 11, 150, 20))

        self.oktawa = QLabel("Oktawa: ", self)
        self.oktawa.setFont(self.font)
        self.oktawa.setAlignment(Qt.AlignRight)
        self.oktawa.setGeometry(QRect(10, 30 + 25 * 12, 150, 20))

        self.pauza = QLabel("Pauza:", self)
        self.pauza.setFont(self.font)
        self.pauza.setAlignment(Qt.AlignRight)
        self.pauza.setGeometry(QRect(270, 30, 150, 20))

        self.nuta = QLabel("Nuta:", self)
        self.nuta.setFont(self.font)
        self.nuta.setAlignment(Qt.AlignRight)
        self.nuta.setGeometry(QRect(270, 30 + 25 * 1, 150, 20))

        self.polnuta = QLabel("Półnuta:", self)
        self.polnuta.setFont(self.font)
        self.polnuta.setAlignment(Qt.AlignRight)
        self.polnuta.setGeometry(QRect(270, 30 + 25 * 2, 150, 20))

        self.cwiercnuta = QLabel("Ćwierćnuta:", self)
        self.cwiercnuta.setFont(self.font)
        self.cwiercnuta.setAlignment(Qt.AlignRight)
        self.cwiercnuta.setGeometry(QRect(270, 30 + 25 * 3, 150, 20))

        self.osemka = QLabel("Ósemka:", self)
        self.osemka.setFont(self.font)
        self.osemka.setAlignment(Qt.AlignRight)
        self.osemka.setGeometry(QRect(270, 30 + 25 * 4, 150, 20))

        self.intervals = QLabel("Interwały:", self)
        self.intervals.setFont(self.font)
        self.intervals.setAlignment(Qt.AlignRight)
        self.intervals.setGeometry(QRect(220, 30 + 25 * 5, 150, 20))

        self.intervals_variety_l = QLabel("Różnorodność:", self)
        self.intervals_variety_l.setFont(self.font2)
        self.intervals_variety_l.setAlignment(Qt.AlignRight)
        self.intervals_variety_l.setGeometry(QRect(270, 30 + 25 * 6, 150, 20))

        self.intervals_mean_l = QLabel("Średnia:", self)
        self.intervals_mean_l.setFont(self.font2)
        self.intervals_mean_l.setAlignment(Qt.AlignRight)
        self.intervals_mean_l.setGeometry(QRect(270, 30 + 25 * 7, 150, 20))

        self.rhytm = QLabel("Rytmika:", self)
        self.rhytm.setFont(self.font)
        self.rhytm.setAlignment(Qt.AlignRight)
        self.rhytm.setGeometry(QRect(220, 30 + 25 * 8, 150, 20))

        self.rhytm_variety_l = QLabel("Różnorodnośc:", self)
        self.rhytm_variety_l.setFont(self.font2)
        self.rhytm_variety_l.setAlignment(Qt.AlignRight)
        self.rhytm_variety_l.setGeometry(QRect(270, 30 + 25 * 9, 150, 20))

        self.rhytm_mean_l = QLabel("Średnia:", self)
        self.rhytm_mean_l.setFont(self.font2)
        self.rhytm_mean_l.setAlignment(Qt.AlignRight)
        self.rhytm_mean_l.setGeometry(QRect(270, 30 + 25 * 10, 150, 20))

        self.tone_diff = QLabel("Różnorodność tonów:", self)
        self.tone_diff.setFont(self.font3)
        self.tone_diff.setAlignment(Qt.AlignRight)
        self.tone_diff.setGeometry(QRect(240, 30 + 25 * 12, 180, 20))

        self.break_l = QLabel("Ilość przerw:", self)
        self.break_l.setFont(self.font)
        self.break_l.setAlignment(Qt.AlignRight)
        self.break_l.setGeometry(QRect(270, 30 + 25 * 13, 150, 20))
