import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog)
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPalette, QColor, QFont

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("QWidget{background-color:#242424;border:2px solid #181824}QPushButton{background-color:#343434;color:#f1edec;border:1px solid #181824;padding:5px;min-width:80px}QPushButton:hover{background-color:#404040}QLineEdit{background-color:#343434;color:#f1edec;border:1px solid #181824;padding:5px}")
        self.player = QMediaPlayer() 
        self.path_input = QLineEdit(placeholderText='Select file...', parent=self)
        self.browse_button = QPushButton('Browse', clicked=lambda: self.browse_file(), parent=self)
        self.play_button = QPushButton('▶', clicked=lambda: self.play_music(), parent=self)
        self.play_button.setToolTip('Play')
        font = QFont("Cascadia Code")
        font.setPointSize(14)
        browse_layout = QHBoxLayout() #Browse Section
        browse_layout.addWidget(self.path_input)
        browse_layout.addWidget(self.browse_button)
        layout = QVBoxLayout()
        layout.addLayout(browse_layout)
        layout.addWidget(self.play_button)    
        self.setLayout(layout)
        self.setWindowTitle('Music Player')
        self.resize(468, 126)
    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self,"Select Audio File","","Audio Files (*.mp3 *.wav *.ogg *.flac *.m4a *.aac *.wma)")
        if file_name:
            self.path_input.setText(file_name)
    def play_music(self):
        if self.path_input.text():
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.path_input.text())))
            self.player.play()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setFont(QFont("Cascadia Code", 10))
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor('#242424'))
    palette.setColor(QPalette.WindowText, QColor('#f1edec'))
    app.setPalette(palette)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())