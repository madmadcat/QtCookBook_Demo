import sys
from PyQt5.QtWidgets import QApplication
from diggingold import Gold



if __name__ == "__main__":
    app = QApplication(sys.argv)
    gold = Gold()
    gold.show()
    sys.exit(app.exec_())