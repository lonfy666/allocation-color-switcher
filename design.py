# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import rec_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        MainWindow.setMaximumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icon/image.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0439 \u0444\u043e\u043d \u0438 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"QWidget {\n"
"    background-color: #2b2b2b;\n"
"    color: #f0f0f0;\n"
"    font-family: Arial;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 */\n"
"QPushButton {\n"
"    background-color: #3c3c3c;\n"
"    border: 1px solid #5c5c5c;\n"
"    padding: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #505050;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #2a82da;\n"
"    color: white;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit, QTextEdit, QPlainTextEdit {\n"
"    background-color: #3c3c3c;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5c5c5c;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u041a\u043e\u043c\u0431\u043e-\u0431\u043e\u043a\u0441\u044b */\n"
"QComboBox {\n"
"    background-color: #3c3c3c;\n"
"    color: #ffffff;\n"
"    border: 1px soli"
                        "d #5c5c5c;\n"
"    border-radius: 4px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3c3c3c;\n"
"    selection-background-color: #2a82da;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* \u0427\u0435\u043a\u0431\u043e\u043a\u0441\u044b \u0438 \u0440\u0430\u0434\u0438\u043e-\u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"QCheckBox, QRadioButton {\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"/* \u0422\u0430\u0431\u043b\u0438\u0446\u044b \u0438 \u0441\u043f\u0438\u0441\u043a\u0438 */\n"
"QTableView, QListView, QTreeView {\n"
"    background-color: #3c3c3c;\n"
"    alternate-background-color: #2f2f2f;\n"
"    color: #f0f0f0;\n"
"    gridline-color: #5c5c5c;\n"
"}\n"
"\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u0442\u0430\u0431\u043b\u0438\u0446 */\n"
"QHeaderView::section {\n"
"    background-color: #4b4b4b;\n"
"    color: #f0f0f0;\n"
"    padding: 4px;\n"
"    border: 1px solid #5c5c5c;\n"
"}\n"
"\n"
"/* Scrollbar */\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    backgro"
                        "und: #2b2b2b;\n"
"    border: none;\n"
"    width: 12px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #5c5c5c;\n"
"    border-radius: 6px;\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 440, 281, 51))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(17, 410, 271, 21))
        self.internallabel = QLabel(self.centralwidget)
        self.internallabel.setObjectName(u"internallabel")
        self.internallabel.setGeometry(QRect(8, 6, 281, 21))
        self.externallabel = QLabel(self.centralwidget)
        self.externallabel.setObjectName(u"externallabel")
        self.externallabel.setGeometry(QRect(10, 100, 281, 21))
        self.externalcolor = QPushButton(self.centralwidget)
        self.externalcolor.setObjectName(u"externalcolor")
        self.externalcolor.setGeometry(QRect(4, 133, 291, 51))
        self.internalcolor = QPushButton(self.centralwidget)
        self.internalcolor.setObjectName(u"internalcolor")
        self.internalcolor.setGeometry(QRect(4, 33, 291, 51))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Allocation color switcher", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Restart explorer.exe(recommended)", None))
        self.internallabel.setText(QCoreApplication.translate("MainWindow", u"Set Internal Color", None))
        self.externallabel.setText(QCoreApplication.translate("MainWindow", u"Set External Color", None))
        self.externalcolor.setText("")
        self.internalcolor.setText("")
    # retranslateUi

