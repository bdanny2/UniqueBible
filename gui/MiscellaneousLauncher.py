import config
from qtpy.QtCore import Qt
from qtpy.QtWidgets import (QPushButton, QLineEdit, QComboBox, QGroupBox, QGridLayout, QHBoxLayout, QSlider, QVBoxLayout, QWidget)
from gui.HighlightLauncher import HighlightLauncher
from util.TtsLanguages import TtsLanguages

class MiscellaneousLauncher(QWidget):

    def __init__(self, parent):
        super().__init__()
        # set title
        self.setWindowTitle(config.thisTranslation["cp4"])
        # set up variables
        self.parent = parent
        # setup interface
        self.setupUI()

    def setupUI(self):
        mainLayout = QGridLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        self.highLightLauncher = HighlightLauncher(self)
        leftLayout.addWidget(self.highLightLauncher)
        rightLayout.addWidget(self.noteEditor())
        rightLayout.addWidget(self.textToSpeechUtility())
        rightLayout.addWidget(self.utilities())
        rightLayout.addStretch()
        mainLayout.addLayout(leftLayout, 0, 0, 1, 2)
        mainLayout.addLayout(rightLayout, 0, 2, 1, 1)
        self.setLayout(mainLayout)


    def noteEditor(self):
        box = QGroupBox(config.thisTranslation["note_editor"])
        subLayout = QHBoxLayout()
        button = QPushButton(config.thisTranslation["menu7_create"])
        button.setToolTip(config.thisTranslation["menu7_create"])
        button.clicked.connect(self.parent.parent.createNewNoteFile)
        subLayout.addWidget(button)
        button = QPushButton(config.thisTranslation["menu7_open"])
        button.setToolTip(config.thisTranslation["menu7_open"])
        button.clicked.connect(self.parent.parent.openTextFileDialog)
        subLayout.addWidget(button)
        box.setLayout(subLayout)
        return box

    def utilities(self):
        box = QGroupBox(config.thisTranslation["utilities"])
        subLayout = QHBoxLayout()
        button = QPushButton(config.thisTranslation["presentation"])
        button.setToolTip(config.thisTranslation["presentation"])
        button.clicked.connect(lambda: self.parent.parent.runPlugin("Presentation"))
        subLayout.addWidget(button)
        if config.isYoutubeDownloaderInstalled:
            button = QPushButton(config.thisTranslation["youtube_utility"])
            button.setToolTip(config.thisTranslation["youtube_utility"])
            button.clicked.connect(self.parent.parent.openYouTube)
            subLayout.addWidget(button)
        box.setLayout(subLayout)
        return box

    def textToSpeechUtility(self):
        box = QGroupBox(config.thisTranslation["tts_utility"])

        layout = QVBoxLayout()

        subLayout = QHBoxLayout()
        self.ttsEdit = QLineEdit()
        self.ttsEdit.setClearButtonEnabled(True)
        self.ttsEdit.setToolTip(config.thisTranslation["enter_text_here"])
        self.ttsEdit.returnPressed.connect(self.speakText)
        subLayout.addWidget(self.ttsEdit)
        layout.addLayout(subLayout)

        self.ttsSlider = QSlider(Qt.Horizontal)
        self.ttsSlider.setToolTip(config.thisTranslation["adjustSpeed"])
        self.ttsSlider.setMinimum(10)
        self.ttsSlider.setMaximum(310)
        self.ttsSlider.setValue(config.espeakSpeed if config.espeak else (160 + config.qttsSpeed * 150))
        self.ttsSlider.valueChanged.connect(self.changeEspeakSpeed if config.espeak else self.changeQttsSpeed)
        layout.addWidget(self.ttsSlider)

        subLayout = QHBoxLayout()

        self.languageCombo = QComboBox()
        subLayout.addWidget(self.languageCombo)
        if config.espeak:
            languages = TtsLanguages().isoLang2epeakLang
        else:
            languages = TtsLanguages().isoLang2qlocaleLang
        self.languageCodes = list(languages.keys())
        for code in self.languageCodes:
            self.languageCombo.addItem(languages[code][1])
        # Check if selected tts engine has the language user specify.
        if not (config.ttsDefaultLangauge in self.languageCodes):
            config.ttsDefaultLangauge = "en"
        # Set initial index
        # It is essential.  Otherwise, default tts language is changed by defaultTtsLanguageChanged method.
        ttsLanguageIndex = self.languageCodes.index(config.ttsDefaultLangauge)
        self.languageCombo.setCurrentIndex(ttsLanguageIndex)
        # Change default tts language as users select a new language
        self.languageCombo.currentIndexChanged.connect(self.defaultTtsLanguageChanged)

        button = QPushButton(config.thisTranslation["speak"])
        button.setToolTip(config.thisTranslation["speak"])
        button.clicked.connect(self.speakText)
        subLayout.addWidget(button)
        button = QPushButton(config.thisTranslation["stop"])
        button.setToolTip(config.thisTranslation["stop"])
        button.clicked.connect(self.parent.parent.textCommandParser.stopTtsAudio)
        subLayout.addWidget(button)
        layout.addLayout(subLayout)

        box.setLayout(layout)
        return box

    def defaultTtsLanguageChanged(self, index):
        config.ttsDefaultLangauge = self.languageCodes[index]

    def speakText(self):
        text = self.ttsEdit.text()
        if text:
            if config.isTtsInstalled:
                if ":::" in text:
                    text = text.split(":::")[-1]
                command = "SPEAK:::{0}:::{1}".format(self.languageCodes[self.languageCombo.currentIndex()], text)
                self.parent.isRefreshing = True
                self.parent.runTextCommand(command)
                self.parent.isRefreshing = False
            else:
                self.parent.displayMessage(config.thisTranslation["message_noSupport"])
        else:
            self.parent.displayMessage(config.thisTranslation["enterTextFirst"])

    def changeQttsSpeed(self, value):
        config.qttsSpeed = (value * (1.5/300) - .5)

    def changeEspeakSpeed(self, value):
        config.espeakSpeed = value

    def refresh(self):
        ttsLanguageIndex = self.languageCodes.index(config.ttsDefaultLangauge)
        self.languageCombo.setCurrentIndex(ttsLanguageIndex)
        self.highLightLauncher.refresh()
