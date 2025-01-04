import random
import copy
import os
import time
import sys

# ----------Gauss-Jordan-Eliminaton-calculator----------------------------------
# ------------------------------------------------Written by Nick Sevostiyanov--

# Clears screen
def clear_screen():
    # For windows
    if os.name == 'nt':
        os.system('cls')
    else:
        # For Unix/Linux/Mac
        os.system('clear')


def show_loading(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        for i in range(4):
            sys.stdout.write('\rloading' + '.' * i)
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write('\rDone!        \n')





# Example matrix generator
def math_random_small_int(small=True, medium=True, big=True):
    if small and not medium and not big:
        return random.randint(0, 15)
    if not small and medium and not big:
        return random.randint(15, 30)
    if not small and not medium and big:
        return random.randint(30, 100)

# Matrix maker (no fail checking yet)
def linear_equation(unknown, row, column):
    unknown = int(unknown)
    row = int(row)
    column = int(column)
    if unknown > 0:
        fullequations = {}

        print("Input linear equations (example: 3A + 2B - C = 4)")

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

# Row normalization (with pivot checking)
def row_normalization(matrix, row):
    dictrow = row + 1
    pivot = matrix[f"row{dictrow}"][row]
    
    if float(pivot) == 0:
        raise ValueError("Pivot element is zero, cannot normalize the row.")
    
    pivot = float(pivot)
    
    for index in range(len(matrix[f"row{dictrow}"])):
        matrix[f"row{dictrow}"][index] = float(matrix[f"row{dictrow}"][index]) / pivot

    return matrix

# Row swapping function for partial pivoting
def swap_rows(matrix, row1, row2):
    matrix[f"row{row1}"], matrix[f"row{row2}"] = matrix[f"row{row2}"], matrix[f"row{row1}"]
    return matrix

# Column elimination function (correcting the logic)
def col_elimination(equations, operation):
    pivot_row = equations[f"row{operation + 1}"]
    
    for row_num, row in equations.items():
        if row_num != f"row{operation + 1}":
            pivot_element = float(row[operation])
            
            if pivot_element != 0:
                for i in range(len(row)):
                    row[i] = float(row[i]) - pivot_element * float(pivot_row[i])

    return equations

# Main loop (for testing)
while True:
    needs_help = input('Would you like a tutorial? (Y/N): ')

    unknown_size = input('Input number of unknown variables: ')
    row_size = input('Number of rows in matrix: ')
    column_size = input('Number of columns: ')
    
    equations = linear_equation(unknown_size, row_size, column_size)

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

    for systemsofequations in equationscopy.values():
        print(systemsofequations)

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
    
    def print_last_items(equations):
        suffixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for index, (key, value) in enumerate(equations.items()):
            if index < len(suffixes):
                suffix = suffixes[index]
            else:
                suffix = suffixes[index % len(suffixes)]
            print(f"{suffix} = {value[-1]}")



    clear_screen()

    print('\nFINAL MATRIX:\n')

    equationscopy = copy.deepcopy(equations)
    show_loading(3)
    print('\nFINAL MATRIX:\n')

    for final in equations.values():
        print(final)

    print('\nTherefor: \n')
    print_last_items(equations)

    break