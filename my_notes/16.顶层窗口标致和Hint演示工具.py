import sys

from PyQt5.Qt import *


class ControllerWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('WindowFlags')
        self.setWindowIcon(QIcon(QPixmap('setting-100.png').scaled(50, 50)))
        self.preview_window = PreviewWindow()
        self.init_ui()

    def init_ui(self):

        self.create_type_group_box()
        self.create_hints_group_box()

        self.quit_button = QPushButton('&Quit', self)
        self.quit_button.clicked.connect(self.close)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.quit_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.type_group_box)
        main_layout.addWidget(self.hints_group_box)
        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)

        self.update_preview()
        pass

    def create_type_group_box(self):
        self.type_group_box = QGroupBox('Type')
        self.windowRadioButton = self.create_radio_button('Window')
        self.dialogRadioButton = self.create_radio_button("Dialog")
        self.sheetRadioButton = self.create_radio_button("Sheet")
        self.drawerRadioButton = self.create_radio_button("Drawer")
        self.popupRadioButton = self.create_radio_button("Popup")
        self.toolRadioButton = self.create_radio_button("Tool")
        self.toolTipRadioButton = self.create_radio_button("Tooltip")
        self.splashScreenRadioButton = self.create_radio_button("Splash screen")

        # set layout
        layout = QGridLayout()
        layout.addWidget(self.windowRadioButton, 0, 0)
        layout.addWidget(self.dialogRadioButton, 1, 0)
        layout.addWidget(self.sheetRadioButton, 2, 0)
        layout.addWidget(self.drawerRadioButton, 3, 0)
        layout.addWidget(self.popupRadioButton, 0, 1)
        layout.addWidget(self.toolRadioButton, 1, 1)
        layout.addWidget(self.toolTipRadioButton, 2, 1)
        layout.addWidget(self.splashScreenRadioButton, 3, 1)
        self.type_group_box.setLayout(layout)

    def create_radio_button(self, info):
        button = QRadioButton(info)
        button.clicked.connect(self.update_preview)
        return button

    def create_hints_group_box(self):
        self.hints_group_box = QGroupBox("Hints")

        self.msWindowsFixedSizeDialogCheckBox = self.create_check_box("MS Windows fixed size dialog")
        self.x11BypassWindowCheckBox = self.create_check_box("X11 bypass window manager")
        self.framelessWindowCheckBox = self.create_check_box("Frameless window")
        self.windowNoShadowCheckBox = self.create_check_box("No drop shadow")
        self.windowTitleCheckBox = self.create_check_box("Window title")
        self.windowSystemMenuCheckBox = self.create_check_box("Window system menu")
        self.windowMinimizeButtonCheckBox = self.create_check_box("Window minimize button")
        self.windowMaximizeButtonCheckBox = self.create_check_box("Window maximize button")
        self.windowCloseButtonCheckBox = self.create_check_box("Window close button")
        self.windowContextHelpButtonCheckBox = self.create_check_box("Window context help button")
        self.windowShadeButtonCheckBox = self.create_check_box("Window shade button")
        self.windowStaysOnTopCheckBox = self.create_check_box("Window stays on top")
        self.windowStaysOnBottonCheckBox = self.create_check_box("Window stays on bottom")
        self.customizeWindowHintCheckBox = self.create_check_box("Customize window")

        # set layout
        layout = QGridLayout()
        layout.addWidget(self.msWindowsFixedSizeDialogCheckBox, 0, 0)
        layout.addWidget(self.x11BypassWindowCheckBox, 1, 0)
        layout.addWidget(self.framelessWindowCheckBox, 2, 0)
        layout.addWidget(self.windowNoShadowCheckBox, 3, 0)
        layout.addWidget(self.windowTitleCheckBox, 4, 0)
        layout.addWidget(self.windowSystemMenuCheckBox, 5, 0)
        layout.addWidget(self.customizeWindowHintCheckBox, 6, 0)
        layout.addWidget(self.windowMinimizeButtonCheckBox, 0, 1)
        layout.addWidget(self.windowMaximizeButtonCheckBox, 1, 1)
        layout.addWidget(self.windowCloseButtonCheckBox, 2, 1)
        layout.addWidget(self.windowContextHelpButtonCheckBox, 3, 1)
        layout.addWidget(self.windowShadeButtonCheckBox, 4, 1)
        layout.addWidget(self.windowStaysOnTopCheckBox, 5, 1)
        layout.addWidget(self.windowStaysOnBottonCheckBox, 6, 1)

        self.hints_group_box.setLayout(layout)
        pass

    def create_check_box(self, info):
        check_box = QCheckBox(info)
        check_box.clicked.connect(self.update_preview)
        return check_box

    def update_preview(self):
        print('start update..',id(self.preview_window))
        # flags = Qt.WindowType_Mask
        flags = Qt.WindowFlags()
        print(flags)
        if self.windowRadioButton.isChecked():
            flags = Qt.Window
        elif self.dialogRadioButton.isChecked():
            flags = Qt.Dialog
        elif self.sheetRadioButton.isChecked():
            flags = Qt.Sheet
        elif self.drawerRadioButton.isChecked():
            flags = Qt.Drawer
        elif self.popupRadioButton.isChecked():
            flags = Qt.Popup
        elif self.toolRadioButton.isChecked():
            flags = Qt.Tool
        elif self.toolTipRadioButton.isChecked():
            flags = Qt.ToolTip
        elif self.splashScreenRadioButton.isChecked():
            flags = Qt.SplashScreen

        if self.msWindowsFixedSizeDialogCheckBox.isChecked():
            flags |= Qt.MSWindowsFixedSizeDialogHint
        if self.x11BypassWindowCheckBox.isChecked():
            flags |= Qt.X11BypassWindowManagerHint
        if self.framelessWindowCheckBox.isChecked():
            flags |= Qt.FramelessWindowHint
        if self.windowNoShadowCheckBox.isChecked():
            flags |= Qt.NoDropShadowWindowHint
        if self.windowTitleCheckBox.isChecked():
            flags |= Qt.WindowTitleHint
        if self.windowSystemMenuCheckBox.isChecked():
            flags |= Qt.WindowSystemMenuHint
        if self.windowMinimizeButtonCheckBox.isChecked():
            flags |= Qt.WindowMinimizeButtonHint
        if self.windowMaximizeButtonCheckBox.isChecked():
            flags |= Qt.WindowMaximizeButtonHint
        if self.windowCloseButtonCheckBox.isChecked():
            flags |= Qt.WindowCloseButtonHint
        if self.windowContextHelpButtonCheckBox.isChecked():
            flags |= Qt.WindowContextHelpButtonHint
        if self.windowShadeButtonCheckBox:
            flags |= Qt.WindowShadeButtonHint
        if self.windowStaysOnTopCheckBox.isChecked():
            flags |= Qt.WindowStaysOnTopHint
        if self.windowStaysOnBottonCheckBox.isChecked():
            flags |= Qt.WindowStaysOnBottomHint
        if self.customizeWindowHintCheckBox.isChecked():
            flags |= Qt.CustomizeWindowHint

        self.preview_window.set_Window_Flags(flags)
        print(id(self.preview_window))
        pos = self.preview_window.pos()
        if pos.x() < 0:
            pos.setX(0)
        if pos.y() < 0:
            pos.setY(0)
        self.preview_window.move(pos)
        self.preview_window.show()
        pass


class PreviewWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        closeButton = QPushButton('&Close')
        closeButton.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(closeButton)
        self.setLayout(layout)
        self.setWindowTitle('Preview')


    def set_Window_Flags(self, flags):
        print('-' * 10)
        text = ''
        self.setWindowFlags(flags)
        #  Qt::WindowFlags type = (flags & Qt::WindowType_Mask);
        type1 = flags & Qt.WindowType_Mask

        if type1 == Qt.Window:
            text = "Qt.Window"
        elif type1 == Qt.Dialog:
            text = "Qt.Dialog"
        elif type1 == Qt.Sheet:
            text = "Qt.Sheet"
        elif type1 == Qt.Drawer:
            text = "Qt.Drawer"
        elif type1 == Qt.Popup:
            text = "Qt.Popup"
        elif type1 == Qt.Tool:
            text = "Qt.Tool"
        elif type1 == Qt.ToolTip:
            text = "Qt.ToolTip"
        elif type1 == Qt.SplashScreen:
            text = "Qt.SplashScreen"

        if flags & Qt.MSWindowsFixedSizeDialogHint:
            text += '\n| Qt.MSWindowsFixedSizeDialogHint'
        if flags & Qt.X11BypassWindowManagerHint:
            text += '\n| Qt.X11BypassWindowManagerHint'
        if flags & Qt.FramelessWindowHint:
            text += '\n| Qt.FramelessWindowHint'
        if flags & Qt.NoDropShadowWindowHint:
            text += '\n| Qt.NoDropShadowWindowHint'
        if flags & Qt.WindowTitleHint:
            text += '\n| Qt.WindowTitleHint'
        if flags & Qt.WindowSystemMenuHint:
            text += '\n| Qt.WindowSystemMenuHint'
        if flags & Qt.WindowMinimizeButtonHint:
            text += '\n| Qt.WindowMinimizeButtonHint'
        if flags & Qt.WindowMaximizeButtonHint:
            text += '\n| Qt.WindowMaximizeButtonHint'
        if flags & Qt.WindowCloseButtonHint:
            text += '\n| Qt.WindowCloseButtonHint'
        if flags & Qt.WindowContextHelpButtonHint:
            text += '\n| Qt.WindowContextHelpButtonHint'
        if flags & Qt.WindowShadeButtonHint:
            text += '\n| Qt.WindowShadeButtonHint'
        if flags & Qt.WindowStaysOnTopHint:
            text += '\n| Qt.WindowStaysOnTopHint'
        if flags & Qt.WindowStaysOnBottomHint:
            text += '\n| Qt.WindowStaysOnBottomHint'
        if flags & Qt.CustomizeWindowHint:
            text += '\n| Qt.CustomizeWindowHint'
        print('text is :', text)
        self.textEdit.setText(text)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = ControllerWindow()
    w.show()
    sys.exit(app.exec_())