
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtPrintSupport import * 
import os
import sys
bgc = 'black;'
butc = 'white;'

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.showMaximized()
        self.setWindowIcon(QIcon("icon.png"))
        
        self.setStyleSheet(f"background-color: {bgc}")
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(f"background-color: {bgc}")
        
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.setCentralWidget(self.tabs)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.navtb = QToolBar("Navigation")
        self.addToolBar(self.navtb)
        self.navtb.setStyleSheet(f"background-color: {bgc}")
        self.navtb.setStyleSheet(f"color: {butc}")
        back_btn = QAction("Back", self)
        
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        self.navtb.addAction(back_btn)
  
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        self.navtb.addAction(next_btn)
  
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        self.navtb.addAction(reload_btn)
  
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
  
        home_btn.triggered.connect(self.navigate_home)
        dmode = QAction("Dark Mode", self)
        dmode.setStatusTip("Change to Dark Mode")
  
        dmode.triggered.connect(self.darkmode)
        self.navtb.addAction(dmode)
        lmode = QAction("Light Mode", self)
        lmode.setStatusTip("Change to Light Mode")
        self.navtb.addAction(lmode)
  
        lmode.triggered.connect(self.lightmode)
        self.navtb.addAction(home_btn)
        fs = QAction("Fullscreen", self)
        fs.setStatusTip("Get fullscreen")
        fs.triggered.connect(self.fullscreen)
        self.navtb.addAction(fs)
        self.navtb.addSeparator()
  
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
  
        self.navtb.addWidget(self.urlbar)
  
        stop_btn = QAction("Exit", self)
        stop_btn.setStatusTip("Exit Sheffari")
        stop_btn.triggered.connect(self.close)
        self.navtb.addAction(stop_btn)
  
        self.add_new_tab(QUrl('https://Mengo-Team.github.io/SheffariHomePage/'), 'Homepage')
  
        self.show()
        self.setWindowTitle("Mengo Sheffari Web Browser")
    def add_new_tab(self, qurl = None, label ="Blank"):
        if qurl is None:
            qurl = QUrl('https://Mengo-Team.github.io/SheffariHomePage/')
  
        browser = QWebEngineView()
  
        browser.setUrl(qurl)
  
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
  
        browser.urlChanged.connect(lambda qurl, browser = browser:
                                   self.update_urlbar(qurl, browser))
  
        browser.loadFinished.connect(lambda _, i = i, browser = browser:
                                     self.tabs.setTabText(i, browser.page().title()))
  
    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()
  
    def current_tab_changed(self, i):
  
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return

        self.tabs.removeTab(i)

    def update_title(self, browser):

        if browser != self.tabs.currentWidget():
            return
  
        title = self.tabs.currentWidget().page().title()
  
        self.setWindowTitle("% s - Sheffari Web Browser" % title)
  
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("https://Mengo-Team.github.io/SheffariHomePage/"))
  
    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.tabs.currentWidget().setUrl(q)
  
    def update_urlbar(self, q, browser = None):
        if browser != self.tabs.currentWidget():
            return

        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)
    def fullscreen(self):
        self.showFullScreen()
    def darkmode(self):
        self.setStyleSheet(f"background-color: {bgc}")
        self.tabs.setStyleSheet(f"background-color: {bgc}")
        self.navtb.setStyleSheet(f"background-color: {bgc}")
        self.navtb.setStyleSheet(f"color: {butc}")
    def lightmode(self):
        self.setStyleSheet(f"background-color: {butc}")
        self.tabs.setStyleSheet(f"background-color: {butc}")
        self.navtb.setStyleSheet(f"background-color: {butc}")
        self.navtb.setStyleSheet(f"color: {bgc}")
if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Sheffari")
    window = MainWindow()
    app.exec_()
