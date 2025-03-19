import sys
import random
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon, QFont

# M ILHAM ABDUL SHALEH
# F1D022061


class CatchAGhost(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Catch a Ghost")
        self.setGeometry(350, 350, 750, 600)

        # Load and set window icon
        pixmap_icon = QPixmap("asset/icon.svg").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setWindowIcon(QIcon(pixmap_icon))

        # Main layout
        main_layout = QVBoxLayout()

        # Title label
        self.title_label = QLabel("Catch a Ghost", self)
        self.title_label.setFont(QFont("Arial", 24, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)

        # Ghost
        self.ghost_label = QLabel(self)
        self.ghost_pixmap = QPixmap("asset/ghost.svg")
        self.ghost_label.setPixmap(self.ghost_pixmap)
        self.ghost_label.setFixedSize(150, 150)

        # Coordinate
        self.coord_label = QLabel("[0, 0]", self)
        self.coord_label.setFont(QFont("Arial", 10))  # Smaller font size
        self.coord_label.setStyleSheet("background-color: white; border: 1px solid black; padding: 3px;")
        self.coord_label.setFixedSize(150, 40)  # Adjusted size

        # Add widgets to layout
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(self.ghost_label)
        main_layout.addWidget(self.coord_label)

        self.setLayout(main_layout)

        # Tracking mouse
        self.setMouseTracking(True)
        self.ghost_label.setMouseTracking(True)
        self.coord_label.setMouseTracking(True)

        # Event filter
        self.ghost_label.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.ghost_label and event.type() == event.Enter:
            self.moveGhostRandomly()
        return super().eventFilter(obj, event)

    def moveGhostRandomly(self):
        max_x = max(0, self.width() - self.ghost_label.width())
        max_y = max(0, self.height() - self.ghost_label.height())
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.ghost_label.move(new_x, new_y)
        self.coord_label.move(new_x + 110, new_y + 30)

    def mouseMoveEvent(self, event):
        # Update coordinate
        self.coord_label.setText(f"[{event.x()}, {event.y()}]")
        super().mouseMoveEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CatchAGhost()
    window.show()
    sys.exit(app.exec())