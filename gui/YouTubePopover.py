import config
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QAction, QApplication
from qtpy.QtWebEngineWidgets import QWebEnginePage, QWebEngineView, QWebEngineSettings

class YouTubePopover(QWebEngineView):

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle(config.thisTranslation["menu11_youtube"])
        self.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        #self.page().fullScreenRequested.connect(lambda request: request.accept())
        self.page().fullScreenRequested.connect(self.fullScreenRequested)
        #self.load(QUrl("https://www.youtube.com/"))
        self.urlString = ""
        self.urlChanged.connect(self.videoLinkChanged)
        # add context menu (triggered by right-clicking)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.addMenuActions()

    def fullScreenRequested(self, request):
        self.parent.showFullScreen()
        request.accept()

    def exitFullScreen(self):
        self.parent.showNormal()
        self.page().triggerAction(QWebEnginePage.ExitFullScreen)

    def videoLinkChanged(self, url):
        self.urlString = url.toString()
        self.parent.addressBar.setText(self.urlString)

    def addMenuActions(self):
        goBack = QAction(self)
        goBack.setText(config.thisTranslation["youtube_back"])
        goBack.triggered.connect(self.back)
        self.addAction(goBack)

        goForward = QAction(self)
        goForward.setText(config.thisTranslation["youtube_forward"])
        goForward.triggered.connect(self.forward)
        self.addAction(goForward)

        separator = QAction(self)
        separator.setSeparator(True)
        self.addAction(separator)

        copyLink = QAction(self)
        copyLink.setText(config.thisTranslation["youtube_copy"])
        copyLink.triggered.connect(self.copy)
        self.addAction(copyLink)

        separator = QAction(self)
        separator.setSeparator(True)
        self.addAction(separator)

        mp3 = QAction(self)
        mp3.setText(config.thisTranslation["youtube_mp3"])
        mp3.triggered.connect(lambda: self.convertToFormat("mp3"))
        self.addAction(mp3)

        if self.parent.isFfmpegInstalled:
            video = QAction(self)
            video.setText(config.thisTranslation["youtube_mp4"])
            video.triggered.connect(lambda: self.convertToFormat("mp4"))
            self.addAction(video)
        else:
            video = QAction(self)
            video.setText(config.thisTranslation["downloadVideo"])
            video.triggered.connect(self.parent.downloadLastOption)
            self.addAction(video)
        video = QAction(self)
        video.setText(config.thisTranslation["downloadOptions"])
        video.triggered.connect(self.parent.downloadOptions)
        self.addAction(video)

#        separator = QAction(self)
#        separator.setSeparator(True)
#        self.addAction(separator)
#
#        action = QAction(self)
#        action.setText(config.thisTranslation["youtube_copy"])
#        action.triggered.connect(self.exitFullScreen)
#        self.addAction(action)

    def back(self):
        self.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.page().triggerAction(QWebEnginePage.Forward)

    def copy(self):
        if self.urlString:
            QApplication.clipboard().setText(self.urlString)

    def convertToFormat(self, fileType):
        self.parent.convertToFormat(fileType, self.urlString)
