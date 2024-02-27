import sys

def input_seq(f1,f2):
    with open(f1,'r') , open(file2,'r') :
        seq1 = f1.readline().strip()
        seq2 = f2.readline().strip()
    return seq1, seq2

def init_mat(rows,cols):
    matrix = [[0]*cols for _ in  range(rows)]
    for i in range(rows):
        matrix[i][0] = -i
    for j in range(cols):
        matrix[0][j] = -j
    return matrix

def Match(char1,char2):
    if char1==char2:
        return 1
    else:
        return -1

def global_alignment(seq1,seq2):
    rows,cols = len(seq1) + 1, len(seq2) + 1
    matrix = init_mat(rows, cols)

    for i in range(1,rows):
        for j in range(1, cols):
            match = matrix[i-1][j-1]+ Match(seq1[i-1], seq2[j-1])
            delete = matrix[i-1][j]- 1
            insert = matrix[i][j-1]- 1
            matrix[i][j] = max(match, delete, insert)

    align1,align2 = '', ''
    i, j = len(seq1), len(seq2)
    while i>0 or  j> 0:
        if i >0 and j>0 and max(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1]) == matrix[i-1][j-1]:
            align1 = seq1[i-1]+ align1
            align2 = seq2[j-1]+  align2
            i -=1
            j -=1
        elif i > 0  and max(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1]) == matrix[i-1][j]:
            align1 =  seq1[i-1] + align1
            align2 = '-'+ align2
            i -= 1
        else:
            align1 = '-' +align1
            align2 = seq2[j-1] +align2
            j -= 1

    return align1,align2

if __name__ == "__main__":
   
        

    file1,file2 = sys.argv[1], sys.argv[2]
    seq1,seq2 = input_seq(file1,file2)
    seqout1, seqout2 = global_alignment(seq1,seq2)
    print("Sequence 1:",seqout1)
    print("Sequence 2:",seqout2)
