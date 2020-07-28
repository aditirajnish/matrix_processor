def process_elements(i=2, msg=""):
    if i == 1:
        x = tuple(map(float, input(msg).rstrip().split()))
        return x
    m, n = tuple(map(int, input(msg).rstrip().split()))
    return m, n


def transpose():
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    c = int(input("Your choice: "))

    m, n = process_elements(msg="Enter matrix size: ")
    print("Enter matrix:")
    matrix = []
    for _ in range(m):
        row = process_elements(1)
        matrix.append(row)
    transposed_matrix = []

    if c == 1:
        for j in range(n):
            row = []
            for i in range(m):
                row.append(matrix[i][j])
            transposed_matrix.append(row)
    elif c == 2:
        for j in range(n - 1, -1, -1):
            row = []
            for i in range(m - 1, -1, -1):
                row.append(matrix[i][j])
            transposed_matrix.append(row)
    elif c == 3:
        for i in range(m):
            row = []
            for j in range(n - 1, -1, -1):
                row.append(matrix[i][j])
            transposed_matrix.append(row)
    else:
        for i in range(m - 1, -1, -1):
            transposed_matrix.append(matrix[i])

    print("The result is:")
    for row in transposed_matrix:
        print(*row)
    print()


def multiply_m():
    i, j1 = process_elements(msg="Enter size of first matrix: ")
    print("Enter first matrix: ")
    matrix_1 = []
    for _ in range(i):
        row = process_elements(1)
        matrix_1.append(row)

    j2, k = process_elements(msg="Enter size of second matrix: ")
    print("Enter second matrix: ")
    matrix_2 = []
    for _ in range(j2):
        row = process_elements(1)
        matrix_2.append(row)

    if j1 == j2:
        product_matrix = []
        for x in range(i):
            products = []
            for y in range(k):
                product = 0
                for z in range(j2):
                    product += matrix_1[x][z] * matrix_2[z][y]
                products.append(product)
            product_matrix.append(products)

        print("The result is:")
        for product in product_matrix:
            print(*product)
        print()

    else:
        print("The operation cannot be performed.\n")


def multiply_c():
    m, n = process_elements(msg="Enter size of matrix: ")
    print("Enter matrix: ")
    matrix = []
    for i in range(m):
        row = process_elements(1)
        matrix.append(row)

    constant = int(input("Enter constant: "))

    matrix_product = []
    for i in range(m):
        new_row = []
        for j in range(n):
            new_element = matrix[i][j] * constant
            new_row.append(str(new_element))
        matrix_product.append(new_row)

    print("The result is:")
    for row in matrix_product:
        print(*row)
    print()


def add():
    m1, n1 = process_elements(msg="Enter size of first matrix: ")
    print("Enter first matrix:")
    matrix_1 = []
    for _ in range(m1):
        row = process_elements(1)
        matrix_1.append(row)

    m2, n2 = process_elements(msg="Enter size of second matrix: ")
    print("Enter second matrix:")
    matrix_2 = []
    for _ in range(m2):
        row = process_elements(1)
        matrix_2.append(row)

    if m1 == m2 and n1 == n2:
        matrix_sum = []
        for row_1, row_2 in zip(matrix_1, matrix_2):
            new_row = []
            for element_1, element_2 in zip(row_1, row_2):
                new_element = element_1 + element_2
                new_row.append(str(new_element))
            matrix_sum.append(new_row)
        print("The result is:")
        for row in matrix_sum:
            print(*row)
        print()
    else:
        print("The operation cannot be performed.\n")


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
0. Exit""")
    choice = int(input("Your choice: "))
    print()
    if choice == 1:
        add()
    elif choice == 2:
        multiply_c()
    elif choice == 3:
        multiply_m()
    elif choice == 4:
        transpose()
    else:
        break
