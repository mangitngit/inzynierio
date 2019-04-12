from gui.start import *
from gui.settings import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        QMainWindow.setWindowTitle(self, "AI Composer")
        QMainWindow.setWindowIcon(self, QIcon("src/note.png"))
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        self.start_screen = StartScreen()
        self.settings_screen = SettingsScreen()

        self.central_widget.addWidget(self.start_screen)
        self.central_widget.addWidget(self.settings_screen)
        self.resize(600, 400)

        self.central_widget.setCurrentWidget(self.start_screen)

        self.start_screen.settingsClicked.connect(lambda: self.central_widget.setCurrentWidget(self.settings_screen))
        self.settings_screen.backClicked.connect(lambda: self.central_widget.setCurrentWidget(self.start_screen))
