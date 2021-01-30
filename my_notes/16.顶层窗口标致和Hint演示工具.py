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

        # set layout
        layout = QGridLayout()
        layout.addWidget(self.windowRadioButton, 0, 0)

        self.type_group_box.setLayout(layout)
        pass

    def create_radio_button(self, info):
        button = QRadioButton(info)
        button.clicked.connect(self.update_preview)
        return button

    def create_hints_group_box(self):
        self.hints_group_box = QGroupBox("Hints")

        self.msWindowsFixedSizeDialogCheckBox = self.create_check_box("MS Windows fixed size dialog")

        # set layout
        layout = QGridLayout()
        layout.addWidget(self.msWindowsFixedSizeDialogCheckBox, 0, 0)

        self.hints_group_box.setLayout(layout)
        pass

    def create_check_box(self, info):
        check_box = QCheckBox(info)
        check_box.clicked.connect(self.update_preview)
        return check_box

    def update_preview(self):
        print('start update..',id(self.preview_window))
        flags = Qt.WindowType_Mask
        if self.windowRadioButton.isChecked():
            flags = Qt.Window
        if self.msWindowsFixedSizeDialogCheckBox.isChecked():
            flags |= Qt.MSWindowsFixedSizeDialogHint

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
        type1 = (flags & Qt.WindowType_Mask)

        if type1 == Qt.Window:
            text = "Qt.Window"

        if (flags & Qt.MSWindowsFixedSizeDialogHint):
            text += '\n| Qt.MSWindowsFixedSizeDialogHint'

        self.textEdit.setText(text)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = ControllerWindow()
    w.show()
    sys.exit(app.exec_())