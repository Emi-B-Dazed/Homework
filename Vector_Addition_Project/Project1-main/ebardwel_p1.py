# linear algebra hw1
# Emily Bardwell 9/9/2021 ebardwel@uccs.edu
# make de matrix

#main will handle calling the functions since this is a small one and no
#ui development was requested in rubric
def main():
    #my name
    first = "Emily";
    last = "Bardwell";
    first_len = len(first);
    last_len = len(last);

    #mat_1
    mat_1 = increment_matrix_col(first_len, last_len, 1, 1)
    mat_str_1 = matrix_print(mat_1)
    write_to_file("ebardwel_mat1.txt", "w", mat_str_1)


    #mat_2
    mat_2 = increment_matrix_row(last_len, first_len, 3, 3)
    mat_str_2 = matrix_print(mat_2)
    write_to_file("ebardwel_mat2.txt", "w", mat_str_2)


    #mat_3
    mat_3 = increment_matrix_row(last_len, first_len, .4, .3)
    mat_str_3 = matrix_print(mat_3)
    write_to_file("ebardwel_mat3.txt", "w", mat_str_3)


    #mat_4
    mat_4 = increment_matrix_row(6, 13, 2, 2)
    mat_str_4 = matrix_print(mat_4)
    write_to_file("ebardwel_mat4.txt", "w", mat_str_4)


    #mat_5
    mat_5 = increment_matrix_col(6, 13, -7, 1)
    mat_str_5 = matrix_print(mat_5)
    write_to_file("ebardwel_mat5.txt", "w", mat_str_5)


def write_to_file(file_name, writing_prefrence, str):
    f = open(file_name, writing_prefrence)
    f.write(str)
    f.close()

#makes 2d matrix indicies over columns first then rows
#row and col are the number of rows and columns
#start is where the callee wants the matrix to start with Position(0,0)
#incr is the amount incremented each cycle
def increment_matrix_col(row, col, start, incr):
    matrix = []
    for i in range(row):
        matrix.append([])
        for j in range(col):
            matrix[i].append(start)
            start += incr

    return matrix;

#had issues getting this one to work incrementing the rows first
#So went with a mathmatical formula that calculates what an index is given
#matrix the total number of rows the starting number the index Position and the increment
#otherwise basically works the same as col
def increment_matrix_row(row, col, start, incr):
    matrix = []
    base = 1
    for i in range(row):
        matrix.append([])
        for j in range(col):
            count = (incr * ((row * j) + i)) + start
            matrix[i].append(count)

    return matrix;

#creates a string out of a 2d matrix with tab spaces inbetween each column
#and a new line for each row.
def matrix_print(matrix):
    ret_str = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            ret_str += str(matrix[i][j])
            ret_str += "\t"
        ret_str += "\n"
    return ret_str;

#go go __main__gadget
if __name__ == '__main__':
    main();
