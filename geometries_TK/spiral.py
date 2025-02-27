import numpy as np

def construct_spiral( R, X, Y, Z, N ):
    #   Function to construct a circular geometry. The function receives: Radius(R), (x,y,z) positions (ant_x,ant_y,Z)
    #   Folder name where it has to save the geometry (folder_name) and the section name (sec) to differentiate from other 
    #   Circular antennas.
    
    coordinates = set()
    num_points = 4000
    theta_step = N*np.pi/num_points
    k = R/(N*np.pi)

    for i in range( num_points ):
        theta = i*theta_step
        r = k*theta

        #computes the radial position of the antenna, 
        #given the radius and the antenna center position
        x = round( X + r * np.cos(theta) )
        y = round( Y + r * np.sin(theta) )
        z = round( Z )

        coordinates.add( (x,y,z) ) 

    coordinates = np.array( list(coordinates) )
    
    return coordinates


