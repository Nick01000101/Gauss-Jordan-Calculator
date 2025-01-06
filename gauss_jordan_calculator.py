import random
import copy
import os
import time
import sys
# -----------------------------------------------------------------------------
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ----------Gauss-Jordan-Eliminaton-calculator---------------------------------
# ------------------------------------------------Written by Nick Sevostiyanov-
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# -----------------------------------------------------------------------------


#    ___                       __                _              
#   / _ \__ _ _   _ ___ ___    \ \  ___  _ __ __| | __ _ _ __   
#  / /_\/ _` | | | / __/ __|    \ \/ _ \| '__/ _` |/ _` | '_ \  
# / /_\\ (_| | |_| \__ \__ \ /\_/ / (_) | | | (_| | (_| | | | | 
# \____/\__,_|\__,_|___/___/ \___/ \___/|_|  \__,_|\__,_|_| |_| 

#    _____      _            _       _             
#   / ____|    | |          | |     | |            
#  | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
#  | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
#  | |___| (_| | | (__| |_| | | (_| | || (_) | |   
#   \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                                                               

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ----------------------------Defined-Functions--------------------------------
        # Clears screen
        
def clear_screen():
    # For windows
    if os.name == 'nt':
        os.system('cls')
    else:
        # For Unix/Linux/Mac
        os.system('clear')
# -----------------------------------------------------------------------------
        # Loading icon

def show_loading(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            sys.stdout.write('\rloading' + '.' * i)
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write('\rDone!        \n')
# -----------------------------------------------------------------------------
        # Random Num Generator

    # Generates random Int in range(arg):
def math_random_small_int(small=True, medium=True, big=True):
    if small and not medium and not big:
        return random.randint(0, 15)
    if not small and medium and not big:
        return random.randint(15, 30)
    if not small and not medium and big:
        return random.randint(30, 100)
# -----------------------------------------------------------------------------
            # Matrix Generator

        # - Takes dimensions
        # - Registers values per row @ gets determinant
        # - Appends equations into lists ({row:[values]})
        # Returns Matrix (Dict)
def linear_equation(unknown, row):
    unknown = int(unknown)
    row = int(row)
    if unknown > 0:
        fullequations = {}
        clear_screen()
        for rownum in range(1, row + 1):
            print(f"Currently on row {rownum}!")
            equations = []
            for colnum in range(1, unknown + 2):
                if colnum == unknown + 1:
                    determinant = input('Determinant of matrix = ')
                    equations.append(determinant)
                else:
                    equations.append(input(f'Input equation in column {colnum} of the matrix: '))
            clear_screen()
            fullequations[f"row{rownum}"] = equations
        return fullequations
# -----------------------------------------------------------------------------
        # Column elimination

    # Turns Columns in Pivot into 0's
def col_elimination(equations, operation):
    pivot_row = equations[f"row{operation + 1}"]
    
    for row_num, row in equations.items():
        if row_num != f"row{operation + 1}":
            pivot_element = float(row[operation])
            
            if pivot_element != 0:
                for i in range(len(row)):
                    row[i] = float(row[i]) - pivot_element * float(pivot_row[i])
    return equations
# -----------------------------------------------------------------------------
        # Row normalization (with pivot checking)

    # Divides row by Pivot Position
    # Returns Matrix
def row_normalization(matrix, row):
    dictrow = row + 1
    pivot = matrix[f"row{dictrow}"][row]
    
    if float(pivot) == 0:
        raise ValueError("\nSPECIAL CASE!\nPivot element is zero, cannot normalize the row.\n")
    
    pivot = float(pivot)
    
    for index in range(len(matrix[f"row{dictrow}"])):
        matrix[f"row{dictrow}"][index] = float(matrix[f"row{dictrow}"][index]) / pivot

    return matrix
# -----------------------------------------------------------------------------
        # Row swapping function 
        
    # partial pivoting
def swap_rows(matrix, row1, row2):
    matrix[f"row{row1}"], matrix[f"row{row2}"] = matrix[f"row{row2}"], matrix[f"row{row1}"]
    return matrix
# -----------------------------------------------------------------------------
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ----------------------------Calculator-Menu----------------------------------


while True:
# -----------------------------------------------------------------------------
            # Gives Tutorial
    needs_help = input('Would you like a tutorial? (Y/N): ')
# -----------------------------------------------------------------------------
            # MATRIX DIMENSIONS
    
        # Dimensions passed to Matrix generator 
        # linear_equations(columns, rows)
    unknown_size = input('Number of unknown variables\n(3 = A, B, C)\n(2 = A, B)\netc..\nInput: ')
    row_size = input('Number of rows in matrix: ')
    equations = linear_equation(unknown_size, row_size)
# -----------------------------------------------------------------------------
            # Copies Matrix, adds Suffixes

        # Suffixes E.G (3A, 2B, 5C)
    equationscopy = copy.deepcopy(equations)
    # show_loading(3)
    print('\nCURRENT MATRIX:\n')

    original_suffixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    determinantcounter = 0
    for key in equationscopy:
        suffixes = original_suffixes.copy()
        for i in range(len(equationscopy[key]) - 1):
            if not suffixes:
                suffixes = original_suffixes.copy()
            equationscopy[key][i] = equationscopy[key][i] + suffixes.pop(0).upper()
        determinantcounter += 1
        equationscopy[key][-1] = (f"Det{determinantcounter} = {equationscopy[key][-1]}")
# -----------------------------------------------------------------------------
            # Current matrix

        # Prints copied matrix with suffixes
    for systemsofequations in equationscopy.values():
        print(systemsofequations)
# -----------------------------------------------------------------------------
            # Beginning functions


        # Passes Clean matrix to functions
    print('\nBeginning elementary row operations!')
    
    for operation in range(0, len(equations), 1):
        clear_screen()
        print('\nCURRENT MATRIX:\n')
        for systemsofequations in equationscopy.values():
            print(systemsofequations)
        print('')

        try:
            equations = row_normalization(equations, operation)
        except ValueError:
            # If pivot element is zero, swap with a lower row and try again
            if operation + 2 <= len(equations):
                equations = swap_rows(equations, operation + 1, operation + 2)
                equations = row_normalization(equations, operation)
            else:
                raise ValueError("SPECIAL CASE!")
                raise ValueError("Unable to normalize row, no non-zero pivot available.")

        time.sleep(1)        
        print(f"Matrix row{operation + 1} reduced by pivot position!")
        for systemsofequations in equations.values():
            print(systemsofequations)

        time.sleep(1)        
        equations = col_elimination(equations, operation)
        print(f"Matrix column{operation + 1} reduced by pivot row!")
        for systemsofequations in equations.values():
            print(systemsofequations)
    
    # -----------------------------------------------------------------------------
                # Prints final Gauss Jordan Matrix

            # Appends suffixes
    def print_last_items(equations):
        suffixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for index, (key, value) in enumerate(equations.items()):
            if index < len(suffixes):
                suffix = suffixes[index]
            else:
                suffix = suffixes[index % len(suffixes)]
            print(f"{suffix} = {value[-1]}")



    clear_screen()

# ----------------------------Operations-Done!------------------------------------

    print('\nFINAL MATRIX:\n')


    show_loading(3)
    clear_screen()

    print('\nORIGINAL MATRIX:')
    for systemsofequations in equationscopy.values():
        print(systemsofequations)
    print('\nFINAL MATRIX:\n')

    for final in equations.values():
        print(final)

    print('\nTherefor: \n')
    print_last_items(equations)
    print('')

    break

# End