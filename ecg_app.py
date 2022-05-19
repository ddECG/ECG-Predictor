# -----------------------------------------------------------------------------
# Project: ECG predictor
#
# What: A application to predict age from a ECG file.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication
from modules.user_interface import MainWindow

# ------------------------------------------------------------- #
# 2 - Application start                                         #
# ------------------------------------------------------------- #
if __name__ == "__main__":
    # Create application
    app = QApplication(sys.argv)

    # Change style
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon(':/Logo/icon.icon'))

    # Show GUI window
    window = MainWindow()
    window.show()

    # App execute/loop
    sys.exit(app.exec_())