# Developer: Luis Carlos Herrera Quesada
# Date: 05/12/2024
# Universität Stuttgart
#  
#Main file for antenna modeling, calls the other functions to construct, plot and save 
#the antenna values that wil be used in the FHELI code.
#Antennas are always directed in the z axis

from GUI import HelicalAntennaDesigner

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = HelicalAntennaDesigner()
    window.show()

    # Run the application event loop
    sys.exit(app.exec())
