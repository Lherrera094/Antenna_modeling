import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWebEngineWidgets import QWebEngineView  # Import QWebEngineView

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
    QComboBox,
)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from geometries_TK.construct_antenna import *
from utils.file_utils import *
from utils.plot_functions import plot_antenna


class HelicalAntennaDesigner(QMainWindow):

    def __init__(self):
        #   Initialize the window and runs each function.

        super().__init__()

        # Set window title and size
        self.setWindowTitle("Helical Antenna Designer for FHELI")
        self.setGeometry(100, 100, 500, 300)

        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Add an image to the main window
        self.add_image("utils/cat.jpg")  # Replace with your image file path

        # Dropdown for geometry selection
        # Dropdown for antenna selection
        self.label_antenna = QLabel("Select Antenna Type:")
        self.layout.addWidget(self.label_antenna)
        self.combo_antenna = QComboBox()
        self.combo_antenna.addItems([  "Single-Loop", "Spiral",
                                       "Double-Loop", "Nagoya_Type-III", "Boswell", 
                                       "RH-Helical", "LH-Helical", 
                                       "Birdcage" ])
        self.combo_antenna.currentIndexChanged.connect(self.update_parameters)
        self.layout.addWidget(self.combo_antenna)

        # Container for dynamic parameter fields
        self.parameter_widgets = QWidget()
        self.parameter_layout = QVBoxLayout(self.parameter_widgets)
        self.layout.addWidget(self.parameter_widgets)

        # Button to trigger design generation
        self.button_design = QPushButton("Generate Design")
        self.button_design.clicked.connect(self.generate_design)
        self.layout.addWidget(self.button_design)

        # Initialize parameter fields for the first antenna
        self.update_parameters()

    def add_image(self, image_path):    
        #   Add an image to the main window.

        # Create a QLabel to hold the image
        image_label = QLabel(self)
        pixmap = QPixmap(image_path)

        # Resize the image if necessary (optional)
        pixmap = pixmap.scaled(500, 400)  # Adjust width and height as needed

        # Set the pixmap to the QLabel
        image_label.setPixmap(pixmap)

        # Add the QLabel to the layout
        self.layout.addWidget(image_label)

    def update_parameters(self):
        #   Update the displayed parameters based on the selected antenna.
        parameters = [ "Radius", "X_position (center)", "Y_position (center)", "Z_position (center)" ]

        # Clear existing parameter fields
        for i in reversed(range(self.parameter_layout.count())):
            self.parameter_layout.itemAt(i).widget().setParent(None)

        # Get the required parameters for the selected antenna
        antenna_index = self.combo_antenna.currentIndex()
        #   Return the required parameters for Circular antenna type.
        if antenna_index == 0:
            parameters = [ "Radius", "X_position (center)", "Y_position (center)", "Z_position (center)"]
        
        #   Return the required parameters for Spiral antenna type.
        elif antenna_index == 1:
            parameters = [ "Radius", "X_position (center)", "Y_position (center)", "Z_position (center)", "Number of Turns" ]

        #   Return the required parameters for Boswell, double-loop and Nagoya antenna.
        elif antenna_index == 2 or antenna_index == 3 or antenna_index == 4:
            parameters = [ "Radius", "Lenght", "X_position (center)", "Y_position (center)", "Z_position (center)" ]

        #   Return the required parameters for RH and LH helical antenna.
        elif antenna_index == 5 or antenna_index == 6:
            parameters = [ "Radius", "Lenght", "X_position (center)", "Y_position (center)", "Z_position (center)", "Number of Turns" ]
        
        #   Return the required parameters for RBirdcage antenna.
        elif antenna_index == 7:
            parameters = [ "Radius", "Lenght", "X_position (center)", "Y_position (center)", "Z_position (center)", "Number of Arms" ]
        
        # Create input fields for each parameter
        self.input_fields = {}
        for param in parameters:
            label = QLabel(f"{param.capitalize()}:")
            self.parameter_layout.addWidget(label)
            input_field = QLineEdit()
            self.parameter_layout.addWidget(input_field)
            self.input_fields[param] = input_field

    def generate_design(self):
        try:
            # Get input values
            parameters = {}
            for param, input_field in self.input_fields.items():
                parameters[param] = float(input_field.text())

            # Get selected antenna
            antenna_index = self.combo_antenna.currentIndex()
            sections = assembly_antenna( antenna_index, parameters)
            
            # Save sections to files
            directory = QFileDialog.getExistingDirectory(self, "Select Directory")
            if directory:
                for section_name, coordinates in sections.items():
                    save_section(coordinates, directory, section_name)
                 
                #save input parameters    
                save_input_params(parameters, directory)
                QMessageBox.information(self, "Success", "All sections saved successfully.")

            # Plot the combined antenna using Plotly
            plot_antenna(sections, self)

        except ValueError:
            QMessageBox.critical(self, "Error", "Please enter valid numbers")


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelicalAntennaDesigner()
    window.show()
    sys.exit(app.exec())

