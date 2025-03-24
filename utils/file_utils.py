#   Set of functions to support different characteristics of the GUI for helical 
#   Antenna design

def save_section(coordinates, directory, section_name):
    """
    Save a section's coordinates to a .txt file.
    """
    file_path = f"{directory}/{section_name}.txt"
    with open(file_path, "w") as file:
        for coord in coordinates:
            file.write(f"{coord[0]}, {coord[1]}, {coord[2]}\n")
    return file_path
    
def save_input_params(parameters, directory):
    file_path = f"{directory}/Input_Parameters.txt"
    with open(file_path, "w") as file:
        for param, value in parameters.items():
            file.write(f"{param}: {value}\n")
    return file_path
    
    
