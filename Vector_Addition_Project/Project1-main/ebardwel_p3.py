#project part 3



def main():
    files = ["ebardwel_mat1.txt", "ebardwel_mat2.txt", "ebardwel_mat3.txt", "ebardwel_mat4.txt", "ebardwel_mat5.txt"]
    run_files(files)

#auto runs a list of files with matricies in them
def run_files(files):
    len_file = len(files)
    for i in range(len_file):
        for j in range(len_file):
            new_filename = "ebardwel_p3_out" + str(i+1) + str(j+1) + ".txt"
            mat1 = read_parse_file(files[i])
            mat2 = read_parse_file(files[j])
            if multi_check(mat1, mat2):
                new_mat = multiply_matrix(mat1, mat2)
                new_mat_str = matrix_print(new_mat)
                write_to_file(new_filename, "w", new_mat_str)
            else:
                write_to_file(new_filename, "w", "Error. Unable to multiply.")



#multiplies two matricies
def multiply_matrix(mat1, mat2):
    retmat = []
    total = 0
    col_mat1 = len(mat1[0])
    row_mat1 = len(mat1)
    col_mat2 = len(mat2[0])
    for k in range(row_mat1):
        retmat.append([])
        for j in range(col_mat2):
            for i in range(col_mat1):
                total += (float(mat1[k][i]) * float(mat2[i][j]))
            retmat[k].append(total)
            total = 0
    return retmat


#checks if two matricies have the same number of column in 1 as rows in 2
def multi_check(mat1, mat2):
    mat1_col = len(mat1[0])
    mat2_row = len(mat2)
    if mat1_col == mat2_row:
        return True
    return False

#writes to a file given a string and a file and writing type prefrence
def write_to_file(file_name, writing_prefrence, str):
    f = open(file_name, writing_prefrence)
    f.write(str)
    f.close()

#reads a file parses into 2d matrix
def read_parse_file(file_name):
    f = open(file_name, "r")
    retmatrix = []
    for line in f:
        retmatrix.append(line.split())
    f.close()
    return retmatrix


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
