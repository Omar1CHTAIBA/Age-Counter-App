from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.admit.clicked.connect(self.search_click)

    def settings(self):
        self.setWindowTitle('Age App')
        self.setGeometry(250, 250, 470, 550)

    def initUI(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1F1F1F;
                color: #B0B0B0;
                font-family: 'Helvetica Neue', sans-serif;
            }
            QLabel#title {
                font-size: 48px;
                margin-bottom: 20px;
                color: #00BFFF;
                text-align: center;
                font-weight: bold;
            }
            QLabel {
                font-size: 18px;
                margin: 10px;
                color: #B0B0B0;
            }
            QLineEdit {
                padding: 12px;
                border: 2px solid #00BFFF;
                border-radius: 8px;
                background-color: #2F2F2F;
                color: #FFFFFF;
            }
            QLineEdit:focus {
                border: 2px solid #1E90FF;
                background-color: #3F3F3F;
            }
            QPushButton {
                background-color: #00BFFF;
                color: #1F1F1F;
                padding: 12px;
                border: none;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            QPushButton:hover {
                background-color: #1E90FF;
            }
            QLabel#output {
                font-size: 20px;
                margin: 20px;
                padding: 20px;
                border: 2px solid #00BFFF;
                border-radius: 12px;
                background-color: #2F2F2F;
                min-height: 120px;
                color: #B0B0B0;
                line-height: 1.5;
                text-align: left;
                font-family: 'Helvetica Neue', sans-serif;
                font-weight: 500;
            }
        """)
        self.title = QLabel('Age App')
        self.title.setObjectName("title")
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter your age ...")

        self.output = QLabel("Age information")
        self.output.setObjectName("output")
        self.admit = QPushButton("Admit")

        self.master = QVBoxLayout()
        self.master.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        self.master.addWidget(self.input_box)
        self.master.addWidget(self.output)
        self.master.addWidget(self.admit)

        self.master.setSpacing(20)
        self.setLayout(self.master)

    def search_click(self):
        age = self.input_box.text()
        if age:
            self.results = self.get_age(age)
        else:
            self.results = "Please type your age."
        self.output.setText(self.results)

    def get_age(self, age):
        try:
            age = int(age)  # Convert the input to an integer

            months = age * 12
            weeks = months * 4
            days = age * 365
            hours = days * 24
            minutes = hours * 60
            seconds = minutes * 60

            full_data = (
                f"You have lived for:\n"
                f"Months: {months} months\n"
                f"Weeks: {weeks} weeks\n"
                f"Days: {days} days\n"
                f"Hours: {hours} hours\n"
                f"Minutes: {minutes} minutes\n"
                f"Seconds: {seconds} seconds\n"
            )
            return full_data
        except ValueError:
            return "Please enter a valid integer for age."
        except Exception as e:
            return f"An error occurred: {e}"

if __name__ == '__main__':
    app = QApplication([])
    main = Window()
    main.show()
    app.exec()
