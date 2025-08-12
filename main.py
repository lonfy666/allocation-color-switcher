import sys
import ctypes
import winreg
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QColor, QIcon
from design import Ui_MainWindow
from vcolorpicker import getColor


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.internal_color = QColor(60, 60, 60)
        self.external_color = QColor(60, 60, 60)

        self.ui.internalcolor.setStyleSheet(f"background-color: rgb({self.internal_color.red()}, {self.internal_color.green()}, {self.internal_color.blue()});")
        self.ui.externalcolor.setStyleSheet(f"background-color: rgb({self.external_color.red()}, {self.external_color.green()}, {self.external_color.blue()});")
        self.ui.internalcolor.clicked.connect(self.pickInternalColor)
        self.ui.externalcolor.clicked.connect(self.pickExternalColor)
        self.ui.pushButton.clicked.connect(self.applyColors)

    def pickInternalColor(self):
        rgb = getColor()
        if rgb:
            self.internal_color = QColor(*rgb)
            r, g, b = rgb
            self.ui.internalcolor.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def pickExternalColor(self):
        rgb = getColor()
        if rgb:
            self.external_color = QColor(*rgb)
            r, g, b = rgb
            self.ui.externalcolor.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def applyColors(self):
        colors_key = r"Control Panel\Colors"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, colors_key, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Hilight", 0, winreg.REG_SZ,
                              f"{self.internal_color.red()} {self.internal_color.green()} {self.internal_color.blue()}")
            winreg.SetValueEx(key, "HotTrackColor", 0, winreg.REG_SZ,
                              f"{self.external_color.red()} {self.external_color.green()} {self.external_color.blue()}")

        user32 = ctypes.windll.user32
        COLOR_HIGHLIGHT = 13
        COLOR_HOTLIGHT = 26
        rgb_internal = self.internal_color.blue() << 16 | self.internal_color.green() << 8 | self.internal_color.red()
        rgb_external = self.external_color.blue() << 16 | self.external_color.green() << 8 | self.external_color.red()
        elements = (ctypes.c_int * 2)(COLOR_HIGHLIGHT, COLOR_HOTLIGHT)
        colors = (ctypes.c_uint * 2)(rgb_internal, rgb_external)
        user32.SetSysColors(2, elements, colors)

        if self.ui.checkBox.isChecked():
            import os
            os.system("taskkill /f /im explorer.exe")
            os.system("start explorer.exe")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program()
    window.show()
    sys.exit(app.exec())