import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from pydub import AudioSegment

class AudioConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Audio Converter')
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel('Drag and drop M4A files here to convert to MP3')
        self.layout.addWidget(self.label)

        self.convert_button = QPushButton('Convert')
        self.layout.addWidget(self.convert_button)
        self.convert_button.clicked.connect(self.convert_audio)

        self.central_widget.setLayout(self.layout)

    def convert_audio(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        files, _ = QFileDialog.getOpenFileNames(self, 'Select M4A files to convert', '', 'M4A Files (*.m4a);;All Files (*)', options=options)

        for file in files:
            mp3_file = os.path.splitext(file)[0] + '.mp3'
            audio = AudioSegment.from_file(file, format="m4a")
            audio.export(mp3_file, format="mp3")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AudioConverterApp()
    window.show()
    sys.exit(app.exec_())
