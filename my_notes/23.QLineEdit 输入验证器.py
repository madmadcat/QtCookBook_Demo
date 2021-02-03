import sys

from PyQt5.Qt import *


class AgeValidator(QValidator):
    """
    子类化，然后实现两个方法,同样适用于浮点类型，还可以封装上下限参数，更加灵活
    TODO: 封装上下限参数，更加灵活
    """
    def validate(self, input_str, point_int):
        """

        :param input_str: 输入的文本
        :param point_int: 光标位置
        :return:
        """
        print(input_str, point_int)
        # 首先应当判定输入内容是int


        try:
            if 180 >= int(input_str) >= 18:
                return (QValidator.Acceptable, input_str, point_int)
            elif 17 >= int(input_str) >= 1:
                return (QValidator.Intermediate, input_str, point_int)
            else:
                return (QValidator.Invalid, input_str, point_int)
        except:
            if len(input_str) == 0:
                return (QValidator.Intermediate, input_str, point_int)
            return (QValidator.Invalid, input_str, point_int)

    def fixup(self, p_str):
        """
        如果输入无效，且离开输入框，就会进入fixup方法
        :param p_str:
        :return:
        """
        try:
            print('www', p_str)
            if int(p_str) < 18:
                return "18"
            return "180"
        except:
            return "18"

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("验证器")
        self.resize(400, 400)
        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100, 100)

        # 验证器逻辑
        # 18-180 年龄验证

        validator = AgeValidator()
        le.setValidator(validator)

        le2 = QLineEdit(self)
        le2.move(200, 200)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
