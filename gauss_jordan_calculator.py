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
        # Gives Tutorial

def gauss_and_matrixs():
    print("""In mathematics, Gaussian elimination, also known as row reduction, is an algorithm for 
    solving systems of linear equations. It consists of a sequence of row-wise operations 
    performed on the corresponding matrix of coefficients. This method can also be used to 
    compute the rank of a matrix, the determinant of a square matrix, and the inverse of an 
    invertible matrix. The method is named after Carl Friedrich Gauss (1777–1855). To perform 
    row reduction on a matrix, one uses a sequence of elementary row operations to modify 
    the matrix until the lower left-hand corner of the matrix is filled with zeros, as much as possible. 
    There are three types of elementary row operations:
        Swapping two rows,
        Multiplying a row by a nonzero number,
        Adding a multiple of one row to another row.')
    """)
    cont = input('Press any key to continue: ')
    if cont:
        clear_screen()
        return

def needs_help():
    clear_screen()
    print('TUTORIAL:\n')
    print('Welcome to the Gauss Jordan Calculator!\n')
    wantinfo = input('Would you to know what Gauss Jordan is (And info on Matrixs? (Y/N): ')
    if wantinfo == 'Y':
        gauss_and_matrixs()
    clear_screen()
    print('-------------------------------------------------------------------------------')
    print('A linear equation is a where numbers are added or subtracted with unknown values\nE.g: 1A + 3B - 2C = 4')
    print('A matrix is multiple linear equations')    
    print('Example matrix:')
    print('\n2A, 4B, 3C =7\n5A, 5B, 2C = 2\n\n= 2 Rows\n= 3 Unknowns')
    print('\nMy calculator can solve for A, B and C (in this example), \nIt will prompt you to enter column numbers and repeats for X number of rows')
    print('Try it out now!')
    print('-------------------------------------------------------------------------------')
    cont = input('Press any key to continue: ')
    if cont:
        return

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
def linear_equation():
    unknown = input('Number of unknown variables\n(3 = A, B, C)\n(2 = A, B)\netc..\nInput: ')
    # row = input('Number of rows in matrix\nInput: ')
    row = unknown
    if not unknown.isdigit() or not row.isdigit():
        print('Enter a valid Numeric Digit!')
        return False
    else:
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
        raise ValueError("SPECIAL CASE! Pivot element is zero, cannot normalize the row.")
    
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
    print('\nWelcome to the Gauss Jordan Calculator!')
    print('\nNote: This calculator is for SQUARE matrixes only\n')
    need_help = input('Would you like a tutorial? (Y/N): ')

    if need_help == 'Y':
        needs_help()

    clear_screen()
# -----------------------------------------------------------------------------
            # MATRIX DIMENSIONS
    
        # Dimensions passed to Matrix generator 
        # linear_equations(columns, rows)
    while True:
        equations = linear_equation()
        if equations == False:
            equations = linear_equation()
        else:
            break
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