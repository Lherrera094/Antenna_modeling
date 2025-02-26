import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
    QMessageBox,
)


class ParameterCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Antenna Modelling for FOCAL")
        self.setGeometry(100, 100, 300, 200)

        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Input fields for parameters
        self.label_param1 = QLabel("Parameter 1:")
        self.layout.addWidget(self.label_param1)
        self.entry_param1 = QLineEdit()
        self.layout.addWidget(self.entry_param1)

        self.label_param2 = QLabel("Parameter 2:")
        self.layout.addWidget(self.label_param2)
        self.entry_param2 = QLineEdit()
        self.layout.addWidget(self.entry_param2)

        # Button to trigger calculation
        self.button_calculate = QPushButton("Calculate")
        self.button_calculate.clicked.connect(self.calculate)
        self.layout.addWidget(self.button_calculate)

        # Label to display the result
        self.label_result = QLabel("Result: ")
        self.layout.addWidget(self.label_result)

    def calculate(self):
        try:
            # Get input values
            param1 = float(self.entry_param1.text())
            param2 = float(self.entry_param2.text())

            # Perform calculation (example: sum of parameters)
            result = param1 + param2

            # Display result
            self.label_result.setText(f"Result: {result}")

            # Save result to file
            self.save_result(result)
        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter valid numbers")

    def save_result(self, result):
        # Open a file dialog to select the directory
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")

        if directory:
            # Create a file path
            file_path = f"{directory}/result.txt"

            # Write the result to the file
            with open(file_path, "w") as file:
                file.write(f"Result: {result}")

            # Show a success message
            QMessageBox.information(self, "Success", f"Result saved to {file_path}")


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParameterCalculator()
    window.show()
    sys.exit(app.exec())