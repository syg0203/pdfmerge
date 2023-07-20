import os
import sys
from platform import system
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QStyleFactory, QDesktopWidget
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyPDF2 import PdfFileMerger
from PyQt5 import QtCore, QtGui, QtWidgets

# Application root location ↓
if system() == "Windows":
    appFolder = os.path.dirname(os.path.realpath(sys.argv[0])) + "\\"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 283)
        MainWindow.setMinimumSize(QtCore.QSize(465, 283))
        MainWindow.setMaximumSize(QtCore.QSize(465, 283))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/main_icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 3, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/Add Folder_50px.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_add = QtWidgets.QPushButton(self.tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/plus_50px.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon2)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_remove = QtWidgets.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/minus_50px.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_remove.setIcon(icon3)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(50, -1, 50, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_up = QtWidgets.QPushButton(self.tab)
        self.pushButton_up.setMaximumSize(QtCore.QSize(91, 21))
        self.pushButton_up.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/collapse_arrow_50px.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_up.setIcon(icon4)
        self.pushButton_up.setObjectName("pushButton_up")
        self.verticalLayout_2.addWidget(self.pushButton_up)
        self.pushButton_down = QtWidgets.QPushButton(self.tab)
        self.pushButton_down.setMaximumSize(QtCore.QSize(91, 23))
        self.pushButton_down.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/expand_arrow_50px.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_down.setIcon(icon5)
        self.pushButton_down.setObjectName("pushButton_down")
        self.verticalLayout_2.addWidget(self.pushButton_down)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_make_pdf = QtWidgets.QPushButton(self.tab)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/export_pdf_50px.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_make_pdf.setIcon(icon6)
        self.pushButton_make_pdf.setObjectName("pushButton_make_pdf")
        self.horizontalLayout.addWidget(self.pushButton_make_pdf)
        self.pushButton_clear = QtWidgets.QPushButton(self.tab)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/clear_symbol_50px.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clear.setIcon(icon7)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/top_menu_50px.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon8, "")
        self.horizontalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Image To PDF Converter App"))
        self.label_8.setText(_translate(
            "MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">PDF 목록</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", " 폴더 추가"))
        self.pushButton_add.setText(_translate("MainWindow", " 파일 추가"))
        self.pushButton_remove.setText(_translate("MainWindow", " 파일 제거"))
        self.pushButton_make_pdf.setText(_translate("MainWindow", " PDF 생성"))
        self.pushButton_clear.setText(_translate("MainWindow", " 초기화"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("MainWindow", "Home"))


class main:
    def make_pdf_all(dir_path):
        join = str("/")
        # dir_files = [dir_path + join + f for f in os.listdir(
        #     dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        dir_files = [dir_path + join + f for f in os.listdir(
            dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f[-3:].lower()=='pdf']
        return dir_files

    def make_pdf_only_selected(selected_files, path):
        merger = PdfFileMerger()
        for pdf in selected_files:
            merger.append(pdf)
        merger.write(path)
        merger.close()


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Constructor."""
        super(App, self).__init__()
        self.setupUi(self)
        # Load the UI(User Interface) file.
        # uic.loadUi(appFolder + "ImaP.ui", self)
        self.makeWindowCenter()
        self.run_system()  # main operating function of this GUI FIle
        # Status Bar Message
        self.statusBar().showMessage("Copyrightⓒ2022 by ShinYeongGeun ")
        self.setWindowTitle("PDF Merge GUI For Desktop")

    def makeWindowCenter(self):
        """For launching windows in center."""
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def run_system(self):
        """Main load function"""
        self.pushButton.clicked.connect(self.add_folder_button_on_click)
        self.pushButton_add.clicked.connect(self.add_images_button_on_click)
        self.pushButton_remove.clicked.connect(self.remove_button_on_click)
        self.pushButton_up.clicked.connect(self.up_button_on_click)
        self.pushButton_down.clicked.connect(self.down_button_on_click)
        self.pushButton_make_pdf.clicked.connect(self.make_pdf_button_on_click)
        self.pushButton_clear.clicked.connect(self.clear_button_on_click)

    def add_folder_button_on_click(self):
        """Add a Folder button"""
        dir_path = QFileDialog.getExistingDirectory(self, 'Open File')

        if dir_path != "":
            dir_files = main.make_pdf_all(dir_path)
            for i in dir_files:
                next_row = self.listWidget.count()
                self.listWidget.insertItem(next_row, i)
        else:
            return

    def add_images_button_on_click(self):
        file_name = QFileDialog.getOpenFileName(
            self, "Open File", os.getenv('HOME'), 'PDF(*.pdf)')
        next_row = self.listWidget.count()
        if file_name[0] != "":
            self.listWidget.insertItem(next_row, file_name[0])

    def remove_button_on_click(self):
        current_row = self.listWidget.currentRow()
        item = self.listWidget.item(current_row)
        if item is None:
            pass

        else:
            get_reply = QMessageBox.question(self, "파일 삭제", str(item.text())
                                             + " 파일을 리스트에서 삭제하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
            if get_reply == QMessageBox.Yes:
                element = self.listWidget.takeItem(current_row)
                del element
            else:
                pass

    def up_button_on_click(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 1:
            item = self.listWidget.takeItem(current_row)
            self.listWidget.insertItem(current_row - 1, item)
            self.listWidget.setCurrentItem(item)

    def down_button_on_click(self):
        current_row = self.listWidget.currentRow()
        if current_row < self.listWidget.count() - 1:
            item = self.listWidget.takeItem(current_row)
            self.listWidget.insertItem(current_row + 1, item)
            self.listWidget.setCurrentItem(item)

    def clear_button_on_click(self):
        reply = QMessageBox.question(self, "리스트 전체 삭제", "리스트를 전체 삭제하겠습니까?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.listWidget.clear()

    def make_pdf_button_on_click(self):
        if self.listWidget.count() == 0:
            reply = QMessageBox.information(self, "경고!", "파일을 추가하세요",
                                            QMessageBox.Ok)

        else:
            items_list = []
            for i in range(self.listWidget.count()):
                items_list.append(str(self.listWidget.item(i).text()))
            path = QFileDialog.getSaveFileName(
                self, 'PDF 저장', os.getenv('HOME'), 'PDF(*.pdf)')
            if path[0] != "":
                main.make_pdf_only_selected(items_list, path[0])
                reply = QMessageBox.information(
                    self, "PDF가 저장됐어요!", str(path[0])+" 가 저장됐어요! ", QMessageBox.Ok)
            else:
                QMessageBox.information(
                    self, "Alert", "파일명을 입력하세요!", QMessageBox.Ok)
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle(QStyleFactory.create("Fusion"))

    darkPalette = QtGui.QPalette()
    darkColor = QColor(254, 127, 156)
    disabledColor = QColor(205, 205, 205)
    darkPalette.setColor(QPalette.Window, darkColor)
    darkPalette.setColor(QPalette.WindowText, Qt.white)
    darkPalette.setColor(QPalette.Base, QColor(158, 66, 68))
    darkPalette.setColor(QPalette.AlternateBase, darkColor)
    darkPalette.setColor(QPalette.ToolTipBase, Qt.white)
    darkPalette.setColor(QPalette.ToolTipText, Qt.white)
    darkPalette.setColor(QPalette.Text, Qt.white)
    darkPalette.setColor(QPalette.Disabled, QPalette.Text, disabledColor)
    darkPalette.setColor(QPalette.Button, darkColor)
    darkPalette.setColor(QPalette.ButtonText, Qt.white)
    darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, disabledColor)
    darkPalette.setColor(QPalette.BrightText, Qt.red)
    darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.HighlightedText, Qt.black)
    darkPalette.setColor(
        QPalette.Disabled, QPalette.HighlightedText, disabledColor)

    app.setPalette(darkPalette)
    app.setStyleSheet(
        "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    run_main = App()  # Instantiate The App() class
    run_main.show()
    sys.exit(app.exec_())
