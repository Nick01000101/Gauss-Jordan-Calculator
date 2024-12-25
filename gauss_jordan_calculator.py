print('\nWelcome to the Gaussian elimination calculator!\n')
print('The goal of this calculator is to solve a system of linear equations \nby converting a matrix into reduced echelon form!\n')

import random
import copy

# EXAMPLE MATRIX GENERATOR
def math_random_small_int(small = True, medium = True, big = True):
    if small == True and medium == False and big == False:
        return random.randint(0, 15)
    if small == False and medium == True and big == False:
        return random.randint(15, 30)
    if small == False and medium == False and big == True:
        return random.randint(30, 100)

# MATRIX MAKER (NO FAIL CHECKING YET)
def linear_equation(unknown, row, column):
    unknown = int(unknown)
    row = int(row)
    column = int(column)
    if unknown > 0:

        fullequations = {}
 
        print(f"""\nNote! each equation must follow the same structure!:
            example:
            {math_random_small_int(True, False, False)}A + {math_random_small_int(True, False, False)}B - {math_random_small_int(True, False, False)}C = {math_random_small_int()}
        

        """)

        for rownum in range(1, (row + 1), 1):
            # newrow = input(f'Input equation in row{_} of the matrix: ')
            print(f"Currently on row{rownum}!")
            equations = []
            for colnum in range(1, (unknown + 2), 1):
                if colnum == unknown + 1:
                    determinant = input(f'Determinant of matrix =')
                    # determinant = (f"Det{rownum} = {determinant}")
                    equations.append(determinant)
                else:
                    equations.append(input(f'Input equation in column{colnum} of the matrix: '))        
        
            fullequations[f"row{rownum}"] = equations

        return fullequations


# CALCULATOR

def pivotcolnums(currentnum, size):
    currentnum = int(currentnum)
    size = int(size)




def rowoperation(item, pivotposition):
    item = int(item)
    pivotposition = int(pivotposition)
    item = item / pivotposition
    return item


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


while True:
    needs_help = input('Would you like a tutorial? (Y/N): ')


    unknown_size = input('Input number of unknown variables: ')
    row_size = input('Number of rows in matrix: ')
    column_size = input('Number of columns: ')
    equations = linear_equation(unknown_size, row_size, column_size)

    equationscopy = copy.deepcopy(equations)
    print('\nCURRENT MATRIX:\n')

    original_suffixes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # Showcase matrix with variables
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


    for systemsofequations in equationscopy.values():
        print(systemsofequations)

    print('\nBeginning elementary row operations!')
    
    equations = gauss_jordan_operation(equations)
    # for systemsofequations in equations.values():
    #     print(systemsofequations)