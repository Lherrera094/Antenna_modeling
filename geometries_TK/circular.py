import numpy as np

def construct_circular( R, X, Y, Z ):
    #   unction to construct a circular geometry. The function receives: Radius(R), (x,y,z) positions (ant_x,ant_y,Z)
    #   Folder name where it has to save the geometry (folder_name) and the section name (sec) to differentiate from other 
    #   Circular antennas.
    
    coordinates = set()
    num_points = 4000
    theta_step = 2*np.pi/num_points

    for i in range( num_points ):
        theta = i*theta_step

        #computes the radial position of the antenna, 
        #given the radius and the antenna center position
        x = round( X + R * np.cos(theta) )
        y = round( Y + R * np.sin(theta) )
        z = round( Z )

        coordinates.add( (x,y,z) ) 

    coordinates = np.array( list(coordinates) )
    
    return coordinates


