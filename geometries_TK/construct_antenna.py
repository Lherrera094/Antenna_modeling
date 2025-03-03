#   Functions wrapps the coordinates created from the circular, helic and linear files to 
#   create the full structure of antennas.
import sys

sys.path.append("geometries_TK/")

from spiral import construct_spiral
from circular import *
from helic import *
from linear import construct_linear

import numpy as np

def assembly_antenna( antenna_index, parameters ):

    R = parameters["Radius"]
    X = parameters["X_position (center)"]
    Y = parameters["Y_position (center)"]
    Z = parameters["Z_position (center)"]

    #   Ensemble Singular Circular antenna
    if antenna_index == 0: 
        circular_coord =     construct_circular( R, X, Y, Z )
        return {"Section_1": circular_coord}

    #   Ensemble Singular Circular antenna
    elif antenna_index == 1:
        num_turn = parameters["Number of Turns"]
        spiral_coord =      construct_spiral( R, X, Y, Z, num_turn )
        return {"Section_1":spiral_coord}
    
    #   Ensemble Double Circular antenna
    elif antenna_index == 2:
        #   get necessary values.
        L = parameters["Lenght"]

        circular_coord_1 =  construct_circular( R, X, Y, round(Z-(L/2)) )
        circular_coord_2 =  construct_circular( R, X, Y, round(Z+(L/2)) )
        return {"Section_1":circular_coord_1,
                "Section_2":circular_coord_2}
    
    #   Ensemble Nagoya antenna
    elif antenna_index == 3:
        #   get necessary values.
        L = parameters["Lenght"]
        X1 = round( X + R*np.cos(0) )
        Y1 = round( Y + R*np.sin(0) )

        X2 = round( X + R*np.cos(np.pi) )
        Y2 = round( Y + R*np.sin(np.pi) )

        circular_coord_1 =  construct_circular( R, X, Y, round(Z-(L/2)) )
        circular_coord_2 =  construct_circular( R, X, Y, round(Z+(L/2)) )

        linear_coord_1 =    construct_linear( X1, Y1, round(Z-(L/2)), round(Z+(L/2)) )
        linear_coord_2 =    construct_linear( X2, Y2, round(Z-(L/2)), round(Z+(L/2)) )
        return {"Section_1":    circular_coord_1,
                "Section_2":    circular_coord_2,
                "Section_3":    linear_coord_1,
                "Section_4":    linear_coord_2 }
    
    #   Ensemble Boswell antenna
    elif antenna_index == 4:
        #   get necessary values.
        L = parameters["Lenght"]
        X1 = round( X + R*np.cos(np.pi/4) )
        Y1 = round( Y + R*np.sin(np.pi/4) )

        X3 = round( X + R*np.cos(3*np.pi/4) )
        Y3 = round( Y + R*np.sin(3*np.pi/4) )

        X4 = round( X + R*np.cos(5*np.pi/4) )
        Y4 = round( Y + R*np.sin(5*np.pi/4) )

        X2 = round( X + R*np.cos(7*np.pi/4) )
        Y2 = round( Y + R*np.sin(7*np.pi/4) ) 

        circular_coord_1 =  construct_circular_portion( R, X, Y, round(Z-(L/2)) )
        circular_coord_2 =  construct_circular_portion( R, X, Y, round(Z+(L/2)) )

        linear_coord_1 =    construct_linear( X1, Y1, round(Z-(L/2)), round(Z+(L/2)) )
        linear_coord_2 =    construct_linear( X2, Y2, round(Z-(L/2)), round(Z+(L/2)) )
        linear_coord_3 =    construct_linear( X3, Y3, round(Z-(L/2)), round(Z+(L/2)) )
        linear_coord_4 =    construct_linear( X4, Y4, round(Z-(L/2)), round(Z+(L/2)) )

        return {"Section_1":    circular_coord_1,
                "Section_2":    circular_coord_2,
                "Section_3":    linear_coord_1,
                "Section_4":    linear_coord_2,
                "Section_5":    linear_coord_3,
                "Section_6":    linear_coord_4 }
    
    #   Ensemble RH-Helical antenna
    elif antenna_index == 5:
        #   get necessary values.
        L = parameters["Lenght"]
        num_turn = parameters["Number of Turns"]

        circular_coord_1 =  construct_circular( R, X, Y, round(Z-(L/2)) )
        circular_coord_2 =  construct_circular( R, X, Y, round(Z+(L/2)) )

        helic_coord_1 =    right_helical( X, Y, round(Z-(L/2)), round(Z+(L/2)), num_turn, R, 1 )
        helic_coord_2 =    left_helical( X, Y, round(Z-(L/2)), round(Z+(L/2)), num_turn, R, 1 )

        return {"Section_1":    circular_coord_1,
                "Section_2":    circular_coord_2,
                "Section_3":    helic_coord_1,
                "Section_4":    helic_coord_2 }
    
    #   Ensemble LH-Helical antenna
    elif antenna_index == 6:
        #   get necessary values.
        L = parameters["Lenght"]
        num_turn = parameters["Number of Turns"]

        circular_coord_1 =  construct_circular( R, X, Y, round(Z-(L/2)) )
        circular_coord_2 =  construct_circular( R, X, Y, round(Z+(L/2)) )

        helic_coord_1 =    right_helical( X, Y, round(Z-(L/2)), round(Z+(L/2)), num_turn, R, -1 )
        helic_coord_2 =    left_helical( X, Y, round(Z-(L/2)), round(Z+(L/2)), num_turn, R, -1 )

        return {"Section_1":    circular_coord_1,
                "Section_2":    circular_coord_2,
                "Section_3":    helic_coord_1,
                "Section_4":    helic_coord_2 }
    
    #   Ensemble Birdcage antenna
    elif antenna_index == 7:
        #   get necessary values.
        L = parameters["Lenght"]
        num_arm = int(parameters["Number of Arms"])

        circular_coord_1 =  construct_circular( R, X, Y, round(Z-(L/2)) )
        circular_coord_2 =  construct_circular( R, X, Y, round(Z+(L/2)) )

        sections = {"Section_1":   circular_coord_1,
                    "Section_2":   circular_coord_2}

        for i in range(num_arm):
            theta = i*(2*np.pi/num_arm)
            X1 = round( X + R*np.cos(theta) )
            Y1 = round( Y + R*np.sin(theta) )

            section_name = f"Section_{i+3}"
            sections[section_name] =    construct_linear( X1, Y1, round(Z-(L/2)), round(Z+(L/2)) )

        return sections
    