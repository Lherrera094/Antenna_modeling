import numpy as np

def right_helical( X, Y, Z_0, Z_1, num_turns, R, chirality ):

    #   Function to construct a right-handed helical geometry. The function receives: Radius(R), 
    #   (x,y,z0,z1) positions (ant_x,ant_y,Z_0,Z_1), number of turns (num_turns), chirality,
    #   Folder name where it has to save the geometry (folder_name) 
    #   and the section name (sec) to differentiate from other helical sections.

    pitch = (Z_1 - Z_0)/(num_turns)
    coordinates = set()
    num_points = 4000
    theta_step = 2*np.pi/num_points

    for i in range( round(num_turns*num_points) ):

        theta = i*theta_step
        x = round( X + R * np.cos(chirality * theta) )
        y = round( Y + R * np.sin(chirality * theta) )
        z = round( Z_0 + ( pitch * (i)/( num_points ) ) )

        coordinates.add( (x,y,z) ) 

    coordinates = np.array( list(coordinates) )

    return coordinates

def left_helical( X, Y, Z_0, Z_1, num_turns, R, chirality ):

    #   Function to construct a left-handed helical geometry. The function receives: Radius(R), 
    #   (x,y,z0,z1) positions (ant_x,ant_y,Z_0,Z_1), number of turns (num_turns), chirality,
    #   Folder name where it has to save the geometry (folder_name) 
    #   and the section name (sec) to differentiate from other helical sections.

    pitch = (Z_1 - Z_0)/(num_turns)
    coordinates = set()
    num_points = 4000
    theta_step = 2*np.pi/num_points

    for i in range( round(num_turns*num_points) ):

        theta = i*theta_step
        x = round( X + R * np.cos( (chirality * theta) + np.pi) )
        y = round( Y + R * np.sin( (chirality * theta) + np.pi) )
        z = round( Z_0 + ( pitch * (i)/( num_points ) ) )

        coordinates.add( (x,y,z) ) 

    coordinates = np.array( list(coordinates) )

    return coordinates

