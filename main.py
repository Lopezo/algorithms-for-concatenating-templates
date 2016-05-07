import mixer as m

if __name__ == "__main__":
    print('Example of concatenation:')
    B = m.Mixer(3, '0 0 0; 0 1 1; 0 1 2')
    print(B, 'B \n')
    C = m.Mixer(2, '0 -1; -1 -1')
    print(C, 'C \n')
    D = B.concatenate_before(C)
    print(D, 'B+C=D \n')
    print('D can be export in a matrix and an array form')
    D.export_to_matrix_and_array()
    print('\n---- ---- ---- ----')
    print('Another example of concatenation:')
    A = m.Mixer(2, '0 0; 0 1')
    print(A, 'A \n')
    B = A.concatenate_before(A)
    print(B, 'A+A=B')
