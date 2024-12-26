print('\nWelcome to the Gaussian elimination calculator!\n')
print('The goal of this calculator is to solve a system of linear equations \nby converting a matrix into reduced echelon form!\n')

import random
import copy

# EXAMPLE MATRIX GENERATOR
def math_random_small_int(small = True, medium = True, big = True):
    # Generates random number for creating an example Matrix
    # Returns random num based on units of size (small, medium, large)
    if small == True and medium == False and big == False:
        return random.randint(0, 15)
    if small == False and medium == True and big == False:
        return random.randint(15, 30)
    if small == False and medium == False and big == True:
        return random.randint(30, 100)

# MATRIX MAKER (NO FAIL CHECKING YET)
def linear_equation(unknown, row, column):
    # Takes dimensions of matrix
    unknown = int(unknown)  # Number of unknown variables (A, B, C, etc..)
    row = int(row)  # Size of row 
    column = int(column)    # Size of column
    if unknown > 0:
        # Empty Dict for full equations
        fullequations = {} 
 
        # Example matrix (Random number generator)
        print(f"""\nNote! each equation must follow the same structure!:
            example:
            {math_random_small_int(True, False, False)}A + {math_random_small_int(True, False, False)}B - {math_random_small_int(True, False, False)}C = {math_random_small_int()}
        

        """)

        # Prompts input of linear equations (based on number of rows)
        for rownum in range(1, (row + 1), 1):
            
            # States what row of linear equations is to be inputed
            print(f"Currently on row{rownum}!") 
            
            equations = [] 
            # Empty list for each linear equation
            
            # Prompts input for each column of linear equation
            for colnum in range(1, (unknown + 2), 1): 

                # Last column of matrix = Determinant, prompt user for awnser (eg. 3A = 9)
                if colnum == unknown + 1:
                    determinant = input(f'Determinant of matrix =')
                    equations.append(determinant)
                else:
                    # Asks user to put in equations per column (in a single equation)
                    equations.append(input(f'Input equation in column{colnum} of the matrix: '))        

            # Appends lists of equations into dictionary
            fullequations[f"row{rownum}"] = equations
        
        return fullequations


# CALCULATOR

# Turns numbers inside column into 0's
# (IGNORES current working pivot position)
def pivotcolnums(currentnum, size):
    currentnum = int(currentnum)
    size = int(size)


# ROW REDUCER
# Reduces row based on pivot position,
# Returns reduced row (RowA = 1/Pivot X RowA)
def rowoperation(item, pivotposition):
    item = int(item)
    pivotposition = int(pivotposition)
    item = item / pivotposition
    return item

# Takes out equations, passes items to functions in correct order
def gauss_jordan_operation(equations):
    currentrow = -1
    currentcol = 0
    emptydict = {}
    for matrix_rows in equations.values():
        currentrow += 1        
        currentcol += 1
        emptylist = []
        for items in matrix_rows:
            operation = rowoperation(items, matrix_rows[currentrow])
            emptylist.append(operation)
        emptydict[f"row{currentrow}"] = emptylist
        # Pass each row into zero maker
        # pivotcolnums(currentrow, len(equations))

        print(emptylist)
        print(f"Reducing to zero on Column{currentcol}, Row{currentrow}")


    return emptydict

# Calculator menu
while True:
    needs_help = input('Would you like a tutorial? (Y/N): ')

    # Prompts user for matrix dimensions
    unknown_size = input('Input number of unknown variables: ')
    row_size = input('Number of rows in matrix: ')
    column_size = input('Number of columns: ')
    # Passes dimensions into equation creator function
    equations = linear_equation(unknown_size, row_size, column_size)

    # Copies matrix of numbers into matrix with letters
    equationscopy = copy.deepcopy(equations)
    print('\nCURRENT MATRIX:\n')

    # Letters used to represent order of unknowns
    original_suffixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Showcases matrix with variables
    determinantcounter = 0
    for key in equationscopy:
        suffixes = original_suffixes.copy() # Make a copy of the suffix list for each row
        for i in range(len(equationscopy[key]) - 1):  # Skip the last value
            if not suffixes:
                suffixes = original_suffixes.copy()
            equationscopy[key][i] = equationscopy[key][i] + suffixes.pop(0).upper()
        # Updates value of last item:
        determinantcounter += 1
        equationscopy[key][-1] = (f"Det{determinantcounter} = {equationscopy[key][-1]}")

    # Prints new, copied matrix in order (with Suffixes)
    for systemsofequations in equationscopy.values():
        print(systemsofequations)

    # DATA FILLED
    # MATRIX DATA CONVERTED/ADJUSTED/FAILCHECKED
    # CALCULATIONS BEGIN BELOW:

    print('\nBeginning elementary row operations!')
    
    # Data is put into calculator. 
    equations = gauss_jordan_operation(equations)


    # for systemsofequations in equations.values():
    #     print(systemsofequations)