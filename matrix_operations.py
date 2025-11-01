
# MATRIX FILL
size = 1
def MatrixInput():
    global size
    # create the matrix
    matrix = []

    # fill by rows
    for i in range(size):

        #fill by columns
        for a in range(size):
            elem = int(input(f"Enter element {a+1} of ROW {i+1}: "))
            matrix.append(elem)

    DisplayMatrix(matrix)
    return matrix

# SHOW THE 1D ARRAY IN SQUARE MATRIX FORM
def DisplayMatrix(matrix):
    global size
    for i in range(size):
        row = matrix[i*size:(i+1)*size]
        print(row)

# ------------------------------------- MAIN ------------------------------------- #
print("--- SQUARE Matrix Operations: Addition and Scalar Multiplication ---\n\n")


mode = input("\nType mode 'add' for addition, or 'scale' for scalar multiplication\n:").strip().lower()


#INPUT VALIDATION
while mode != 'add' and mode != 'scale':
    mode = input("Wrong input mode, enter 'add' or 'scale' please\n: ").strip().lower()

# ADDITION
if mode == 'add':
    print("- SELECTED ADDITION -\n")
    size = int(input("Enter SQUARE matrix dimensions (n x n), enter n\n: "))
    print("FILL FIRST MATRIX:")
    mat1 = MatrixInput()
    print("FILL SECOND MATRIX:")
    mat2 = MatrixInput()


    # ADD THE MATRICES
    result = [(mat1[i] + mat2[i]) for i in range(len(mat1))]
    print("- RESULTANT MATRIX - :\n")
    DisplayMatrix(result)


# SCALAR MULT
elif mode == 'scale':
    print("- SELECTED SCALE MODE -\n")
    size = int(input("Enter SQUARE matrix dimensions (n x n), enter n\n: "))
    mat1 = MatrixInput()
    scalar = int(input("Enter the SCALAR to multiply the matrix by\n: "))
    result = [mat1[i] * scalar for i in range(len(mat1))]
    DisplayMatrix(result)

 