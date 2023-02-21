#ebardwel 9/10/2021
#this program takes in the files made by ebardwel_p1 and
#adds each matrix together putting the result in a new file
#as addition is associative There will only need to be 15 files rather than 25


def main():
    #go go gadget autorun
    files = ["ebardwel_mat1.txt", "ebardwel_mat2.txt", "ebardwel_mat3.txt", "ebardwel_mat4.txt", "ebardwel_mat5.txt"]
    matched_files = build_files_matrix(files)
    autorun(files, matched_files)
    #autorun stuff is at the eof

#Adds two matricies given two files containing one matrix if they are addable
#if they are not addable output file will return an error
def matrix_addition(mat1_file, mat2_file, return_file):
    mat1 = read_parse_file(mat1_file)
    mat2 = read_parse_file(mat2_file)
    if compare_len(mat1, mat2):
        matrix_added = add_string_matrix(mat1, mat2)
        matrix_added_str = matrix_print(matrix_added)
        write_to_file(return_file, "w", matrix_added_str)
        return None
    error = "files " + mat1_file + " and " + mat2_file + " cannot be added"
    write_to_file(return_file, "w", error)


#writes to a file given a string and a file and writing type prefrence
def write_to_file(file_name, writing_prefrence, str):
    f = open(file_name, writing_prefrence)
    f.write(str)
    f.close()


#iterates over two full matricies mat1 and mat2
#converts matrix[i][j] to float and adds them
#returns 3rd matrix of all added values returns float
def add_string_matrix(mat1, mat2):
    row = len(mat1)
    col = len(mat1[0])
    retmat = []
    for i in range(row):
        retmat.append([])
        for j in range(col):
            retmat[i].append(float(mat1[i][j]) + float(mat2[i][j]))

    return retmat


#compare length of two matrix
#used to see if matrix are addable
def compare_len(mat_1, mat_2):
    mat_1row = len(mat_1)
    mat_1col = len(mat_1[0])
    mat_2row = len(mat_2)
    mat_2col = len(mat_2[0])

    if (mat_1row == mat_2row) and (mat_1col == mat_2col):
        return True
    return False

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


#this will list the files in a 2d matrix. based on matches needed
#to show every possible combination for the matrix files
#this considers matrix additions commutative property A + B == B + A
#The index is the file you compare to the others in that index's list
def build_files_matrix(files):
    retmatrix = []
    leng = len(files) - 1
    temp = leng
    for i in range(len(files)):
        retmatrix.append([])
        for j in range(len(files) - i):
            retmatrix[i].append(leng)
            leng -= 1
        leng = temp
    return retmatrix

#autogenerates requested files
def autorun(files, matched_files):
    for i in range(len(matched_files)):
        for j in range(len(matched_files[i])):
            mat_file1 = files[i]
            mat_file2 = files[(matched_files[i][j])]
            new_filename = "ebardwel_p2_out" + str(i+1) + str(5-j) + ".txt"
            matrix_addition(mat_file1, mat_file2, new_filename)


#go go __main__gadget
if __name__ == '__main__':
    main();
