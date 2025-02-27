import numpy as np

def construct_linear( X, Y, Z_0, Z_1 ):

    #   Function to construct a linear geometry. The function receives: (x,y,z0,z1) positions (ant_x,ant_y,Z_0,Z_1)
    #   Folder name where it has to save the geometry (folder_name) and the section name (sec) to differentiate from other 
    #   linear antennas.
    
    coordinates = set()

    for i in range(0, int(Z_1-Z_0) + 1 ):
        x = round( X )
        y = round( Y )
        z = round( Z_0 + i )
        coordinates.add( (x,y,z) )

    coordinates = np.array( list(coordinates) )

    return coordinates

